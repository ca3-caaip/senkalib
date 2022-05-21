import csv
from enum import Enum, auto

from senkalib.chain.bitbank.bitbank_transaction import BitbankTransaction
from senkalib.chain.transaction_generator import TransactionGenerator
from senkalib.senka_setting import SenkaSetting


class DataType(Enum):
    exchange = auto()
    unknown = auto()


class BitbankTransactionGenerator(TransactionGenerator):
    chain = "bitbank"

    @classmethod
    def get_transaction_from_csv(
        cls, settings: SenkaSetting, data: str
    ) -> list[BitbankTransaction]:
        if BitbankTransactionGenerator._validate(data) == DataType.exchange:
            reader = csv.DictReader(data.splitlines())
            dict_data = [row for row in reader]
            data_with_type = list(map(cls._set_data_type, dict_data))
            return list(map(BitbankTransaction, data_with_type))

        else:
            raise ValueError("Invalid data")

    @staticmethod
    def _set_data_type(data: dict) -> dict:
        data["data_type"] = "bitbank_exchange"
        return data

    @staticmethod
    def _validate(data: str) -> DataType:
        header = csv.reader(data.splitlines()).__next__()
        if set(header) == set(
            ["注文ID", "取引ID", "通貨ペア", "タイプ", "売/買", "数量", "価格", "手数料", "M/T", "取引日時"]
        ):
            return DataType.exchange
        else:
            return DataType.unknown
