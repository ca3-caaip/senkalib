from dataclasses import dataclass
from dateutil import parser
from senkalib.chain.transaction_generator import TransactionGenerator
from senkalib.senka_setting import SenkaSetting
from senkalib.chain.osmosis.osmosis_transaction import OsmosisTransaction
from math import inf
import requests

class OsmosisTransactionGenerator(TransactionGenerator):
  chain = 'osmosis'

  @classmethod
  def get_transactions(cls, settings:SenkaSetting, address:str, timerange:dict = None, blockrange:dict = None) -> list[OsmosisTransaction]:
    startblock = int(blockrange['startblock']) if blockrange is not None and 'startblock' in blockrange and type(blockrange['startblock']) is int else 0
    endblock = int(blockrange['endblock']) if blockrange is not None and 'endblock' in blockrange and type(blockrange['endblock']) is int else inf
    starttime = int(timerange['starttime']) if timerange is not None and 'starttime' in timerange and type(timerange['starttime']) is int else 0
    endtime = int(timerange['endtime']) if timerange is not None and 'endtime' in timerange and type(timerange['endtime']) is int else inf

    total_result = []
    id_cursor = get_nearest_id(endtime)

    while True:
      result = cls.get_txs(address, id_cursor)
      for tx in result:
        id_cursor = int(tx['header']['id'])
        block_id = int(tx['data']['height'])
        time = to_timestamp(tx['header']['timestamp'])

        if starttime <= time <= endtime and startblock <= block_id <= endblock:
          total_result.append(OsmosisTransaction(tx))

        if time < starttime or block_id < startblock:
          return total_result
        else:
          continue

      if len(result) < 50:
        return total_result

  @classmethod
  def get_txs(cls, address: str, id_from: int) -> list[dict]:
    return requests.get('https://api-osmosis.cosmostation.io/v1/account/new_txs/%s' % address, params={'from': id_from, 'limit': 50}).json()


@dataclass
class IdRecord:
  timestamp: int
  id: int

id_records: list[IdRecord] = [
  IdRecord(1641027605, 11843943),  # 2022-01-01T09:00:05Z
  IdRecord(1640995203, 11802509),  # 2022-01-01T00:00:03Z
  IdRecord(1624052574, 2),         # 2021-06-18T21:42:54Z
]

def get_nearest_id(time: int):
  for newer, older in zip(id_records, id_records[1:]):  # NOTE: replace zip with pairwise at python@3.10
    if older.timestamp <= time < newer.timestamp:
      return newer.id
  return 0

def to_timestamp(iso8601string: str) -> int:
  return int(parser.parse(iso8601string).timestamp())
