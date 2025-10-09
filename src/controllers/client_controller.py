from services.client_service import ClientService

class ClientController:
    def __init__(self):
        self.service = ClientService()

    def adicionar_cliente(self, owner_email: str):
        print("\n--- Adicionar Cliente ---")
        nome = input("Nome do cliente: ").strip()
        cpf = input("CPF (somente números): ").strip()
        try:
            client = self.service.add_client(owner_email, nome, cpf)
            print(f"Cliente '{client.name}' adicionado com sucesso!")
        except ValueError as e:
            print(f"{e}")

    def editar_cliente(self, owner_email: str):
        print("\n--- Editar Cliente ---")
        cpf = input("CPF do cliente a editar: ").strip()
        novo_nome = input("Novo nome: ").strip()
        try:
            client = self.service.edit_client(owner_email, cpf, novo_nome)
            print(f"Cliente atualizado: {client.name} (CPF: {client.cpf})")
        except ValueError as e:
            print(f"{e}")

    def remover_cliente(self, owner_email: str):
        print("\n--- Remover Cliente ---")
        cpf = input("CPF do cliente a remover: ").strip()
        try:
            self.service.remove_client(owner_email, cpf)
            print("Cliente removido com sucesso.")
        except ValueError as e:
            print(f"{e}")

    def listar_clientes(self, owner_email: str):
        print("\n--- Lista de Clientes ---")
        clients = self.service.list_clients(owner_email)
        if not clients:
            print("(Nenhum cliente cadastrado ainda)")
        else:
            for c in clients:
                print(f"- {c.name} | CPF: {c.cpf}")
