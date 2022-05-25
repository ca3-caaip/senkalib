from decimal import Decimal
from enum import Enum

from senkalib.chain.transaction import Transaction


class TransactionKey(Enum):
    order_id = "注文ID"
    transaction_id = "取引ID"
    pair = "通貨ペア"
    type = "タイプ"
    trade_type = "売/買"
    amount = "数量"
    price = "価格"
    fee = "手数料"
    m_t = "M/T"
    timestamp = "取引日時"


class BitbankTransaction(Transaction):
    chain = "bitbank"

    def __init__(self, transaction: dict):
        super().__init__(transaction[TransactionKey.transaction_id.value])
        self.transaction = transaction

    def get_timestamp(self) -> str:
        return self.transaction[TransactionKey.timestamp.value]

    def get_amount(self) -> Decimal:
        return Decimal(self.transaction[TransactionKey.amount.value])

    def get_price(self) -> Decimal:
        return Decimal(self.transaction[TransactionKey.price.value])

    def get_transaction_fee(self) -> Decimal:
        return Decimal(self.transaction[TransactionKey.fee.value])

    def get_token_pair(self) -> str:
        return self.transaction[TransactionKey.pair.value]

    def get_transaction_data_type(self) -> str:
        return self.transaction["data_type"]

    def get_trade_type(self) -> str:
        return self.transaction[TransactionKey.trade_type.value]
