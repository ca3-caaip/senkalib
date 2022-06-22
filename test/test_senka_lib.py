import os
import unittest
from unittest.mock import patch

from senkalib.platform.bsc.bsc_transaction_generator import BscTransactionGenerator
from senkalib.platform.osmosis.osmosis_transaction_generator import (
    OsmosisTransactionGenerator,
)
from senkalib.senka_lib import SenkaLib


class TestSenkaLib(unittest.TestCase):
    def test_get_available_platform(self):
        with patch.object(os, "listdir", new=TestSenkaLib.mock_listdir):
            platforms = SenkaLib.get_available_platform()

            self.assertEqual(platforms[0], BscTransactionGenerator)
            self.assertEqual(platforms[1], OsmosisTransactionGenerator)

    @classmethod
    def mock_listdir(cls, transaction_hash):
        return ["osmosis", "bsc"]


if __name__ == "__main__":
    unittest.main()
