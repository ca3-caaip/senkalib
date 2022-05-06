import json
import os
from decimal import Decimal
from pathlib import Path
from unittest.mock import ANY, call, patch

from src.senkalib.senka_setting import SenkaSetting


class TestOsmosisTransactionGenerator:
    @patch(
        "senkalib.chain.cosmostation_api_client.CosmostationApiClient.get_transactions_by_address"
    )
    def test_get_transactions(self, get_transactions_by_address):
        from src.senkalib.chain.osmosis.osmosis_transaction_generator import (
            OsmosisTransactionGenerator,
        )

        get_transactions_by_address.return_value = []
        OsmosisTransactionGenerator.get_transactions(
            SenkaSetting({}),
            address="address",
            starttime=1,
            endtime=2,
            startblock=3,
            endblock=4,
        )
        assert get_transactions_by_address.mock_calls == [
            call(
                chain="osmosis",
                address="address",
                starttime=1,
                endtime=2,
                startblock=3,
                endblock=4,
                cache=ANY,
            )
        ]

    @patch("senkalib.chain.cosmostation_api_client.CosmostationApiClient.get_txs")
    def test_get_transactions_all(self, get_txs):
        from src.senkalib.chain.osmosis.osmosis_transaction_generator import (
            OsmosisTransactionGenerator,
        )

        settings = SenkaSetting(dict())
        get_txs.return_value = TestOsmosisTransactionGenerator.mock_get_txs()
        transactions = OsmosisTransactionGenerator.get_transactions(
            settings, "osmo1xq5du8upw2fmyx7h43w8uqv47vln70hre92wvm"
        )
        assert len(transactions) == 44
        transaction = transactions[0]
        assert transaction.get_timestamp() == "2022-01-13 12:46:46"
        assert transaction.get_transaction_fee() == Decimal("0")
        transaction = transactions[43]
        assert transaction.get_timestamp() == "2022-01-15 12:18:55"
        assert transaction.get_transaction_fee() == Decimal("33")

    @classmethod
    def mock_get_txs(cls):
        transactions = json.loads(
            Path(
                "%s/../../testdata/chain/osmosis/test_transactions.json"
                % os.path.dirname(__file__)
            ).read_text()
        )
        return transactions
