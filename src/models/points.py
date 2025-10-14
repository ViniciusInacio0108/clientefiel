from __future__ import annotations
from dataclasses import dataclass, asdict

@dataclass
class Points:
    owner_email: str
    client_cpf: str
    points: int = 0

    def to_dict(self):
        return asdict(self)
