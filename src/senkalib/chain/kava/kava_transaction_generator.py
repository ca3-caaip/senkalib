from senkalib.chain.transaction import Transaction
from senkalib.chain.transaction_generator import TransactionGenerator
from senkalib.senka_setting import SenkaSetting
from senkalib.chain.kava.kava_transaction import KavaTransaction
from typing import List
import requests

class KavaTransactionGenerator(TransactionGenerator):
  chain = 'kava'

  @classmethod
  def get_transactions(cls, settings:SenkaSetting, address:str, startblock:int = None, endblock:int = None, starttime:int = None, endtime:int = None) -> List[Transaction]:
    osmosis_transactions = []
    num_transactions = 50
    startblock = startblock if startblock is not None else 0
    endblock = endblock if endblock is not None else None

    while num_transactions >= 50:
      transactions = KavaTransactionGenerator.get_txs(address, startblock)
      num_transactions = len(transactions)
      for transaction in transactions:
        startblock = transaction['header']['id']
        if endblock is not None and startblock <= endblock:
          return osmosis_transactions
        osmosis_transactions.append(KavaTransaction(transaction))


    return osmosis_transactions

  @classmethod
  def get_txs(cls, address, startblock):
    response = requests.get(
        'https://api-kava.cosmostation.io/v1/account/new_txs/%s' % address,
        params={'from': startblock, 'limit': 50})
    transactions = response.json()
    return transactions
