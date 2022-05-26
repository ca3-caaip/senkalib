import csv
from enum import Enum, auto

from senkalib.chain.bitbank.bitbank_transaction import (
    BitbankTransaction,
    TransactionKey,
)
from senkalib.chain.transaction_generator import TransactionGenerator


class DataType(Enum):
    exchange = auto()
    unknown = auto()


class BitbankTransactionGenerator(TransactionGenerator):
    chain = "bitbank"

    @classmethod
    def get_transactions(cls, transaction_params: dict) -> list[BitbankTransaction]:
        if transaction_params["type"] != "csv":
            raise ValueError("type must be csv")
        data = transaction_params["data"]
        if BitbankTransactionGenerator._validate(data) == DataType.exchange:
            reader = csv.DictReader(data.splitlines())
            dict_data = [row for row in reader]
            return list(map(BitbankTransaction, dict_data))
        else:
            raise ValueError("Invalid data")

    @staticmethod
    def _validate(data: str) -> DataType:
        header = csv.reader(data.splitlines()).__next__()
        if set(header) == {
            TransactionKey.order_id.value,
            TransactionKey.transaction_id.value,
            TransactionKey.pair.value,
            TransactionKey.type.value,
            TransactionKey.side.value,
            TransactionKey.amount.value,
            TransactionKey.price.value,
            TransactionKey.fee.value,
            TransactionKey.m_t.value,
            TransactionKey.timestamp.value,
        }:
            return DataType.exchange
        else:
            return DataType.unknown
