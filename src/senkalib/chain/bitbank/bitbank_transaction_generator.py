from senkalib.chain.bitbank.bitbank_transaction import BitbankTransaction
from senkalib.chain.transaction_generator import TransactionGenerator
from senkalib.senka_setting import SenkaSetting


class BitbankTransactionGenerator(TransactionGenerator):
    chain = "bitbank"

    @classmethod
    def get_transaction_from_data(
        cls, data: list, settings: SenkaSetting
    ) -> list[BitbankTransaction]:
        data_with_type = list(map(cls.set_data_type, data))
        return list(map(BitbankTransaction, data_with_type))

    @staticmethod
    def set_data_type(data: dict) -> dict:
        data["data_type"] = "bitbank"
        return data
