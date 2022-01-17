import unittest
from unittest.mock import *
from src.senkalib.chain.osmosis.osmosis_transaction import OsmosisTransaction
import json
from pathlib import Path
import os
from decimal import *

class TestOsmosisTransaction(unittest.TestCase):
  def test_get_timestamp(self):
    swap_transaction = json.loads(Path('%s/../../testdata/osmosis/swap.json' % os.path.dirname(__file__)).read_text())
    transaction = OsmosisTransaction(swap_transaction)
    timestamp = transaction.get_timestamp()
    self.assertEqual(timestamp, '2022-01-16 09:03:30')

  def test_get_transaction_fee(self):
    swap_transaction = json.loads(Path('%s/../../testdata/osmosis/swap.json' % os.path.dirname(__file__)).read_text())
    transaction = OsmosisTransaction(swap_transaction)
    fee = transaction.get_transaction_fee()
    self.assertEqual(fee, Decimal('0'))

if __name__ == '__main__':
  unittest.main()