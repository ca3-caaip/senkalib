import csv
import unittest
from unittest.mock import patch

import requests

from senkalib.token_original_id_table import TokenOriginalIdTable


class TestTokenOriginalIdTable(unittest.TestCase):
    def test_get_all_meta_data(self):
        with patch.object(requests, "get", new=TestTokenOriginalIdTable.mock_get):
            with patch.object(
                csv, "DictReader", new=TestTokenOriginalIdTable.mock_DictReader
            ):
                token_original_id_table = TokenOriginalIdTable("")
                metadata = token_original_id_table.get_all_meta_data(
                    "osmosis",
                    "ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2",
                )
                if metadata is None:
                    assert False
                assert metadata["uti"] == "atom/cosmos"
                assert metadata["description"] == "native token for cosmos"
                assert metadata["platform"] == "osmosis"
                assert (
                    metadata["original_id"]
                    == "ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2"
                )

    def test_get_uti_exist(self):
        with patch.object(requests, "get", new=TestTokenOriginalIdTable.mock_get):
            with patch.object(
                csv, "DictReader", new=TestTokenOriginalIdTable.mock_DictReader
            ):
                token_original_id_table = TokenOriginalIdTable("")
                uti = token_original_id_table.get_uti(
                    "osmosis",
                    "ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2",
                )
                assert uti == "atom/cosmos"

    def test_get_uti_nonexist(self):
        with patch.object(requests, "get", new=TestTokenOriginalIdTable.mock_get):
            with patch.object(
                csv, "DictReader", new=TestTokenOriginalIdTable.mock_DictReader
            ):
                token_original_id_table = TokenOriginalIdTable("")
                uti = token_original_id_table.get_uti(
                    "osmosis",
                    "gamm/pool/497",
                )
                assert uti == "gamm%2Fpool%2F497/osmosis"

    def test_get_symbol(self):
        with patch.object(requests, "get", new=TestTokenOriginalIdTable.mock_get):
            with patch.object(
                csv, "DictReader", new=TestTokenOriginalIdTable.mock_DictReader
            ):
                token_original_id_table = TokenOriginalIdTable("")
                symbol = token_original_id_table.get_symbol(
                    "osmosis",
                    "ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2",
                )
                assert symbol == "atom"

    def test_get_description(self):
        with patch.object(requests, "get", new=TestTokenOriginalIdTable.mock_get):
            with patch.object(
                csv, "DictReader", new=TestTokenOriginalIdTable.mock_DictReader
            ):
                token_original_id_table = TokenOriginalIdTable("")
                description = token_original_id_table.get_description(
                    "osmosis",
                    "ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2",
                )
                assert description == "native token for cosmos"

    def test_primary_is_empty(self):
        with patch.object(requests, "get", new=TestTokenOriginalIdTable.mock_get):
            with patch.object(
                csv,
                "DictReader",
                new=TestTokenOriginalIdTable.mock_DictReader,
            ):
                token_original_id_table = TokenOriginalIdTable("")
                symbol = token_original_id_table.get_symbol(
                    "wrong_platform",
                    "ibc/9712DBB13B9631EDFA9BF61B55F1B2D290B2ADB67E3A4EB3A875F3B6081B3B84",
                )
                assert symbol is None

    class TestContent:
        @classmethod
        def decode(cls):
            return ""

    @classmethod
    def mock_get(cls, url: str):
        cls.content = TestTokenOriginalIdTable.TestContent
        return cls

    @classmethod
    def mock_DictReader(cls, src):
        token_original_id_table = [
            {
                "uti": "atom/cosmos",
                "platform": "osmosis",
                "original_id": "ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2",
                "description": "native token for cosmos",
                "primary": "",
            },
            {
                "uti": "atom/cosmos",
                "platform": "bsc",
                "original_id": "0x0Eb3a705fc54725037CC9e008bDede697f62F335",
                "description": "native token for cosmos",
                "primary": "",
            },
            {
                "uti": "atom/cosmos",
                "platform": "cosmos",
                "original_id": "atom",
                "description": "native token for cosmos",
                "primary": "TRUE",
            },
            {
                "uti": "juno/juno",
                "platform": "osmosis",
                "original_id": "ibc/46B44899322F3CD854D2D46DEEF881958467CDD4B3B10086DA49296BBED94BED",
                "description": "native token for juno",
                "primary": "",
            },
            {
                "uti": "luna/terra",
                "platform": "osmosis",
                "original_id": "ibc/0EF15DF2F02480ADE0BB6E85D9EBB5DAEA2836D3860E9F97F9AADE4F57A31AA0",
                "description": "native token for terra",
                "primary": "",
            },
            {
                "uti": "ust/terra",
                "platform": "osmosis",
                "original_id": "ibc/BE1BB42D4BE3C30D50B68D7C41DB4DFCE9678E8EF8C539F6E6A9345048894FCC",
                "description": "doller peg token on terra",
                "primary": "",
            },
            {
                "uti": "osmo/osmosis",
                "platform": "osmosis",
                "original_id": "osmo",
                "description": "native token for osmosis",
                "primary": "TRUE",
            },
            {
                "uti": "umee/umee",
                "platform": "osmosis",
                "original_id": "ibc/67795E528DF67C5606FC20F824EA39A6EF55BA133F4DC79C90A8C47A0901E17C",
                "description": "Umee is a cross platform DeFi hub that interconnects between blockplatforms",
                "primary": "",
            },
            {
                "uti": "scrt/scrt",
                "platform": "osmosis",
                "original_id": "ibc/0954E1C28EB7AF5B72D24F3BC2B47BBB2FDF91BDDFD57B74B99E133AED40972A",
                "description": "Native token for secret network",
                "primary": "",
            },
            {
                "uti": "cro/cro",
                "platform": "osmosis",
                "original_id": "ibc/E6931F78057F7CC5DA0FD6CEF82FF39373A6E0452BF1FD76910B93292CF356C1",
                "description": "native token for crypto.org",
                "primary": "",
            },
            {
                "uti": "xprt/xprt",
                "platform": "osmosis",
                "original_id": "ibc/A0CC0CF735BFB30E730C70019D4218A1244FF383503FF7579C9201AB93CA9293",
                "description": "native token for Persistence",
                "primary": "",
            },
            {
                "uti": "akt/akash",
                "platform": "osmosis",
                "original_id": "ibc/1480B8FD20AD5FCAE81EA87584D269547DD4D436843C1D20F15E00EB64743EF4",
                "description": "native token for akash",
                "primary": "",
            },
            {
                "uti": "regen/regen",
                "platform": "osmosis",
                "original_id": "ibc/1DCC8A6CB5689018431323953344A9F6CC4D0BFB261E88C9F7777372C10CD076",
                "description": "native token for regen network",
                "primary": "",
            },
            {
                "uti": "dvpn/sentinel",
                "platform": "osmosis",
                "original_id": "ibc/9712DBB13B9631EDFA9BF61B55F1B2D290B2ADB67E3A4EB3A875F3B6081B3B84",
                "description": "native token for sentinel",
                "primary": "",
            },
        ]
        return token_original_id_table


if __name__ == "__main__":
    unittest.main()
