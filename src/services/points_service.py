from __future__ import annotations
from typing import List, Dict
from storage.db import load_db, save_db
from models.points import Points
from utils.validators import normalize_cpf

class PointsService:
    def add_points(self, owner_email: str, client_cpf: str, to_add_points: int) -> None:
        client_cpf = normalize_cpf(client_cpf)
        db = load_db()
        if not any(c['owner_email']==owner_email and c['cpf']==client_cpf for c in db['clients']):
            raise ValueError("Cliente não existe para este estabelecimento.")
        points_records = next((points for points in db['points'] if points['owner_email']==owner_email and points['client_cpf']==client_cpf), None)
        if points_records:
            points_records['points'] += to_add_points
        else:
            db['points'].append(Points(owner_email=owner_email, client_cpf=client_cpf, points=max(0, to_add_points)).to_dict())
        save_db(db)

    def set_points(self, owner_email: str, client_cpf: str, value: int) -> None:
        client_cpf = normalize_cpf(client_cpf)
        db = load_db()
        points_records = next((points for points in db['points'] if points['owner_email']==owner_email and points['client_cpf']==client_cpf), None)
        if not points_records:
            raise ValueError("Registro de pontos não encontrado.")
        points_records['points'] = max(0, value)
        save_db(db)

    def remove_points(self, owner_email: str, client_cpf: str, to_remove_points: int) -> None:
        self.add_points(owner_email, client_cpf, -abs(to_remove_points))

    def list_points(self, owner_email: str) -> List[Dict]:
        db = load_db()
        return [points for points in db['points'] if points['owner_email']==owner_email]
