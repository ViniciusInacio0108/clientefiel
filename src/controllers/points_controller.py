from services.points_service import PointsService

class PointsController:
    def __init__(self):
        self.service = PointsService()

    def adicionar_pontos(self, owner_email: str):
        print("\n--- Adicionar Pontos ---")
        cpf = input("CPF do cliente: ").strip()
        try:
            qtd = int(input("Quantidade de pontos a adicionar: "))
            data = self.service.add_points(owner_email, cpf, qtd)
            print(f"Cliente {cpf} agora tem {data.points} pontos.")
        except ValueError as e:
            print(f"{e}")

    def editar_pontos(self, owner_email: str):
        print("\n--- Editar Pontos ---")
        cpf = input("CPF do cliente: ").strip()
        try:
            qtd = int(input("Nova quantidade de pontos: "))
            data = self.service.edit_points(owner_email, cpf, qtd)
            print(f"Pontos atualizados: {data.points} pontos para o cliente {cpf}.")
        except ValueError as e:
            print(f"{e}")

    def remover_pontos(self, owner_email: str):
        print("\n--- Remover Pontos ---")
        cpf = input("CPF do cliente: ").strip()
        try:
            self.service.remove_points(owner_email, cpf)
            print(f"Pontos do cliente {cpf} foram removidos.")
        except ValueError as e:
            print(f"{e}")

    def listar_pontos(self, owner_email: str):
        print("\n--- Pontos dos Clientes ---")
        pontos = self.service.list_points(owner_email)
        if not pontos:
            print("(Nenhum cliente com pontos ainda)")
        else:
            for p in pontos:
                print(f"- CPF: {p.client_cpf} | Pontos: {p.points}")
