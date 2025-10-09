from controllers.user_controller import UserController
from controllers.client_controller import ClientController
from controllers.points_controller import PointsController

def menu():
    user_controller = UserController()
    client_controller = ClientController()
    points_controller = PointsController()
    logged_user = None

    while True:
        print("\n=== Sistema de Estabelecimentos ===")
        print("1 - Cadastrar estabelecimento")
        print("2 - Login")
        if logged_user:
            print("3 - Editar estabelecimento")
            print("4 - Gerenciar clientes")
            print("5 - Gerenciar pontos e recompensas")
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
        elif opcao == '4' and logged_user:
            menu_clientes(client_controller, logged_user.email)
        elif opcao == '5' and logged_user:
            menu_pontos(points_controller, logged_user.email)
        elif opcao == '0':
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

def menu_clientes(client_controller, owner_email):
    while True:
        print("\n=== Gerenciamento de Clientes ===")
        print("1 - Adicionar cliente")
        print("2 - Editar cliente")
        print("3 - Remover cliente")
        print("4 - Listar clientes")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            client_controller.adicionar_cliente(owner_email)
        elif opcao == '2':
            client_controller.editar_cliente(owner_email)
        elif opcao == '3':
            client_controller.remover_cliente(owner_email)
        elif opcao == '4':
            client_controller.listar_clientes(owner_email)
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

def menu_pontos(points_controller, owner_email):
    while True:
        print("\n=== Gerenciamento de Pontos ===")
        print("1 - Adicionar pontos")
        print("2 - Editar pontos")
        print("3 - Remover pontos")
        print("4 - Listar pontos dos clientes")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            points_controller.adicionar_pontos(owner_email)
        elif opcao == '2':
            points_controller.editar_pontos(owner_email)
        elif opcao == '3':
            points_controller.remover_pontos(owner_email)
        elif opcao == '4':
            points_controller.listar_pontos(owner_email)
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
