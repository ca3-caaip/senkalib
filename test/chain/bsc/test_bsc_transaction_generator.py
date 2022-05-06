import json
import os
import unittest
from pathlib import Path
from typing import Union
from unittest.mock import patch

from web3.eth import Eth

from src.senkalib.chain.bsc.bsc_transaction_generator import BscTransactionGenerator
from src.senkalib.senka_setting import SenkaSetting


class TestBscTransactionGenerator(unittest.TestCase):
    def test_get_transactions(self):
        settings = SenkaSetting({})
        with patch.object(
            BscTransactionGenerator,
            "get_txs",
            new=TestBscTransactionGenerator.mock_get_txs,
        ):
            with patch.object(
                Eth,
                "get_transaction_receipt",
                new=TestBscTransactionGenerator.mock_get_transaction_receipt,
            ):
                transactions = BscTransactionGenerator.get_transactions(
                    settings,
                    "0x0Dee38f987ca1EFE37da2cC39c6b2ace0A61A95A",
                    startblock=13526335,
                    endblock=14353208,
                )
                timestamp = transactions[0].get_timestamp()
                fee = transactions[0].get_transaction_fee()

                self.assertEqual(timestamp, "2021-12-28 01:30:55")
                self.assertEqual(fee, 222150000000000)

    @classmethod
    async def mock_get_txs(
        cls,
        settings: dict,
        address: str,
        arg_startblock: Union[int, None] = None,
        arg_endblock: Union[int, None] = None,
        arg_page: Union[int, None] = None,
    ):
        header = json.loads(
            Path(
                "%s/../../testdata/chain/bsc/header.json" % os.path.dirname(__file__)
            ).read_text()
        )
        return [header]

    @classmethod
    def mock_get_transaction_receipt(cls, transaction_hash):
        receipt = json.loads(
            Path(
                "%s/../../testdata/chain/bsc/transaction_receipt/approve.json"
                % os.path.dirname(__file__)
            ).read_text()
        )
        return receipt


if __name__ == "__main__":
    unittest.main()
