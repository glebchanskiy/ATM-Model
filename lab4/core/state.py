from typing import Dict, List, Tuple

import json
import os


class State:
    card_number: str = None
    pincode: str = None
    monies: int = None

    # args: List[Tuple[str, str]]

    def __init__(self) -> None:
        self.state_path = os.path.realpath(
            os.path.dirname(__file__))+"/state.json"
        with open(self.state_path, "r") as file:
            data = json.load(file)
            self.card_number = data['card_number']
            self.pincode = data['pincode']
            self.monies = data['monies']

    # def setUserInput(self, args: List[Tuple[str, str]]) -> None:
    #     self.args = args

    def dump(self) -> None:
        with open(self.state_path, "w") as file:
            json.dump(
                {
                    "card_number":  self.card_number,
                    "pincode":  self.pincode,
                    "monies": self.monies
                },
                file,
                indent=4
            )

    def __del__(self) -> None:
        self.dump()
