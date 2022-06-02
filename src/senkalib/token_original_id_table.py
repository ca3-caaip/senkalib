import csv
from typing import Union

import requests


class TokenOriginalIdTable:
    def __init__(self, csv_url: str):
        res = requests.get(csv_url).content.decode()
        csv_reader = csv.DictReader(res.strip().splitlines())
        token_original_id_table_without_bool = [row for row in csv_reader]
        token_original_id_table = list(
            map(
                TokenOriginalIdTable._replace_bool_from_str,
                token_original_id_table_without_bool,
            )
        )
        self.token_original_id_table = token_original_id_table

    def get_all_meta_data(
        self, platform: str, token_original_id: str
    ) -> Union[dict, None]:

        object_token = list(
            filter(
                lambda x: x["original_id"] == token_original_id
                and x["platform"] == platform,
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

    def get_all_meta_data_without_platform(
        self, token_original_id: str, primary: bool = True
    ) -> Union[dict, None]:
        object_token = list(
            filter(
                lambda x: x["original_id"] == token_original_id
                and x["primary"] == primary,
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
        self, platform: Union[str, None], token_original_id: str, primary: bool = True
    ) -> Union[str, None]:
        if platform is not None:
            meta_data = self.get_all_meta_data(platform, token_original_id)
            if meta_data is not None:
                return meta_data["symbol_uuid"]
            else:
                return None

        else:
            meta_data = self.get_all_meta_data_without_platform(
                token_original_id, primary
            )
            if meta_data is not None:
                return meta_data["symbol_uuid"]
            else:
                return None

    def get_symbol(
        self, platform: Union[str, None], token_original_id: str, primary: bool = True
    ) -> Union[str, None]:
        if platform is not None:
            meta_data = self.get_all_meta_data(platform, token_original_id)
            if meta_data is not None:
                return meta_data["symbol"]
            else:
                return None

        else:
            meta_data = self.get_all_meta_data_without_platform(
                token_original_id, primary
            )
            if meta_data is not None:
                return meta_data["symbol"]
            else:
                return None

    def get_description(
        self,
        platform: Union[str, None],
        token_original_id: str,
        primary: bool = True,
    ) -> Union[str, None]:
        if platform is not None:
            meta_data = self.get_all_meta_data(platform, token_original_id)
            if meta_data is not None:
                return meta_data["description"]
            else:
                return None

        else:
            meta_data = self.get_all_meta_data_without_platform(
                token_original_id, primary
            )
            if meta_data is not None:
                return meta_data["description"]
            else:
                return None

    def get_platform(
        self,
        token_original_id: str,
        primary: bool = True,
    ) -> Union[str, None]:
        meta_data = self.get_all_meta_data_without_platform(token_original_id, primary)
        if meta_data is not None:
            return meta_data["platform"]
        else:
            return None

    @staticmethod
    def _replace_bool_from_str(value: dict) -> dict:
        if value["primary"] == "TRUE":
            value["primary"] = True
        elif value["primary"] == "FALSE":
            value["primary"] = False
        return value
