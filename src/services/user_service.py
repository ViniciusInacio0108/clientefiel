import re
from models.user_model import User

class UserService:
    _users = {}

    def email_is_valid(self, email: str) -> bool:
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    def password_is_valid(self, password: str) -> bool:
        return len(password) >= 6

    def user_exists(self, email: str) -> bool:
        return email in self._users

    def register_user(self, name: str, email: str, password: str):
        if not name.strip():
            raise ValueError("O nome não pode estar vazio.")
        if not self.email_is_valid(email):
            raise ValueError("E-mail inválido.")
        if not self.password_is_valid(password):
            raise ValueError("A senha deve ter pelo menos 6 caracteres.")
        if self.user_exists(email):
            raise ValueError("Este e-mail já está cadastrado.")

        user = User(name, email, password)
        self._users[email] = user
        return user

    def authenticate(self, email: str, password: str) -> User | None:
        user = self._users.get(email)
        if user and user.password == password:
            return user
        return None

    def list_users(self):
        return list(self._users.values())
