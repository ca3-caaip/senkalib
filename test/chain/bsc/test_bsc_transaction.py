import unittest
from unittest.mock import *
from src.senkalib.chain.bsc.bsc_transaction import BscTransaction
import json
from pathlib import Path
import os


class TestBscTransaction(unittest.TestCase):
    def test_get_timestamp(self):
        header = json.loads(
            Path(
                "%s/../../testdata/chain/bsc/header.json" % os.path.dirname(__file__)
            ).read_text()
        )
        receipt = json.loads(
            Path(
                "%s/../../testdata/chain/bsc/transaction_receipt/approve.json"
                % os.path.dirname(__file__)
            ).read_text()
        )
        transaction = BscTransaction(
            header["hash"],
            receipt,
            header["timeStamp"],
            header["gasUsed"],
            header["gasPrice"],
        )
        timestamp = transaction.get_timestamp()
        self.assertEqual(timestamp, "2021-12-28 01:30:55")

    def test_get_transaction_fee(self):
        header = json.loads(
            Path(
                "%s/../../testdata/chain/bsc/header.json" % os.path.dirname(__file__)
            ).read_text()
        )
        receipt = json.loads(
            Path(
                "%s/../../testdata/chain/bsc/transaction_receipt/approve.json"
                % os.path.dirname(__file__)
            ).read_text()
        )
        transaction = BscTransaction(
            header["hash"],
            receipt,
            header["timeStamp"],
            header["gasUsed"],
            header["gasPrice"],
        )
        fee = transaction.get_transaction_fee()
        self.assertEqual(fee, 222150000000000)


if __name__ == "__main__":
    unittest.main()
