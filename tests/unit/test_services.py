"""
Testes unitários para os serviços de negócio.
Valida lógica de criação, edição e remoção de usuários, clientes e pontos.
"""
import pytest
from unittest.mock import patch, MagicMock
from services.user_service import UserService
from services.client_service import ClientService
from services.points_service import PointsService
from models.user import User


class TestUserService:
    """Testes para o serviço de usuários"""

    @patch('services.user_service.load_db')
    @patch('services.user_service.save_db')
    def test_registrar_usuario_com_dados_validos(self, mock_save, mock_load, sample_user):
        """ARRANGE-ACT-ASSERT: Deve registrar usuário com dados válidos"""
        # ARRANGE
        mock_load.return_value = {"users": [], "clients": [], "points": []}
        servico = UserService()
        
        # ACT
        servico.register_user(
            name=sample_user["name"],
            email=sample_user["email"],
            password=sample_user["password"]
        )
        
        # ASSERT
        mock_save.assert_called_once()
        db_salvo = mock_save.call_args[0][0]
        assert len(db_salvo["users"]) == 1
        assert db_salvo["users"][0]["email"] == sample_user["email"]

    @patch('services.user_service.load_db')
    @patch('services.user_service.save_db')
    def test_registrar_usuario_email_invalido(self, mock_save, mock_load):
        """Deve falhar ao registrar usuário com email inválido"""
        # ARRANGE
        mock_load.return_value = {"users": [], "clients": [], "points": []}
        servico = UserService()
        
        # ACT & ASSERT
        with pytest.raises(ValueError, match="E-mail inválido"):
            servico.register_user(
                name="João Silva",
                email="emailsemarroba",
                password="SenhaSegura123!"
            )

    @patch('services.user_service.load_db')
    @patch('services.user_service.save_db')
    def test_registrar_usuario_senha_fraca(self, mock_save, mock_load):
        """Deve falhar ao registrar usuário com senha fraca"""
        # ARRANGE
        mock_load.return_value = {"users": [], "clients": [], "points": []}
        servico = UserService()
        
        # ACT & ASSERT
        with pytest.raises(ValueError, match="Senha deve ter pelo menos 6 caracteres"):
            servico.register_user(
                name="João Silva",
                email="joao@example.com",
                password="123"
            )

    @patch('services.user_service.load_db')
    @patch('services.user_service.save_db')
    def test_registrar_usuario_email_duplicado(self, mock_save, mock_load, sample_user):
        """Deve falhar ao registrar usuário com email já existente"""
        # ARRANGE
        mock_load.return_value = {
            "users": [sample_user],
            "clients": [],
            "points": []
        }
        servico = UserService()
        
        # ACT & ASSERT
        with pytest.raises(ValueError, match="E-mail já cadastrado"):
            servico.register_user(
                name="Outro Nome",
                email=sample_user["email"],
                password="OutraSenha123!"
            )

    @patch('services.user_service.load_db')
    def test_login_usuario_sucesso(self, mock_load, sample_user):
        """Deve fazer login com credenciais válidas"""
        # ARRANGE
        mock_load.return_value = {
            "users": [sample_user],
            "clients": [],
            "points": []
        }
        servico = UserService()
        
        # ACT
        usuario = servico.login(
            email=sample_user["email"],
            password=sample_user["password"]
        )
        
        # ASSERT
        assert usuario is not None
        assert usuario.email == sample_user["email"]
        assert usuario.name == sample_user["name"]

    @patch('services.user_service.load_db')
    def test_login_usuario_senha_incorreta(self, mock_load, sample_user):
        """Deve falhar ao fazer login com senha incorreta"""
        # ARRANGE
        mock_load.return_value = {
            "users": [sample_user],
            "clients": [],
            "points": []
        }
        servico = UserService()
        
        # ACT
        usuario = servico.login(
            email=sample_user["email"],
            password="SenhaErrada123!"
        )
        
        # ASSERT
        assert usuario is None

    @patch('services.user_service.load_db')
    @patch('services.user_service.save_db')
    def test_atualizar_nome_usuario(self, mock_save, mock_load, sample_user):
        """Deve atualizar nome do usuário"""
        # ARRANGE
        mock_load.return_value = {
            "users": [sample_user],
            "clients": [],
            "points": []
        }
        servico = UserService()
        novo_nome = "Maria Silva"
        
        # ACT
        servico.update_name(email=sample_user["email"], new_name=novo_nome)
        
        # ASSERT
        mock_save.assert_called_once()
        db_salvo = mock_save.call_args[0][0]
        assert db_salvo["users"][0]["name"] == "Maria Silva"

    @patch('services.user_service.load_db')
    @patch('services.user_service.save_db')
    def test_atualizar_nome_usuario_nao_existente(self, mock_save, mock_load):
        """Deve falhar ao atualizar usuário inexistente"""
        # ARRANGE
        mock_load.return_value = {"users": [], "clients": [], "points": []}
        servico = UserService()
        
        # ACT & ASSERT
        with pytest.raises(ValueError, match="Usuário não encontrado"):
            servico.update_name(
                email="inexistente@example.com",
                new_name="Novo Nome"
            )


