from __future__ import annotations
import re

def is_valid_email(email: str) -> bool:
    if not email or "@" not in email:
        return False
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email) is not None

def assert_password_strength(password: str) -> None:
    if not password or len(password) < 6:
        raise ValueError("Senha deve ter pelo menos 6 caracteres.")

def normalize_name(name: str) -> str:
    if not name or len(name.strip()) < 2:
        raise ValueError("Nome inválido.")
    return " ".join(p.capitalize() for p in name.strip().split())

def normalize_cpf(cpf: str) -> str:
    digits = re.sub(r"\D", "", cpf or "")
    if len(digits) != 11:
        raise ValueError("CPF deve conter 11 dígitos.")
    return digits
