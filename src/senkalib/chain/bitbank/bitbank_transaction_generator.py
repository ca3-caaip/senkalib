import csv
from enum import Enum, auto

from senkalib.chain.bitbank.bitbank_transaction import BitbankTransaction
from senkalib.chain.transaction_generator import TransactionGenerator


class DataType(Enum):
    exchange = auto()
    unknown = auto()


class Exchange(Enum):
    order_id = "注文ID"
    transaction_id = "取引ID"
    pair = "通貨ペア"
    type = "タイプ"
    side = "売/買"
    amount = "数量"
    price = "価格"
    fee = "手数料"
    m_t = "M/T"
    timestamp = "取引日時"


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
            Exchange.order_id.value,
            Exchange.transaction_id.value,
            Exchange.pair.value,
            Exchange.type.value,
            Exchange.side.value,
            Exchange.amount.value,
            Exchange.price.value,
            Exchange.fee.value,
            Exchange.m_t.value,
            Exchange.timestamp.value,
        }:
            return DataType.exchange
        else:
            return DataType.unknown
