from controllers.user_controller import UserController

def menu():
    user_controller = UserController()
    logged_user = None

    while True:
        print("\n=== Sistema de Estabelecimentos ===")
        print("1 - Cadastrar estabelecimento")
        print("2 - Login")
        if logged_user:
            print("3 - Editar estabelecimento")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            user_controller.cadastrar()
        elif opcao == '2':
            logged_user = user_controller.service.authenticate(
                input("E-mail: ").strip(),
                input("Senha: ").strip()
            )
            if logged_user:
                print(f"Bem-vindo, {logged_user.name}!")
            else:
                print("E-mail ou senha incorretos.")
        elif opcao == '3' and logged_user:
            user_controller.edit_user_name(logged_user.email)
        elif opcao == '0':
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
