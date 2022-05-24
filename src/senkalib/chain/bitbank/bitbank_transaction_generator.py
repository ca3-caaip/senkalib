import csv
from enum import Enum, auto

from senkalib.chain.bitbank.bitbank_transaction import BitbankTransaction
from senkalib.chain.transaction_generator import TransactionGenerator


class DataType(Enum):
    exchange = auto()
    unknown = auto()


class BitbankTransactionGenerator(TransactionGenerator):
    chain = "bitbank"

    @classmethod
    def get_transactions(cls, transaction_params: dict) -> list[BitbankTransaction]:
        if transaction_params["type"] != "csv":
            raise ValueError("type must be str")
        data = transaction_params["data"]
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
        if set(header) == {
            "注文ID",
            "取引ID",
            "通貨ペア",
            "タイプ",
            "売/買",
            "数量",
            "価格",
            "手数料",
            "M/T",
            "取引日時",
        }:
            return DataType.exchange
        else:
            return DataType.unknown
