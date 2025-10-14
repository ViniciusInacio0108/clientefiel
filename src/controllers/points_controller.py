from __future__ import annotations
from services.points_service import PointsService

class PointsController:
    def __init__(self):
        self.service = PointsService()

    def menu(self, owner_email: str):
        while True:
            print("\n--- Pontos & Recompensas ---")
            print("1 - Adicionar pontos")
            print("2 - Ajustar pontos (definir valor)")
            print("3 - Remover pontos")
            print("4 - Listar")
            print("0 - Voltar")
            choosed_option = input("Opção: ").strip()
            try:
                if choosed_option == "1":
                    cpf = input("CPF do cliente: ")
                    to_add_points = int(input("Pontos a adicionar: "))
                    self.service.add_points(owner_email, cpf, to_add_points)
                    print("Pontos adicionados.")
                elif choosed_option == "2":
                    cpf = input("CPF do cliente: ")
                    new_points_value = int(input("Novo total de pontos: "))
                    self.service.set_points(owner_email, cpf, new_points_value)
                    print("Pontos ajustados.")
                elif choosed_option == "3":
                    cpf = input("CPF do cliente: ")
                    to_remove_points = int(input("Pontos a remover: "))
                    self.service.remove_points(owner_email, cpf, to_remove_points)
                    print("Pontos removidos.")
                elif choosed_option == "4":
                    for point in self.service.list_points(owner_email):
                        print(f"- CPF {point['client_cpf']}: {point['points']} ponto(s)")
                elif choosed_option == "0":
                    break
                else:
                    print("Opção inválida.")
            except Exception as e:
                print(f"Erro: {e}")
