from abc import ABCMeta, abstractmethod
from senkalib.chain.transaction import Transaction 
from senkalib.senka_setting import SenkaSetting
from typing import List, TypedDict

class GetOptions(TypedDict, total=False):
  startblock: int
  endblock: int
  starttime: int
  endtime: int

class TransactionGenerator(metaclass=ABCMeta):
  chain = None

  @classmethod
  @abstractmethod
  def get_transactions(cls, settings:SenkaSetting, address:str, options:GetOptions = None) -> List[Transaction]:
    pass
