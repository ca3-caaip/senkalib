import os
from pathlib import Path

from senkalib.chain.bitbank.bitbank_transaction import BitbankTransaction
from senkalib.chain.bitbank.bitbank_transaction_generator import (
    BitbankTransactionGenerator,
)


class TestBitbankTransactionGenerator:
    def test_generate_transaction_id(self):
        transaction = self._get_transaction_from_csv()
        assert transaction[0].get_transaction_id() == "1215140489"

    def test_generate_transaction_data_type(self):
        transaction = self._get_transaction_from_csv()
        assert transaction[0].get_transaction_data_type() == "bitbank_exchange"

    @staticmethod
    def _get_transaction_from_csv() -> list[BitbankTransaction]:
        csvtext = Path(
            "%s/../../testdata/chain/bitbank/bitbank_exchange.csv"
            % os.path.dirname(__file__)
        ).read_text()
        transaction_params = {"data": csvtext, "type": "csv"}
        return BitbankTransactionGenerator.get_transactions(transaction_params)