class TestClientService:
    """Testes para o serviço de clientes"""

    @patch('services.client_service.load_db')
    @patch('services.client_service.save_db')
    def test_adicionar_cliente_com_dados_validos(self, mock_save, mock_load, sample_client):
        """ARRANGE-ACT-ASSERT: Deve adicionar cliente com dados válidos"""
        # ARRANGE
        mock_load.return_value = {"users": [], "clients": [], "points": []}
        servico = ClientService()
        
        # ACT
        servico.add_client(
            owner_email=sample_client["owner_email"],
            name=sample_client["name"],
            cpf=sample_client["cpf"]
        )
        
        # ASSERT
        mock_save.assert_called_once()
        db_salvo = mock_save.call_args[0][0]
        assert len(db_salvo["clients"]) == 1
        assert db_salvo["clients"][0]["cpf"] == sample_client["cpf"]

    @patch('services.client_service.load_db')
    @patch('services.client_service.save_db')
    def test_adicionar_cliente_duplicado(self, mock_save, mock_load, sample_client):
        """Deve falhar ao adicionar cliente duplicado"""
        # ARRANGE
        mock_load.return_value = {
            "users": [],
            "clients": [sample_client],
            "points": []
        }
        servico = ClientService()
        
        # ACT & ASSERT
        with pytest.raises(ValueError, match="Cliente já cadastrado"):
            servico.add_client(
                owner_email=sample_client["owner_email"],
                name="Outro Nome",
                cpf=sample_client["cpf"]
            )

    @patch('services.client_service.load_db')
    @patch('services.client_service.save_db')
    def test_editar_cliente(self, mock_save, mock_load, sample_client):
        """Deve editar nome do cliente"""
        # ARRANGE
        mock_load.return_value = {
            "users": [],
            "clients": [sample_client],
            "points": []
        }
        servico = ClientService()
        novo_nome = "Cliente Atualizado"
        
        # ACT
        servico.edit_client(
            owner_email=sample_client["owner_email"],
            cpf=sample_client["cpf"],
            new_name=novo_nome
        )
        
        # ASSERT
        mock_save.assert_called_once()
        db_salvo = mock_save.call_args[0][0]
        assert db_salvo["clients"][0]["name"] == "Cliente Atualizado"

    @patch('services.client_service.load_db')
    @patch('services.client_service.save_db')
    def test_remover_cliente(self, mock_save, mock_load, sample_client):
        """Deve remover cliente existente"""
        # ARRANGE
        mock_load.return_value = {
            "users": [],
            "clients": [sample_client],
            "points": []
        }
        servico = ClientService()
        
        # ACT
        servico.remove_client(
            owner_email=sample_client["owner_email"],
            cpf=sample_client["cpf"]
        )
        
        # ASSERT
        mock_save.assert_called_once()
        db_salvo = mock_save.call_args[0][0]
        assert len(db_salvo["clients"]) == 0

    @patch('services.client_service.load_db')
    def test_listar_clientes_do_estabelecimento(self, mock_load, sample_client):
        """Deve listar apenas clientes do estabelecimento"""
        # ARRANGE
        outro_cliente = {
            "owner_email": "outra_loja@example.com",
            "name": "Outro Cliente",
            "cpf": "98765432101"
        }
        mock_load.return_value = {
            "users": [],
            "clients": [sample_client, outro_cliente],
            "points": []
        }
        servico = ClientService()
        
        # ACT
        clientes = servico.list_clients(owner_email=sample_client["owner_email"])
        
        # ASSERT
        assert len(clientes) == 1
        assert clientes[0]["cpf"] == sample_client["cpf"]


