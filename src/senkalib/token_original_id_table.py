import csv
from typing import Union

import requests


class TokenOriginalIdTable:
    def __init__(self, csv_url: str):
        res = requests.get(csv_url).content.decode()
        csv_reader = csv.DictReader(res.strip().splitlines())
        token_original_id_table = list(
            map(
                TokenOriginalIdTable._replace_bool_from_str,
                [row for row in csv_reader],
            )
        )
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
                    and x["primary"] is True,
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

    def get_symbol_uuid(
        self,
        platform: str,
        token_original_id: str,
    ) -> Union[str, None]:
        meta_data = self.get_all_meta_data(platform, token_original_id)
        if meta_data is not None:
            return meta_data["symbol_uuid"]
        else:
            return None

    def get_symbol(
        self,
        platform: str,
        token_original_id: str,
    ) -> Union[str, None]:
        meta_data = self.get_all_meta_data(platform, token_original_id)
        if meta_data is not None:
            return meta_data["symbol"]
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

    @staticmethod
    def _replace_bool_from_str(value: dict) -> dict:
        if value["primary"].lower() == "true":
            value["primary"] = True
        elif value["primary"].lower() == "false":
            value["primary"] = False
        else:
            raise ValueError(
                f"token_original_id table have invalid primary value."
                f" primary: {value['primary']}"
                f" original_id: {value['original_id']}"
            )
        return value
