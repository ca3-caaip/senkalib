import unittest
from decimal import Decimal

from senkalib.caaj_journal import CaajJournal


class TestCaajJounal(unittest.TestCase):
    def test_init(self):
        executed_at = "2022-01-12 11:11:11"
        platform = "platform"
        application = "application"
        service = "service"
        transaction_id = (
            "0x36512c7e09e3570dfc53176252678ee9617660550d36f4da797afba6fc55bba6"
        )
        trade_uuid = "bbbbbbddddddd"
        type = "deposit"
        amount = Decimal("0.005147")
        uti = "juno/osmosis"
        caaj_from = "0x111111111111111111111"
        caaj_to = "0x222222222222222222222"
        comment = "hello world"

        cj = CaajJournal(
            executed_at,
            platform,
            application,
            service,
            transaction_id,
            trade_uuid,
            type,
            amount,
            uti,
            caaj_from,
            caaj_to,
            comment,
        )
        assert cj.executed_at == "2022-01-12 11:11:11"
        assert cj.platform == "platform"
        assert cj.application == "application"
        assert cj.service == "service"
        assert (
            cj.transaction_id
            == "0x36512c7e09e3570dfc53176252678ee9617660550d36f4da797afba6fc55bba6"
        )
        assert cj.trade_uuid == "bbbbbbddddddd"
        assert cj.type == "deposit"
        assert cj.amount == Decimal("0.005147")
        assert cj.uti == "juno/osmosis"
        assert cj.caaj_from == "0x111111111111111111111"
        assert cj.caaj_to == "0x222222222222222222222"
        assert cj.comment == "hello world"


if __name__ == "__main__":
    unittest.main()
