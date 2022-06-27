import importlib
import os
import re
from typing import List

from senkalib.platform.transaction_generator import TransactionGenerator


class SenkaLib:
    TOKEN_OERIGINAK_IDS_URL = "https://raw.githubusercontent.com/ca3-caaip/token_original_id/master/token_original_id.csv"

    @classmethod
    def get_available_platform(cls, blacklist=[]) -> List[TransactionGenerator]:
        available_platforms = []
        try:
            blacklist.append("__pycache__")
            path = "%s/platform" % os.path.dirname(__file__)
            files = os.listdir(path)
            dirs = sorted(
                [
                    f
                    for f in files
                    if os.path.isdir(os.path.join(path, f)) and f not in blacklist
                ]
            )

            for dir in dirs:
                module = importlib.import_module(
                    f"senkalib.platform.{dir}.{dir}_transaction_generator", "senkalib"
                )
                transaction_generator = list(f"{dir}_transaction_generator")
                transaction_generator[0] = transaction_generator[0].upper()
                transaction_generator = "".join(transaction_generator)
                transaction_generator = re.sub(
                    "_(.)", lambda x: x.group(1).upper(), transaction_generator
                )
                transaction_generator = getattr(module, transaction_generator)
                available_platforms.append(transaction_generator)
        except Exception as e:
            f"failed to load senkalib transaction generator: {e}"
            raise e

        return available_platforms
