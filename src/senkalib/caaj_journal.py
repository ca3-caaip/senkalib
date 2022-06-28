import dataclasses
from decimal import Decimal


@dataclasses.dataclass
class CaajJournal:
    executed_at: str
    platform: str
    application: str
    service: str
    transaction_id: str
    trade_uuid: str
    type: str
    amount: Decimal
    uti: str
    caaj_from: str
    caaj_to: str
    comment: str
