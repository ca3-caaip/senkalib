from senkalib.chain.transaction import Transaction


class BitbankTransaction(Transaction):
    chain = "bitbank"

    def __init__(self, transaction: dict):
        super().__init__(transaction["取引ID"])
        self.transaction = transaction

    def get_timestamp(self) -> str:
        return self.transaction["取引日時"]

    def get_amount(self) -> float:
        return self.transaction["数量"]

    def get_price(self) -> float:
        return self.transaction["価格"]

    def get_fee(self) -> float:
        return self.transaction["手数料"]

    def get_pair(self) -> str:
        return self.transaction["通貨ペア"]

    def get_type(self) -> str:
        return self.transaction["data_type"]

    def get_trade_type(self) -> str:
        return self.transaction["売/買"]
