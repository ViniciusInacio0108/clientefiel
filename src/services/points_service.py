from models.points_model import Points
from services.client_service import ClientService

class PointsService:
    _points_data = {}

    def __init__(self):
        self.client_service = ClientService()

    def _ensure_client_exists(self, owner_email: str, client_cpf: str):
        clients = self.client_service.list_clients(owner_email)
        if not any(c.cpf == client_cpf for c in clients):
            raise ValueError("Cliente não encontrado na base de dados.")

    def add_points(self, owner_email: str, client_cpf: str, amount: int):
        self._ensure_client_exists(owner_email, client_cpf)
        if amount <= 0:
            raise ValueError("A quantidade de pontos deve ser positiva.")

        if owner_email not in self._points_data:
            self._points_data[owner_email] = {}

        client_points = self._points_data[owner_email].get(client_cpf)
        if not client_points:
            client_points = Points(owner_email, client_cpf, 0)
            self._points_data[owner_email][client_cpf] = client_points

        client_points.points += amount
        return client_points

    def edit_points(self, owner_email: str, client_cpf: str, new_amount: int):
        self._ensure_client_exists(owner_email, client_cpf)
        if new_amount < 0:
            raise ValueError("Os pontos não podem ser negativos.")

        owner_points = self._points_data.get(owner_email, {})
        client_points = owner_points.get(client_cpf)
        if not client_points:
            raise ValueError("Este cliente ainda não possui pontos registrados.")

        client_points.points = new_amount
        return client_points

    def remove_points(self, owner_email: str, client_cpf: str):
        self._ensure_client_exists(owner_email, client_cpf)
        owner_points = self._points_data.get(owner_email, {})
        client_points = owner_points.get(client_cpf)

        if not client_points or client_points.points == 0:
            raise ValueError("Cliente não possui pontos para remover.")

        del owner_points[client_cpf]

    def list_points(self, owner_email: str):
        owner_points = self._points_data.get(owner_email, {})
        return list(owner_points.values())
