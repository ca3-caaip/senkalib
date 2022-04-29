from math import inf
from typing import List
from senkalib.senka_setting import SenkaSetting
from senkalib.chain.cosmostation_api_client import (
    CosmostationApiClient,
    osmosis_tx_history_records,
)
from senkalib.chain.osmosis.osmosis_transaction import OsmosisTransaction
from senkalib.chain.transaction_generator import TransactionGenerator


class OsmosisTransactionGenerator(TransactionGenerator):
    chain = "osmosis"

    @classmethod
    def get_transactions(
        cls,
        settings: SenkaSetting,
        address: str,
        startblock: int = None,
        endblock: int = None,
        starttime: int = None,
        endtime: int = None,
    ) -> List[OsmosisTransaction]:
        startblock = startblock if startblock is not None else 0
        endblock = endblock if endblock is not None else inf
        starttime = starttime if starttime is not None else 0
        endtime = endtime if endtime is not None else inf

        return list(
            map(
                OsmosisTransaction,
                CosmostationApiClient.get_transactions_by_address(
                    chain=cls.chain,
                    address=address,
                    starttime=starttime,
                    endtime=endtime,
                    startblock=startblock,
                    endblock=endblock,
                    cache=osmosis_tx_history_records,
                ),
            )
        )
