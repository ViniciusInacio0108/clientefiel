"""
Testes unitários para os modelos de dados.
Valida estrutura e comportamento dos dataclasses: User, Client e Points.
"""
import pytest
from models.user import User
from models.client import Client
from models.points import Points


class TestUserModel:
    """Testes para o modelo User"""

    def test_criar_usuario_com_dados_validos(self):
        """ARRANGE-ACT-ASSERT: Deve criar um User com dados válidos"""
        # ARRANGE
        nome = "João Silva"
        email = "joao@example.com"
        senha = "SenhaSegura123!"
        
        # ACT
        usuario = User(name=nome, email=email, password=senha)
        
        # ASSERT
        assert usuario.name == nome
        assert usuario.email == email
        assert usuario.password == senha

    def test_usuario_to_dict(self):
        """User deve ser convertível para dicionário"""
        # ARRANGE
        usuario = User(name="João", email="joao@test.com", password="senha123")
        
        # ACT
        dict_usuario = usuario.to_dict()
        
        # ASSERT
        assert dict_usuario == {
            "name": "João",
            "email": "joao@test.com",
            "password": "senha123"
        }
        assert isinstance(dict_usuario, dict)

    def test_usuario_atributos_imutaveis(self):
        """User com dataclass padrão permite modificação de atributos"""
        # ARRANGE
        usuario = User(name="João", email="joao@test.com", password="senha123")
        
        # ACT
        usuario.name = "Maria"
        
        # ASSERT
        assert usuario.name == "Maria"


class TestClientModel:
    """Testes para o modelo Client"""

    def test_criar_cliente_com_dados_validos(self):
        """Deve criar um Client com dados válidos"""
        # ARRANGE
        owner_email = "loja@example.com"
        nome = "Cliente Teste"
        cpf = "12345678901"
        
        # ACT
        cliente = Client(owner_email=owner_email, name=nome, cpf=cpf)
        
        # ASSERT
        assert cliente.owner_email == owner_email
        assert cliente.name == nome
        assert cliente.cpf == cpf

    def test_cliente_to_dict(self):
        """Client deve ser convertível para dicionário"""
        # ARRANGE
        cliente = Client(
            owner_email="loja@test.com",
            name="Cliente",
            cpf="12345678901"
        )
        
        # ACT
        dict_cliente = cliente.to_dict()
        
        # ASSERT
        assert dict_cliente == {
            "owner_email": "loja@test.com",
            "name": "Cliente",
            "cpf": "12345678901"
        }

    def test_cliente_sem_email_valido(self):
        """Client permite qualquer string para owner_email (validação é responsibility do service)"""
        # ARRANGE & ACT
        cliente = Client(
            owner_email="invalido",
            name="Cliente",
            cpf="12345678901"
        )
        
        # ASSERT
        assert cliente.owner_email == "invalido"


class TestPointsModel:
    """Testes para o modelo Points"""

    def test_criar_registro_pontos_com_valor_default(self):
        """Deve criar Points com valor default de 0"""
        # ARRANGE
        owner_email = "loja@example.com"
        client_cpf = "12345678901"
        
        # ACT
        pontos = Points(owner_email=owner_email, client_cpf=client_cpf)
        
        # ASSERT
        assert pontos.owner_email == owner_email
        assert pontos.client_cpf == client_cpf
        assert pontos.points == 0

    def test_criar_registro_pontos_com_valor_especifico(self):
        """Deve criar Points com valor específico"""
        # ARRANGE
        owner_email = "loja@example.com"
        client_cpf = "12345678901"
        valor = 150
        
        # ACT
        pontos = Points(
            owner_email=owner_email,
            client_cpf=client_cpf,
            points=valor
        )
        
        # ASSERT
        assert pontos.points == valor

    def test_pontos_to_dict(self):
        """Points deve ser convertível para dicionário"""
        # ARRANGE
        pontos = Points(
            owner_email="loja@test.com",
            client_cpf="12345678901",
            points=100
        )
        
        # ACT
        dict_pontos = pontos.to_dict()
        
        # ASSERT
        assert dict_pontos == {
            "owner_email": "loja@test.com",
            "client_cpf": "12345678901",
            "points": 100
        }

    def test_pontos_valor_negativo(self):
        """Points aceita valores negativos (validação é responsabilidade do service)"""
        # ARRANGE & ACT
        pontos = Points(
            owner_email="loja@test.com",
            client_cpf="12345678901",
            points=-50
        )
        
        # ASSERT
        assert pontos.points == -50
