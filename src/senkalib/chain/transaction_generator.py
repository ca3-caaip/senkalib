from abc import ABCMeta, abstractmethod
from typing import List, Union

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
        startblock: Union[int, None] = None,
        endblock: Union[int, None] = None,
        starttime: Union[int, None] = None,
        endtime: Union[int, None] = None,
    ) -> List[Transaction]:
        pass

    @classmethod
    @abstractmethod
    def get_transactions_from_data(
        cls,
        settings: SenkaSetting,
        data: dict,
    ) -> List[Transaction]:
        pass
