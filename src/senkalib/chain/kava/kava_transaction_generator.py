from senkalib.chain.transaction import Transaction
from senkalib.chain.transaction_generator import TransactionGenerator, GetOptions
from senkalib.senka_setting import SenkaSetting
from senkalib.chain.kava.kava_transaction import KavaTransaction
from typing import List
import requests

class KavaTransactionGenerator(TransactionGenerator):
  chain = 'kava'

  @classmethod
  def get_transactions(cls, settings:SenkaSetting, address:str, options:GetOptions = None) -> List[Transaction]:
    osmosis_transactions = []
    num_transactions = 50
    startblock = int(options['startblock']) if options is not None and 'startblock' in options and type(options['startblock']) is int else 0
    endblock = int(options['endblock']) if options is not None and 'endblock' in options and type(options['endblock']) is int else None

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
