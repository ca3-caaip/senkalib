from math import inf
from typing import List, Union

from senkalib.chain.cosmostation_api_client import (
    CosmostationApiClient,
    osmosis_tx_history_records,
)
from senkalib.chain.osmosis.osmosis_transaction import OsmosisTransaction
from senkalib.chain.transaction_generator import TransactionGenerator
from senkalib.senka_setting import SenkaSetting


class OsmosisTransactionGenerator(TransactionGenerator):
    chain = "osmosis"

    @classmethod
    def get_transactions(
        cls,
        settings: SenkaSetting,
        address: str,
        startblock: Union[int, None] = None,
        endblock: Union[int, None] = None,
        starttime: Union[int, None] = None,
        endtime: Union[int, None] = None,
    ) -> List[OsmosisTransaction]:
        startblock = startblock if startblock is not None else 0
        endblock = endblock if endblock is not None else inf
        starttime = starttime if starttime is not None else 0
        endtime = endtime if endtime is not None else inf

        return list(
            map(
                OsmosisTransaction,
                CosmostationApiClient.get_transactions_by_address(chain=cls.chain, address=address,
                                                                  startblock=startblock, endblock=endblock,
                                                                  starttime=starttime, endtime=endtime,
                                                                  cache=osmosis_tx_history_records),
            )
        )
