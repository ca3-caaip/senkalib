import csv
import json
import urllib.parse
from typing import Union
from xmlrpc.client import boolean

import requests


class TokenOriginalIdTable:
    def __init__(self, csv_url: str):
        res = requests.get(csv_url).content.decode()
        csv_reader = csv.DictReader(res.strip().splitlines())
        token_original_id_table = [row for row in csv_reader]
        self.token_original_id_table = token_original_id_table

    def get_all_meta_data(
        self,
        platform: str,
        token_original_id: str,
    ) -> Union[dict, None]:
        object_token = []
        try:
            object_token = list(
                filter(
                    lambda x: x["original_id"].lower() == token_original_id.lower()
                    and x["platform"].lower() == platform.lower(),
                    self.token_original_id_table,
                )
            )
        except Exception as e:
            if not e.args:
                e.args = ("",)
            e.args = (
                f"object token filtering is failed"
                f" token_original_id.lower(): {token_original_id.lower()}. platform: {platform.lower()}. {str(e)}"
                f"{json.dumps(self.token_original_id_table)}",
            )
            raise e

        if len(object_token) == 0:
            object_token = list(
                filter(
                    lambda x: x["original_id"].lower() == token_original_id.lower()
                    and "/" not in x["uti"],
                    self.token_original_id_table,
                )
            )

        token_symbol = None
        if len(object_token) >= 1:
            token_symbol = object_token[0]
        return token_symbol

    def get_uti(
        self,
        platform: str,
        token_original_id: str,
        default_symbol: Union[str, None] = None,
    ) -> str:
        meta_data = self.get_all_meta_data(platform, token_original_id)
        if meta_data is not None:
            return meta_data["uti"]
        else:
            if default_symbol is not None:
                return (
                    f"{default_symbol}/{urllib.parse.quote(token_original_id, safe='')}"
                )
            else:
                return f"{urllib.parse.quote(token_original_id, safe='')}"

    def get_only_uti(
        self,
        platform: str,
        token_original_id: str,
    ) -> Union[str, boolean]:
        meta_data = self.get_all_meta_data(platform, token_original_id)
        if meta_data is not None:
            return meta_data["uti"]
        else:
            return False

    def get_symbol(
        self,
        platform: str,
        token_original_id: str,
    ) -> Union[str, None]:
        meta_data = self.get_all_meta_data(platform, token_original_id)
        if meta_data is not None:
            symbol = urllib.parse.unquote(meta_data["uti"].split("/")[0])
            return symbol
        else:
            return None
