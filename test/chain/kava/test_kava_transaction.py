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
    delegate_legacy_transaction = json.loads(Path('%s/../../testdata/chain/kava/delegate_v8(legacy).json' % os.path.dirname(__file__)).read_text())
    transaction = KavaTransaction(delegate_legacy_transaction)
    fee = transaction.get_transaction_fee()
    self.assertEqual(fee, Decimal('100'))

  def test_get_transaction_mepty_fee_list(self):
    empty_fee_list_transaction = json.loads(Path('%s/../../testdata/chain/kava/empty_fee_list.json' % os.path.dirname(__file__)).read_text())
    transaction = KavaTransaction(empty_fee_list_transaction)
    fee = transaction.get_transaction_fee()
    self.assertEqual(fee, Decimal('0'))
  
  def test_get_fail(self):
    swap_transaction = json.loads(Path('%s/../../testdata/chain/kava/create_atomic_swap.json' % os.path.dirname(__file__)).read_text())
    transaction = KavaTransaction(swap_transaction)
    failed = transaction.get_fail()
    self.assertEqual(failed, False)

    failed_transaction = json.loads(Path('%s/../../testdata/chain/kava/fail_v8.json' % os.path.dirname(__file__)).read_text())
    transaction = KavaTransaction(failed_transaction)
    failed = transaction.get_fail()
    self.assertEqual(failed, True)

  def test_get_chain_version(self):
    swap_transaction = json.loads(Path('%s/../../testdata/chain/kava/create_atomic_swap.json' % os.path.dirname(__file__)).read_text())
    transaction = KavaTransaction(swap_transaction)
    chain_version = transaction.get_chain_version()
    self.assertEqual(chain_version, 9)

    legacy_transaction = json.loads(Path('%s/../../testdata/chain/kava/delegate_v8(legacy).json' % os.path.dirname(__file__)).read_text())
    transaction = KavaTransaction(legacy_transaction)
    chain_version = transaction.get_chain_version()
    self.assertEqual(chain_version, 8)

if __name__ == '__main__':
  unittest.main()