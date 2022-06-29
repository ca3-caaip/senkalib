import csv
import urllib.parse
from typing import Union

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
        object_token = list(
            filter(
                lambda x: x["original_id"] == token_original_id
                and x["platform"] == platform,
                self.token_original_id_table,
            )
        )

        if len(object_token) == 0:
            object_token = list(
                filter(
                    lambda x: x["original_id"] == token_original_id
                    and x.get("primary", ""),
                    self.token_original_id_table,
                )
            )

        token_symbol = None
        if len(object_token) == 1:
            token_symbol = object_token[0]
        elif len(object_token) > 1:
            raise ValueError(
                f"token_original_id table have duplicated definition. token_original_id: {token_original_id}"
            )
        return token_symbol

    def get_uti(
        self,
        platform: str,
        token_original_id: str,
    ) -> Union[str, None]:
        meta_data = self.get_all_meta_data(platform, token_original_id)
        if meta_data is not None:
            return meta_data["uti"]
        else:
            return f"{urllib.parse.quote(token_original_id, safe='')}/{urllib.parse.quote(platform, safe='')}"

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

    def get_description(
        self,
        platform: str,
        token_original_id: str,
    ) -> Union[str, None]:
        meta_data = self.get_all_meta_data(platform, token_original_id)
        if meta_data is not None:
            return meta_data["description"]
        else:
            return None
