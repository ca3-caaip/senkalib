import dataclasses
from decimal import Decimal
from typing import List


@dataclasses.dataclass
class CaajJournal:
    executed_at: str
    chain: str
    platform: str
    application: str
    transaction_id: str
    trade_uuid: str
    type: str
    amount: Decimal
    token_symbol: str
    token_original_id: str
    token_symbol_uuid: str
    caaj_from: str
    caaj_to: str
    comment: str
