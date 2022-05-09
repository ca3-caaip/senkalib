import sys
from typing import List

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
        startblock: int = 0,
        endblock: int = sys.maxsize,
        starttime: int = 0,
        endtime: int = sys.maxsize,
    ) -> List[OsmosisTransaction]:
        return list(
            map(
                OsmosisTransaction,
                CosmostationApiClient.get_transactions_by_address(
                    chain=cls.chain,
                    address=address,
                    startblock=startblock,
                    endblock=endblock,
                    starttime=starttime,
                    endtime=endtime,
                    cache=osmosis_tx_history_records,
                ),
            )
        )
