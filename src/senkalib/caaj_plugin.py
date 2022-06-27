from abc import ABCMeta, abstractmethod
from typing import List

from senkalib.caaj_journal import CaajJournal
from senkalib.platform.transaction import Transaction
from senkalib.token_original_id_table import TokenOriginalIdTable


class CaajPlugin(metaclass=ABCMeta):
    platform = None

    @abstractmethod
    def can_handle(cls, transaction: Transaction) -> bool:
        pass

    @abstractmethod
    def get_caajs(
        cls,
        address: str,
        transaction: Transaction,
        token_original_id_table: TokenOriginalIdTable,
    ) -> List[CaajJournal]:
        pass
