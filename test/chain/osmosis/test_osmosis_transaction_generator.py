from unittest.mock import patch, call, ANY
from src.senkalib.senka_setting import SenkaSetting


class TestOsmosisTransactionGenerator:
  @patch('senkalib.chain.cosmostation_api_client.CosmostationApiClient')
  def test_get_transactions(self, client):
    from src.senkalib.chain.osmosis.osmosis_transaction_generator import OsmosisTransactionGenerator
    client.get_transactions_by_address.return_value = []
    OsmosisTransactionGenerator.get_transactions(SenkaSetting({}), address='address', starttime=1, endtime=2, startblock=3, endblock=4)
    assert client.get_transactions_by_address.mock_calls == [call(chain='osmosis', address='address', starttime=1, endtime=2, startblock=3, endblock=4, cache=ANY)]
