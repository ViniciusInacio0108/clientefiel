from __future__ import annotations
from services.client_service import ClientService

class ClientController:
    def __init__(self):
        self.service = ClientService()

    def menu(self, owner_email: str):
        while True:
            print("\n--- Clientes ---")
            print("1 - Adicionar")
            print("2 - Editar")
            print("3 - Remover")
            print("4 - Listar")
            print("0 - Voltar")
            choosed_option = input("Opção: ").strip()
            try:
                if choosed_option == "1":
                    name = input("Nome do cliente: ")
                    cpf = input("CPF: ")
                    self.service.add_client(owner_email, name, cpf)
                    print("Cliente adicionado.")
                elif choosed_option == "2":
                    cpf = input("CPF do cliente: ")
                    new_name = input("Novo nome: ")
                    self.service.edit_client(owner_email, cpf, new_name)
                    print("Cliente atualizado.")
                elif choosed_option == "3":
                    cpf = input("CPF do cliente: ")
                    self.service.remove_client(owner_email, cpf)
                    print("Cliente removido.")
                elif choosed_option == "4":
                    for client in self.service.list_clients(owner_email):
                        print(f"- {client['name']} (CPF {client['cpf']})")
                elif choosed_option == "0":
                    break
                else:
                    print("Opção inválida.")
            except Exception as e:
                print(f"Erro: {e}")
