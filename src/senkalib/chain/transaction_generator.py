from abc import ABCMeta, abstractmethod
from typing import List

from senkalib.chain.transaction import Transaction
from senkalib.senka_setting import SenkaSetting


class TransactionGenerator(metaclass=ABCMeta):
    chain = None

    @classmethod
    @abstractmethod
    def get_transactions(
        cls,
        settings: SenkaSetting,
        address: str,
        startblock: int = None,
        endblock: int = None,
        starttime: int = None,
        endtime: int = None,
    ) -> List[Transaction]:
        pass
