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
    cpf = re.sub(r"\D", "", cpf or "")

    if len(cpf) != 11:
        raise ValueError("CPF deve conter 11 dígitos.")
    
    soma = 0
    peso = 10 
    
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = soma % 11
    
    dv1_calculado = 0 if resto < 2 else 11 - resto
    
    if dv1_calculado != int(cpf[9]):
        raise ValueError("CPF inválido!")

    soma = 0
    peso = 11
    
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1
        
    resto = soma % 11
    
    dv2_calculado = 0 if resto < 2 else 11 - resto
    
    if dv2_calculado != int(cpf[10]):
        raise ValueError("CPF inválido!")

    return cpf