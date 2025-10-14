from __future__ import annotations
from dataclasses import dataclass, asdict

@dataclass
class Client:
    owner_email: str
    name: str
    cpf: str

    def to_dict(self):
        return asdict(self)
