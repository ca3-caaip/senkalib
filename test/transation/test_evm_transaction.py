import unittest
from unittest.mock import *
from src.senkalib.transaction.evm_transaction import EvmTransaction
import json
from pathlib import Path
import os

class TestEvmTransaction(unittest.TestCase):
  def test_get_timestamp(self):
    header = json.loads(Path('%s/../testdata/evm/header.json' % os.path.dirname(__file__)).read_text())
    receipt = json.loads(Path('%s/../testdata/evm/transaction_receipt/approve.json' % os.path.dirname(__file__)).read_text())
    transaction = EvmTransaction(header['hash'], receipt, header['timeStamp'], header['gasUsed'], header['gasPrice'])
    timestamp = transaction.get_timestamp()
    self.assertEqual(timestamp, '2021-12-28 01:30:55')


if __name__ == '__main__':
  unittest.main()