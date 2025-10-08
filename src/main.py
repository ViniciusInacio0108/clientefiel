from controllers.user_controller import UserController

def menu():
    controller = UserController()

    while True:
        print("\n=== Sistema de Estabelecimentos ===")
        print("1 - Cadastrar")
        print("2 - Login")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            controller.cadastrar()
        elif opcao == '2':
            controller.login()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
