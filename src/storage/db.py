from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict

DATA_FILE = Path(__file__).parent / "data.json"

def _init_if_missing() -> None:
    if not DATA_FILE.exists():
        DATA_FILE.write_text(json.dumps({
            "users": [],
            "clients": [],
            "points": []
        }, ensure_ascii=False, indent=2), encoding="utf-8")

def load_db() -> Dict[str, Any]:
    _init_if_missing()
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))

def save_db(db: Dict[str, Any]) -> None:
    DATA_FILE.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")
