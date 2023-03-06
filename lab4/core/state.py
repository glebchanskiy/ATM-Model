from lab4.core.serializer.serializer import Serializer

class State:
    serializer: Serializer = None
    card_number: str = None
    pincode: str = None
    monies: int = None

    def __init__(self, serializer: Serializer) -> None:
        self.serializer = serializer

        data = self.serializer.deserialize()
        self.card_number = data['card_number']
        self.pincode = data['pincode']
        self.monies = data['monies']

    def dump(self) -> None:
        self.serializer.serialize(
            {
                'card_number': self.card_number,
                'pincode': self.pincode,
                'monies': self.monies
            }
        )

    def __del__(self) -> None:
        self.dump()
