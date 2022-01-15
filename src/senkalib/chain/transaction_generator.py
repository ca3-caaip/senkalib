from abc import ABCMeta, abstractmethod
from src.senkalib.chain.transaction import Transaction 
from src.senkalib.senka_setting import SenkaSetting
from typing import List

class TransactionGenerator(metaclass=ABCMeta):
  chain = None

  @classmethod
  @abstractmethod
  def get_transactions(cls, settings:SenkaSetting, address:str, timerange:dict = None, blockrange:dict = None) -> List[Transaction]:
    pass