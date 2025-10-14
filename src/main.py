from __future__ import annotations
from controllers.user_controller import UserController
from controllers.client_controller import ClientController
from controllers.points_controller import PointsController

def menu():
    user_controller = UserController()
    client_controller = ClientController()
    points_controller = PointsController()
    logged_user = None

    while True:
        print("\n=== ClienteFiel (CLI) ===")
        print("1 - Cadastrar estabelecimento")
        print("2 - Login")
        if logged_user:
            print("3 - Editar estabelecimento")
            print("4 - Clientes")
            print("5 - Pontos & Recompensas")
            print("0 - Sair (logout)")
        else:
            print("0 - Sair")
        choosed_option = input("Opção: ").strip()

        try:
            if choosed_option == "1":
                user_controller.register()
            elif choosed_option == "2":
                logged_user = user_controller.login()
            elif choosed_option == "3" and logged_user:
                user_controller.edit(logged_user.email)
            elif choosed_option == "4" and logged_user:
                client_controller.menu(logged_user.email)
            elif choosed_option == "5" and logged_user:
                points_controller.menu(logged_user.email)
            elif choosed_option == "0":
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    menu()
