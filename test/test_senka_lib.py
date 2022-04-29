import os
import re
import unittest
from decimal import Decimal
from unittest.mock import *

from senkalib.caaj_journal import CaajJournal
from senkalib.chain.bsc.bsc_transaction_generator import BscTransactionGenerator
from senkalib.chain.osmosis.osmosis_transaction_generator import (
    OsmosisTransactionGenerator,
)
from senkalib.senka_lib import SenkaLib


class TestSenkaLib(unittest.TestCase):
    def test_get_available_chain(self):
        with patch.object(os, "listdir", new=TestSenkaLib.mock_listdir):
            chains = SenkaLib.get_available_chain()

            self.assertEqual(chains[0], BscTransactionGenerator)
            self.assertEqual(chains[1], OsmosisTransactionGenerator)

    @classmethod
    def mock_listdir(cls, transaction_hash):
        return ["osmosis", "bsc"]


if __name__ == "__main__":
    unittest.main()
