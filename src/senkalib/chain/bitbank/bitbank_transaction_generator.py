import csv

from senkalib.chain.bitbank.bitbank_transaction import BitbankTransaction
from senkalib.chain.transaction_generator import TransactionGenerator
from senkalib.senka_setting import SenkaSetting


class BitbankTransactionGenerator(TransactionGenerator):
    chain = "bitbank"

    @classmethod
    def get_transaction_from_csv(
        cls, settings: SenkaSetting, data: str
    ) -> list[BitbankTransaction]:
        reader = csv.DictReader(data.splitlines())
        dict_data = [row for row in reader]
        data_with_type = list(map(cls.set_data_type, dict_data))
        return list(map(BitbankTransaction, data_with_type))

    @staticmethod
    def set_data_type(data: dict) -> dict:
        data["data_type"] = "bitbank_exchange"
        return data

    @staticmethod
    def validate_exchange(data: dict) -> bool:
        return True
