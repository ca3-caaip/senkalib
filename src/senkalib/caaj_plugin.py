from abc import ABCMeta, abstractmethod
from src.senkalib.caaj_journal import CaajJournal
from src.senkalib.transaction.transaction import Transaction

class CaajPlugin(metaclass=ABCMeta):
  chain = None

  @abstractmethod
  def can_handle(cls, transaction:Transaction) -> bool:
    pass

  @abstractmethod
  def get_caajs(cls, transaction:Transaction) -> CaajJournal:
    pass