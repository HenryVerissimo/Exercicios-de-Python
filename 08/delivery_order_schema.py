from dataclasses import dataclass, field

from config import ACCEPTED_TYPES

@dataclass
class DeliveryOrder:
    id: int
    weight: float
    distance: float
    type_of_load: str
    urgency: int = field(default=1)

    def __post_init__(self) -> None:
        self._verify_type_of_load()

    def _verify_type_of_load(self) -> None:

        if self.type_of_load not in ACCEPTED_TYPES:
            raise ValueError(f'Error: The "type_of_load" parameter in the DeliveryOrder is inválid! Use some valid type: {ACCEPTED_TYPES}')
