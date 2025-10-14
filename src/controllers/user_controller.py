from __future__ import annotations
from services.user_service import UserService

class UserController:
    def __init__(self):
        self.service = UserService()

    def register(self):
        print("\n--- Cadastro de Estabelecimento ---")
        name = input("Nome: ").strip()
        email = input("E-mail: ").strip()
        password = input("Senha (>=6): ").strip()
        self.service.register_user(name, email, password)
        print("Cadastro realizado com sucesso.")

    def login(self):
        print("\n--- Login ---")
        email = input("E-mail: ").strip()
        password = input("Senha: ").strip()
        user = self.service.login(email, password)
        if user:
            print(f"Bem-vindo(a), {user.name}!")
            return user
        print("Credenciais inválidas.")
        return None

    def edit(self, email: str):
        print("\n--- Editar Estabelecimento ---")
        new_name = input("Novo nome: ").strip()
        self.service.update_name(email, new_name)
        print("Nome atualizado com sucesso.")
