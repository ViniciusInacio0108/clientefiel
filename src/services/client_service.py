from __future__ import annotations
from typing import List, Dict
from storage.db import load_db, save_db
from models.client import Client
from utils.validators import normalize_cpf, normalize_name

class ClientService:
    def add_client(self, owner_email: str, name: str, cpf: str) -> None:
        name = normalize_name(name)
        cpf = normalize_cpf(cpf)
        db = load_db()
        if any(client['owner_email']==owner_email and client['cpf']==cpf for client in db['clients']):
            raise ValueError("Cliente já cadastrado para este estabelecimento.")
        db['clients'].append(Client(owner_email=owner_email, name=name, cpf=cpf).to_dict())
        save_db(db)

    def edit_client(self, owner_email: str, cpf: str, new_name: str) -> None:
        cpf = normalize_cpf(cpf)
        new_name = normalize_name(new_name)
        db = load_db()
        for client in db['clients']:
            if client['owner_email']==owner_email and client['cpf']==cpf:
                client['name'] = new_name
                save_db(db)
                return
        raise ValueError("Cliente não encontrado.")

    def remove_client(self, owner_email: str, cpf: str) -> None:
        cpf = normalize_cpf(cpf)
        db = load_db()
        length_clients_before = len(db['clients'])
        db['clients'] = [client for client in db['clients'] if not (client['owner_email']==owner_email and client['cpf']==cpf)]
        if len(db['clients']) == length_clients_before:
            raise ValueError("Cliente não encontrado.")
        save_db(db)

    def list_clients(self, owner_email: str) -> List[Dict]:
        db = load_db()
        return [client for client in db['clients'] if client['owner_email']==owner_email]
