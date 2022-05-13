import sys
from dataclasses import dataclass
from operator import attrgetter
from time import sleep
from typing import List, Union

import requests
from dateutil import parser


@dataclass
class CosmostationTxApiHistoryRecord:
    id: int
    timestamp: int


osmosis_tx_history_records: List[CosmostationTxApiHistoryRecord] = sorted(
    [
        CosmostationTxApiHistoryRecord(2, 1624052574),  # 2021-06-18T21:42:54Z
        CosmostationTxApiHistoryRecord(455035, 1625097604),  # 2021-07-01T00:00:04Z
        CosmostationTxApiHistoryRecord(1207598, 1627776001),  # 2021-08-01T00:00:01Z
        CosmostationTxApiHistoryRecord(2284219, 1630454401),  # 2021-09-01T00:00:01Z
        CosmostationTxApiHistoryRecord(3815804, 1633046402),  # 2021-10-01T00:00:02Z
        CosmostationTxApiHistoryRecord(5802050, 1635724801),  # 2021-11-01T00:00:01Z
        CosmostationTxApiHistoryRecord(8282434, 1638316803),  # 2021-12-01T00:00:03Z
        CosmostationTxApiHistoryRecord(11802509, 1640995203),  # 2022-01-01T00:00:03Z
        CosmostationTxApiHistoryRecord(11843943, 1641027605),  # 2022-01-01T09:00:05Z
    ],
    key=attrgetter("id"),
)


kava_tx_history_records: List[CosmostationTxApiHistoryRecord] = sorted(
    [], key=attrgetter("id")
)


class CosmostationApiClient:
    @classmethod
    def sort_transactions_order(cls, transactions: List[dict]) -> List[dict]:
        transactions = sorted(transactions, key=lambda x: x["header"]["id"])
        return transactions

    @classmethod
    def get_transactions_by_address(
        cls,
        chain: str,
        address: str,
        startblock: Union[int, None] = 0,
        endblock: Union[int, None] = sys.maxsize,
        starttime: Union[int, None] = 0,
        endtime: Union[int, None] = sys.maxsize,
        cache: List[CosmostationTxApiHistoryRecord] = [],
    ) -> List[dict]:
        startblock = startblock if startblock is not None else 0
        endblock = endblock if endblock is not None else sys.maxsize
        starttime = starttime if starttime is not None else 0
        endtime = endtime if endtime is not None else sys.maxsize

        total_result: list[dict] = []
        id_cursor = get_nearest_id(endtime, cache)

        while True:
            result = cls.get_txs(chain, address, id_cursor)
            for tx in result:
                id_cursor = int(tx["header"]["id"])
                block_id = int(tx["data"]["height"])
                time = to_timestamp(tx["header"]["timestamp"])

                if starttime <= time <= endtime and startblock <= block_id <= endblock:
                    total_result.append(tx)

                if time < starttime or block_id < startblock:
                    return cls.sort_transactions_order(total_result)
                else:
                    continue

            if len(result) < 50:
                return cls.sort_transactions_order(total_result)

            sleep(1)

    @classmethod
    def get_txs(cls, chain: str, address: str, id_from: int) -> List[dict]:
        url = f"https://{get_cosmostation_api_host(chain)}.cosmostation.io/v1/account/new_txs/{address}"
        params = {"from": id_from, "limit": 50}
        headers = {
            "Origin": "https://www.mintscan.io",
            "Referer": "https://www.mintscan.io/",
        }  # workaround from 2022-04-25: both origin and referer headers are required
        return requests.get(url, params=params, headers=headers).json()


COSMOSTATION_API_HOSTS = {
    "atom": "api",
    "kava": "api-kava",
    "osmosis": "api-osmosis",
}


def get_cosmostation_api_host(chain: str):
    host = COSMOSTATION_API_HOSTS.get(chain, None)
    if type(host) is not str:
        raise ValueError(
            f'{chain} is not implemented. check following supported chains: {",".join(list(COSMOSTATION_API_HOSTS.keys()))}'
        )
    return host


def get_nearest_id(time: int, cache: List[CosmostationTxApiHistoryRecord]):
    return next(map(attrgetter("id"), filter(lambda x: time < x.timestamp, cache)), 0)


def to_timestamp(iso8601string: str) -> int:
    return int(parser.parse(iso8601string).timestamp())
