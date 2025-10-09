import re
from models.client_model import Client

class ClientService:
    _clients_by_owner = {}

    def _validate_name(self, name: str):
        if not name.strip():
            raise ValueError("O nome do cliente não pode estar vazio.")

    def _validate_cpf(self, cpf: str):
        cpf_pattern = r'^\d{11}$'
        if not re.match(cpf_pattern, cpf):
            raise ValueError("CPF inválido. Use apenas 11 dígitos numéricos.")

    def add_client(self, owner_email: str, name: str, cpf: str):
        self._validate_name(name)
        self._validate_cpf(cpf)

        if owner_email not in self._clients_by_owner:
            self._clients_by_owner[owner_email] = {}

        clients = self._clients_by_owner[owner_email]
        if cpf in clients:
            raise ValueError("Já existe um cliente com esse CPF.")

        client = Client(name, cpf, owner_email)
        clients[cpf] = client
        return client

    def edit_client(self, owner_email: str, cpf: str, new_name: str):
        self._validate_name(new_name)

        clients = self._clients_by_owner.get(owner_email, {})
        if cpf not in clients:
            raise ValueError("Cliente não encontrado.")

        clients[cpf].name = new_name
        return clients[cpf]

    def remove_client(self, owner_email: str, cpf: str):
        clients = self._clients_by_owner.get(owner_email, {})
        if cpf not in clients:
            raise ValueError("Cliente não encontrado.")
        del clients[cpf]

    def list_clients(self, owner_email: str):
        return list(self._clients_by_owner.get(owner_email, {}).values())
