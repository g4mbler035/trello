from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class Card:
    id: str
    badges: dict
    desc: str
    name: str