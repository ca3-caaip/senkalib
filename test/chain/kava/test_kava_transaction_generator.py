from unittest.mock import patch, call, ANY
from src.senkalib.senka_setting import SenkaSetting


class TestKavaTransactionGenerator:
  @patch('senkalib.chain.cosmostation_api_client.CosmostationApiClient')
  def test_get_transactions(self, client):
    from src.senkalib.chain.kava.kava_transaction_generator import KavaTransactionGenerator
    client.get_transactions_by_address.return_value = []
    KavaTransactionGenerator.get_transactions(SenkaSetting({}), address='address', starttime=1, endtime=2, startblock=3, endblock=4)
    assert client.get_transactions_by_address.mock_calls == [call(chain='kava', address='address', starttime=1, endtime=2, startblock=3, endblock=4, cache=ANY)]
