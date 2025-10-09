class Client:
    def __init__(self, name: str, cpf: str, establishment_email_owner: str):
        self.name = name
        self.cpf = cpf
        self.establishment_email_owner = establishment_email_owner

    def to_dict(self):
        return {
            "name": self.name,
            "cpf": self.cpf,
            "establishment_email_owner": self.establishment_email_owner
        }
