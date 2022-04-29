from decimal import Decimal
import json
import os
from pathlib import Path
from unittest.mock import patch, call, ANY
from src.senkalib.senka_setting import SenkaSetting


class TestKavaTransactionGenerator:
    @patch(
        "senkalib.chain.cosmostation_api_client.CosmostationApiClient.get_transactions_by_address"
    )
    def test_get_transactions(self, get_transactions_by_address):
        from src.senkalib.chain.kava.kava_transaction_generator import (
            KavaTransactionGenerator,
        )

        get_transactions_by_address.return_value = []
        KavaTransactionGenerator.get_transactions(
            SenkaSetting({}),
            address="address",
            starttime=1,
            endtime=2,
            startblock=3,
            endblock=4,
        )
        assert get_transactions_by_address.mock_calls == [
            call(
                chain="kava",
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
        from src.senkalib.chain.kava.kava_transaction_generator import (
            KavaTransactionGenerator,
        )

        settings = SenkaSetting({})
        get_txs.return_value = TestKavaTransactionGenerator.mock_get_txs()
        transactions = KavaTransactionGenerator.get_transactions(
            settings, "kava1af7lm2qv9zp526gjd3cdxrpr9zeangjlyhjqjx"
        )
        assert len(transactions) == 31

        transaction = transactions[0]
        assert transaction.get_timestamp() == "2021-09-18 13:50:16"
        transaction = transactions[30]
        assert transaction.get_timestamp() == "2022-04-01 09:20:35"
        assert transaction.get_transaction_fee() == Decimal(1000)

    @classmethod
    def mock_get_txs(cls):
        print("mock")
        transactions = json.loads(
            Path(
                "%s/../../testdata/chain/kava/test_transactions.json"
                % os.path.dirname(__file__)
            ).read_text()
        )
        return transactions
