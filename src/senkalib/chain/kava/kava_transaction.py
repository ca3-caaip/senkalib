from datetime import datetime as dt
from decimal import Decimal, getcontext

from senkalib.chain.transaction import Transaction

getcontext().prec = 50


class KavaTransaction(Transaction):
    chain = "kava"

    def __init__(self, transaction:dict):
      super().__init__(transaction["data"]["txhash"])
      self.transaction = transaction
      self.chain_id = transaction['header']['chain_id']
      self.chain_version = int(self.chain_id.split('-')[1])
      self.fail = False
      if 'code' in transaction['data'] and transaction['data']['code'] != 0:
        self.fail = True


    def get_timestamp(self) -> str:
        return str(
            dt.strptime(
                self.transaction["header"]["timestamp"], "%Y-%m-%dT%H:%M:%SZ"
            ).replace(tzinfo=None)
        )

    def get_transaction_fee(self) -> Decimal:
      if self.chain_version <= 8:
        fee_list = self.transaction['data']['tx']['value']['fee']['amount']
      else:
        fee_list = self.transaction['data']['tx']['auth_info']['fee']['amount']
      return Decimal('0') if len(fee_list) == 0 else Decimal(fee_list[0]['amount'])

    def get_transaction(self) -> dict:
      return self.transaction

    def get_fail(self):
      return self.fail

    def get_chain_version(self):
      return self.chain_version
