import unittest
from unittest.mock import *
from senkalib.chain.kava.kava_transaction import KavaTransaction
import json
from pathlib import Path
import os
from decimal import *

class TestKavaTransaction(unittest.TestCase):
  def test_get_timestamp(self):
    swap_transaction = json.loads(Path('%s/../../testdata/chain/kava/create_atomic_swap.json' % os.path.dirname(__file__)).read_text())
    transaction = KavaTransaction(swap_transaction)
    timestamp = transaction.get_timestamp()
    self.assertEqual(timestamp, '2022-01-27 02:23:59')

  def test_get_transaction_fee(self):
    swap_transaction = json.loads(Path('%s/../../testdata/chain/kava/create_atomic_swap.json' % os.path.dirname(__file__)).read_text())
    transaction = KavaTransaction(swap_transaction)
    fee = transaction.get_transaction_fee()
    self.assertEqual(fee, Decimal('1000'))
  
  def test_get_legacy_transaction_fee(self):
    swap_transaction = json.loads(Path('%s/../../testdata/chain/kava/delegate_v8(legacy).json' % os.path.dirname(__file__)).read_text())
    transaction = KavaTransaction(swap_transaction)
    fee = transaction.get_transaction_fee()
    self.assertEqual(fee, Decimal('100'))

  def test_get_transaction_mepty_fee_list(self):
    swap_transaction = json.loads(Path('%s/../../testdata/chain/kava/empty_fee_list.json' % os.path.dirname(__file__)).read_text())
    transaction = KavaTransaction(swap_transaction)
    fee = transaction.get_transaction_fee()
    self.assertEqual(fee, Decimal('0'))


if __name__ == '__main__':
  unittest.main()