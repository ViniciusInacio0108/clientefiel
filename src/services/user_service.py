from __future__ import annotations
from typing import Optional, Dict, Any, List
from storage.db import load_db, save_db
from models.user import User
from utils.validators import is_valid_email, assert_password_strength, normalize_name

class UserService:
    def register_user(self, name: str, email: str, password: str) -> None:
        name = normalize_name(name)
        if not is_valid_email(email):
            raise ValueError("E-mail inválido.")
        assert_password_strength(password)

        db = load_db()
        if any(user['email'].lower() == email.lower() for user in db['users']):
            raise ValueError("E-mail já cadastrado.")
        db['users'].append(User(name=name, email=email, password=password).to_dict())
        save_db(db)

    def login(self, email: str, password: str) -> Optional[User]:
        if not is_valid_email(email):
            raise ValueError("E-mail inválido.")
        db = load_db()
        for user in db['users']:
            if user['email'].lower() == email.lower() and user['password'] == password:
                return User(**user)
        return None

    def update_name(self, email: str, new_name: str) -> None:
        new_name = normalize_name(new_name)
        db = load_db()
        for user in db['users']:
            if user['email'].lower() == email.lower():
                user['name'] = new_name
                save_db(db)
                return
        raise ValueError("Usuário não encontrado.")
