import unittest
from unittest.mock import *
from src.senkalib.caaj_plugin import CaajPlugin
from src.senkalib.chain.transaction import Transaction
from src.senkalib.caaj_journal import CaajJournal
import json
from pathlib import Path
import os

class SampleCaajPlugin(CaajPlugin):
  @classmethod
  def can_handle(cls, transaction:Transaction):
    return True

  @classmethod
  def get_caajs(cls, transaction:Transaction) -> CaajJournal:
    jounal = CaajJournal({})
    return jounal


class TestCaajPlugin(unittest.TestCase):
  def test_get_handle(self):
    result = SampleCaajPlugin.can_handle('XXXXXXXXXXXXXXXXXXXXXXX')
    self.assertTrue(result)    



if __name__ == '__main__':
  unittest.main()