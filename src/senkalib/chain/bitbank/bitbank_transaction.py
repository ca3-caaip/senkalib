from decimal import Decimal

from senkalib.chain.transaction import Transaction


class BitbankTransaction(Transaction):
    chain = "bitbank"

    def __init__(self, transaction: dict):
        super().__init__(transaction["取引ID"])
        self.transaction = transaction

    def get_timestamp(self) -> str:
        return self.transaction["取引日時"]

    def get_amount(self) -> Decimal:
        return Decimal(self.transaction["数量"])

    def get_price(self) -> Decimal:
        return Decimal(self.transaction["価格"])

    def get_transaction_fee(self) -> Decimal:
        return Decimal(self.transaction["手数料"])

    def get_pair(self) -> str:
        return self.transaction["通貨ペア"]

    def get_transaction_data_type(self) -> str:
        return self.transaction["data_type"]

    def get_trade_type(self) -> str:
        return self.transaction["売/買"]
