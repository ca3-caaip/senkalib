import json
import os
from decimal import Decimal
from pathlib import Path

from senkalib.chain.bitbank.bitbank_transaction import BitbankTransaction


class TestBitbankTransaction(object):
    def test_get_timestamp(self):
        transaction = self._get_test_transaction()
        assert transaction.get_timestamp() == "2022/03/14 20:55:24"

    def test_get_amount(self):
        transaction = self._get_test_transaction()
        assert transaction.get_amount() == Decimal("537.8006")

    def test_get_price(self):
        transaction = self._get_test_transaction()
        assert transaction.get_price() == Decimal("110.779")

    def test_get_transaction_fee(self):
        transaction = self._get_test_transaction()
        assert transaction.get_transaction_fee() == Decimal("71.4924")

    def test_token_pair(self):
        transaction = self._get_test_transaction()
        assert transaction.get_token_pair() == "mona_jpy"

    def test_get_side(self):
        transaction = self._get_test_transaction()
        assert transaction.get_side() == "buy"

    @staticmethod
    def _get_test_transaction() -> BitbankTransaction:
        data_json = json.loads(
            Path(
                "%s/../../testdata/chain/bitbank/bitbank_exchange.json"
                % os.path.dirname(__file__)
            ).read_text()
        )
        transaction = BitbankTransaction(data_json[0])
        return transaction
