import unittest
from unittest.mock import *
from src.senkalib.chain.kava.kava_transaction_generator import KavaTransactionGenerator
import json
from pathlib import Path
import os
from src.senkalib.senka_setting import SenkaSetting
from unittest.mock import *
from decimal import *

class TestKavaTransactionGenerator(unittest.TestCase):
  def test_get_transactions(self):
    settings = SenkaSetting({})

    with patch.object(KavaTransactionGenerator, 'get_txs', new=TestKavaTransactionGenerator.mock_get_txs):
      transactions = KavaTransactionGenerator.get_transactions(settings, 'kava1af7lm2qv9zp526gjd3cdxrpr9zeangjlyhjqjx')
      timestamp = transactions[0].get_timestamp()
      fee = transactions[0].get_transaction_fee()
      self.assertEqual(len(transactions), 31)
      self.assertEqual(timestamp, '2022-04-01 09:20:35')
      self.assertEqual(fee, Decimal(1000))

      transactions = KavaTransactionGenerator.get_transactions(settings, 'kava1af7lm2qv9zp526gjd3cdxrpr9zeangjlyhjqjx', endblock=4271593)
      self.assertEqual(len(transactions), 14)

  @classmethod
  def mock_get_txs(cls, settings:dict, address:str, arg_startblock:int = None, arg_endblock:int = None, arg_page:int = None):
    print('mock')
    transactions = json.loads(Path('%s/../../testdata/chain/kava/test_transactions.json' % os.path.dirname(__file__)).read_text())
    return transactions

if __name__ == '__main__':
  unittest.main()
