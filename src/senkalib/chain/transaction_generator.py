from abc import ABCMeta, abstractmethod
from typing import List

from senkalib.chain.transaction import Transaction


class TransactionGenerator(metaclass=ABCMeta):
    chain = None

    @classmethod
    @abstractmethod
    def get_transactions(cls, transaction_params: dict) -> List[Transaction]:
        pass
