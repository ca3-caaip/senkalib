import json
import os
import unittest
from pathlib import Path

from src.senkalib.platform.bsc.bsc_transaction import BscTransaction


class TestBscTransaction(unittest.TestCase):
    def test_get_timestamp(self):
        header = json.loads(
            Path(
                "%s/../../testdata/platform/bsc/header.json" % os.path.dirname(__file__)
            ).read_text()
        )
        receipt = json.loads(
            Path(
                "%s/../../testdata/platform/bsc/transaction_receipt/approve.json"
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
                "%s/../../testdata/platform/bsc/header.json" % os.path.dirname(__file__)
            ).read_text()
        )
        receipt = json.loads(
            Path(
                "%s/../../testdata/platform/bsc/transaction_receipt/approve.json"
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