class TestPointsService:
    """Testes para o serviço de pontos"""

    @patch('services.points_service.load_db')
    @patch('services.points_service.save_db')
    def test_adicionar_pontos_novo_cliente(self, mock_save, mock_load, sample_client, sample_points):
        """ARRANGE-ACT-ASSERT: Deve adicionar pontos para novo cliente"""
        # ARRANGE
        mock_load.return_value = {
            "users": [],
            "clients": [sample_client],
            "points": []
        }
        servico = PointsService()
        
        # ACT
        servico.add_points(
            owner_email=sample_points["owner_email"],
            client_cpf=sample_points["client_cpf"],
            to_add_points=100
        )
        
        # ASSERT
        mock_save.assert_called_once()
        db_salvo = mock_save.call_args[0][0]
        assert len(db_salvo["points"]) == 1
        assert db_salvo["points"][0]["points"] == 100

    @patch('services.points_service.load_db')
    @patch('services.points_service.save_db')
    def test_adicionar_pontos_cliente_inexistente(self, mock_save, mock_load):
        """Deve falhar ao adicionar pontos para cliente inexistente"""
        # ARRANGE
        mock_load.return_value = {
            "users": [],
            "clients": [],
            "points": []
        }
        servico = PointsService()
        
        # ACT & ASSERT
        with pytest.raises(ValueError, match="Cliente não existe"):
            servico.add_points(
                owner_email="loja@example.com",
                client_cpf="22188931696",
                to_add_points=100
            )

    @patch('services.points_service.load_db')
    @patch('services.points_service.save_db')
    def test_adicionar_pontos_cliente_existente(self, mock_save, mock_load, sample_client, sample_points):
        """Deve adicionar pontos a registro existente"""
        # ARRANGE
        mock_load.return_value = {
            "users": [],
            "clients": [sample_client],
            "points": [sample_points]
        }
        servico = PointsService()
        
        # ACT
        servico.add_points(
            owner_email=sample_points["owner_email"],
            client_cpf=sample_points["client_cpf"],
            to_add_points=50
        )
        
        # ASSERT
        mock_save.assert_called_once()
        db_salvo = mock_save.call_args[0][0]
        assert db_salvo["points"][0]["points"] == 150  # 100 + 50

    @patch('services.points_service.load_db')
    @patch('services.points_service.save_db')
    def test_remover_pontos(self, mock_save, mock_load, sample_client, sample_points):
        """Deve remover pontos de cliente"""
        # ARRANGE
        mock_load.return_value = {
            "users": [],
            "clients": [sample_client],
            "points": [sample_points]
        }
        servico = PointsService()
        
        # ACT
        servico.remove_points(
            owner_email=sample_points["owner_email"],
            client_cpf=sample_points["client_cpf"],
            to_remove_points=30
        )
        
        # ASSERT
        mock_save.assert_called_once()
        db_salvo = mock_save.call_args[0][0]
        assert db_salvo["points"][0]["points"] == 70  # 100 - 30

    @patch('services.points_service.load_db')
    def test_listar_pontos_estabelecimento(self, mock_load, sample_points):
        """Deve listar apenas pontos do estabelecimento"""
        # ARRANGE
        outro_pontos = {
            "owner_email": "outra_loja@example.com",
            "client_cpf": "98765432101",
            "points": 50
        }
        mock_load.return_value = {
            "users": [],
            "clients": [],
            "points": [sample_points, outro_pontos]
        }
        servico = PointsService()
        
        # ACT
        pontos = servico.list_points(owner_email=sample_points["owner_email"])
        
        # ASSERT
        assert len(pontos) == 1
        assert pontos[0]["owner_email"] == sample_points["owner_email"]
