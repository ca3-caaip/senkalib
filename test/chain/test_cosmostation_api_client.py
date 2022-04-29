import json
import os
from itertools import repeat
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

from src.senkalib.chain.cosmostation_api_client import (
    CosmostationApiClient,
    get_cosmostation_api_host,
    get_nearest_id,
    osmosis_tx_history_records,
    to_timestamp,
)


class TestCosmostationApiClient:
    @patch.object(CosmostationApiClient, "get_txs")
    def test_get_transactions_by_address(self, get_txs):
        dummy_txs = json.loads(
            Path(
                "%s/../testdata/chain/osmosis/test_transactions.json"
                % os.path.dirname(__file__)
            ).read_text()
        )
        # check results should be expected data
        get_txs.return_value = dummy_txs
        txs = CosmostationApiClient.get_transactions_by_address("osmosis", "address")
        assert len(txs) == 44
        # filter results by parameters
        assert (
            len(
                CosmostationApiClient.get_transactions_by_address("osmosis", "address", startblock=2781756)
            )
            == 43
        )
        assert (
            len(
                CosmostationApiClient.get_transactions_by_address("osmosis", "address", endblock=2781756)
            )
            == 4
        )
        assert (
            len(
                CosmostationApiClient.get_transactions_by_address("osmosis", "address",
                                                                  starttime=to_timestamp("2022-01-15T12:18:54Z"))
            )
            == 2
        )
        assert (
            len(
                CosmostationApiClient.get_transactions_by_address("osmosis", "address",
                                                                  endtime=to_timestamp("2022-01-15T12:18:54Z"))
            )
            == 42
        )
        # get_txs should be called multiply if result length gte 50
        get_txs.reset_mock()
        tx = dummy_txs[0]
        get_txs.side_effect = [list(repeat(tx, 50)), list(repeat(tx, 49))]
        txs = CosmostationApiClient.get_transactions_by_address("osmosis", "address")
        assert len(txs) == 99
        assert get_txs.call_count == 2


class TestCosmostationApiClientInternals(TestCase):
    def test_get_nearest_id(self):
        cache = osmosis_tx_history_records
        newest = cache[-1]
        second = cache[-2]
        assert get_nearest_id(to_timestamp("2030-01-01T00:00:00Z"), cache=cache) == 0
        assert get_nearest_id(newest.timestamp + 1, cache=cache) == 0
        assert get_nearest_id(newest.timestamp + 0, cache=cache) == 0
        assert get_nearest_id(newest.timestamp - 1, cache=cache) == newest.id
        assert get_nearest_id(second.timestamp + 1, cache=cache) == newest.id
        assert get_nearest_id(second.timestamp + 0, cache=cache) == newest.id
        assert get_nearest_id(second.timestamp - 1, cache=cache) == second.id

    def test_to_timestamp(self):
        assert to_timestamp("2022-01-01T08:59:59Z") == 1641027599

    def test_get_cosmostation_api_host(self):
        assert get_cosmostation_api_host("atom") == "api.cosmostation.io"
        assert get_cosmostation_api_host("osmosis") == "api-osmosis.cosmostation.io"
        with self.assertRaisesRegex(
            ValueError,
            "invalid chain is not implemented. check following supported chains: .+",
        ):
            get_cosmostation_api_host("invalid chain")
