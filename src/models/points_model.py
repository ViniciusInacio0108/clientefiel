class Points:
    def __init__(self, owner_email: str, client_cpf: str, points: int = 0):
        self.owner_email = owner_email
        self.client_cpf = client_cpf
        self.points = points

    def to_dict(self):
        return {
            "owner_email": self.owner_email,
            "client_cpf": self.client_cpf,
            "points": self.points
        }
