import sys
from typing import List

from senkalib.chain.cosmostation_api_client import (
    CosmostationApiClient,
    kava_tx_history_records,
)
from senkalib.chain.kava.kava_transaction import KavaTransaction
from senkalib.chain.transaction_generator import TransactionGenerator


class KavaTransactionGenerator(TransactionGenerator):
    chain = "kava"

    @classmethod
    def get_transactions(cls, transaction_params: dict) -> List[KavaTransaction]:
        if transaction_params["type"] != "address":
            raise ValueError("type must be 'address'")

        return list(
            map(
                KavaTransaction,
                CosmostationApiClient.get_transactions_by_address(
                    chain=cls.chain,
                    address=transaction_params["data"],
                    startblock=transaction_params.get("startblock", 0),
                    endblock=transaction_params.get("endblock", sys.maxsize),
                    starttime=transaction_params.get("starttime", 0),
                    endtime=transaction_params.get("endtime", sys.maxsize),
                    cache=kava_tx_history_records,
                ),
            )
        )
