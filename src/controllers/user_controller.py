from services.user_service import UserService
class UserController:
    def __init__(self):
        self.service = UserService()

    def cadastrar(self):
        print("\n--- Cadastro ---")
        name = input("Digite seu nome: ").strip()
        email = input("Digite seu e-mail: ").strip()
        senha = input("Digite sua senha: ").strip()

        try:
            self.service.register_user(name, email, senha)
            print("Cadastro realizado com sucesso!")
        except ValueError as e:
            print(f"{e}")

    def login(self):
        print("\n--- Login ---")
        email = input("Digite seu e-mail: ").strip()
        senha = input("Digite sua senha: ").strip()

        user = self.service.authenticate(email, senha)
        if user:
            print(f"Bem-vindo, {user.name}! Login bem-sucedido.")
        else:
            print("E-mail ou senha incorretos.")

    def edit_user_name(self, logged_user_email: str):
        print("--- Editar nome de estabelecimento ---")
        new_name = input("Digite o novo nome: ").strip()
        saved_name = self.service.edit_user_name(logged_user_email, new_name)
        if saved_name:
            print(f"Nome alterado com sucesso! Bem-vindo {saved_name}")
        else:
            print("Não foi possível altera o nome.")