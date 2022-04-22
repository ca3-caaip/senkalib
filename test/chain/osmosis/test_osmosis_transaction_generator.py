import unittest
from src.senkalib.chain.osmosis.osmosis_transaction_generator import OsmosisTransactionGenerator, get_nearest_id, to_timestamp, records
import json
from pathlib import Path
import os
from src.senkalib.senka_setting import SenkaSetting
from unittest.mock import *
from decimal import *
from itertools import repeat

class TestOsmosisTransactionGenerator(unittest.TestCase):
  @patch.object(OsmosisTransactionGenerator, 'get_txs')
  def test_get_transactions(self, get_txs):
    dummy_txs = json.loads(Path('%s/../../testdata/chain/osmosis/test_transactions.json' % os.path.dirname(__file__)).read_text())
    settings = SenkaSetting({})
    # check results should be expected data
    get_txs.return_value = dummy_txs
    txs = OsmosisTransactionGenerator.get_transactions(settings, 'address', None, {})
    tx = txs[0]
    assert len(txs) == 44
    assert tx.get_timestamp() == '2022-01-15 12:18:55'
    assert tx.get_transaction_fee() == Decimal(33)
    # filter results by parameters
    assert len(OsmosisTransactionGenerator.get_transactions(settings, 'address', None, {'startblock': 2781756})) == 43
    assert len(OsmosisTransactionGenerator.get_transactions(settings, 'address', None, {'endblock': 2781756})) == 4
    assert len(OsmosisTransactionGenerator.get_transactions(settings, 'address', {'starttime': to_timestamp('2022-01-15T12:18:54Z')})) == 2
    assert len(OsmosisTransactionGenerator.get_transactions(settings, 'address', {'endtime': to_timestamp('2022-01-15T12:18:54Z')})) == 42
    # get_txs should be called multiply if result length gte 50
    get_txs.reset_mock()
    tx = dummy_txs[0]
    get_txs.side_effect = [list(repeat(tx, 50)), list(repeat(tx, 49))]
    txs = OsmosisTransactionGenerator.get_transactions(settings, 'address', None, {})
    assert len(txs) == 99
    assert get_txs.call_count == 2

class TestOsmosisTransactionGeneratorInternals:
  def test_get_nearest_id(self):
    newest = records[-1]
    second = records[-2]
    assert get_nearest_id(to_timestamp('2030-01-01T00:00:00Z')) == 0
    assert get_nearest_id(newest.timestamp + 1) == 0
    assert get_nearest_id(newest.timestamp + 0) == 0
    assert get_nearest_id(newest.timestamp - 1) == newest.id
    assert get_nearest_id(second.timestamp + 1) == newest.id
    assert get_nearest_id(second.timestamp + 0) == newest.id
    assert get_nearest_id(second.timestamp - 1) == second.id

  def test_to_timestamp(self):
    assert to_timestamp('2022-01-01T08:59:59Z') == 1641027599

if __name__ == '__main__':
  unittest.main()
