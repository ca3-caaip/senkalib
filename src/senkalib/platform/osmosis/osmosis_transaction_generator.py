import sys
from typing import List

from senkalib.platform.cosmostation_api_client import (
    CosmostationApiClient,
    osmosis_tx_history_records,
)
from senkalib.platform.osmosis.osmosis_transaction import OsmosisTransaction
from senkalib.platform.transaction_generator import TransactionGenerator


class OsmosisTransactionGenerator(TransactionGenerator):
    platform = "osmosis"

    @classmethod
    def get_transactions(cls, transaction_params: dict) -> List[OsmosisTransaction]:
        if transaction_params["type"] != "address":
            raise ValueError("type must be 'address'")
        return list(
            map(
                OsmosisTransaction,
                CosmostationApiClient.get_transactions_by_address(
                    platform=cls.platform,
                    address=transaction_params["data"],
                    startblock=transaction_params.get("startblock", 0),
                    endblock=transaction_params.get("endblock", sys.maxsize),
                    starttime=transaction_params.get("starttime", 0),
                    endtime=transaction_params.get("endtime", sys.maxsize),
                    cache=osmosis_tx_history_records,
                ),
            )
        )
