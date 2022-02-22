import unittest
from unittest.mock import *
from src.senkalib.chain.osmosis.osmosis_transaction_generator import OsmosisTransactionGenerator
import json
from pathlib import Path
import os
from src.senkalib.senka_setting import SenkaSetting
from unittest.mock import *
from decimal import *

class TestOsmosisTransactionGenerator(unittest.TestCase):
  def test_get_transactions(self):
    settings = SenkaSetting({})

    with patch.object(OsmosisTransactionGenerator, 'get_txs', new=TestOsmosisTransactionGenerator.mock_get_txs):
      transactions = OsmosisTransactionGenerator.get_transactions(settings, 'osmo1xq5du8upw2fmyx7h43w8uqv47vln70hre92wvm', None, {})
      timestamp = transactions[0].get_timestamp()
      fee = transactions[0].get_transaction_fee()
      self.assertEqual(len(transactions), 44)
      self.assertEqual(timestamp, '2022-01-15 12:18:55')
      self.assertEqual(fee, Decimal(33))

      transactions = OsmosisTransactionGenerator.get_transactions(settings, 'osmo1xq5du8upw2fmyx7h43w8uqv47vln70hre92wvm', None, {'endblock': 14700510})
      self.assertEqual(len(transactions), 40)

  @classmethod
  def mock_get_txs(cls, settings:dict, address:str, arg_startblock:int = None, arg_endblock:int = None, arg_page:int = None):
    transactions = json.loads(Path('%s/../../testdata/chain/osmosis/test_transactions.json' % os.path.dirname(__file__)).read_text())
    return transactions

if __name__ == '__main__':
  unittest.main()