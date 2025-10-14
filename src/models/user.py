from __future__ import annotations
from dataclasses import dataclass, asdict

@dataclass
class User:
    name: str
    email: str
    password: str

    def to_dict(self):
        return asdict(self)
