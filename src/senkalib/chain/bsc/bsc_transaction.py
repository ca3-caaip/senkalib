import datetime
from decimal import Decimal

from web3.types import TxReceipt

from senkalib.chain.transaction import Transaction


class BscTransaction(Transaction):
    chain = "bsc"

    def __init__(
        self,
        transaction_id: str,
        transaction_receipt: TxReceipt,
        timestamp: str,
        gasused: str,
        gasprice: str,
    ):
        super().__init__(transaction_id)
        self.transaction_receipt = transaction_receipt
        self.timestamp = timestamp
        self.gasused = Decimal(gasused)
        self.gasprice = Decimal(gasprice)

    def get_timestamp(self) -> str:
        return str(
            datetime.datetime.fromtimestamp(
                int(self.timestamp), datetime.timezone.utc
            ).replace(tzinfo=None)
        )

    def get_transaction_fee(self) -> Decimal:
        return self.gasused * self.gasprice

    def get_transaction_receipt(self) -> TxReceipt:
        return self.transaction_receipt
