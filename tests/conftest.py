import pytest
import json
import os
import sys
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# Adicionar src ao path para importações
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))


@pytest.fixture
def mock_db():
    """Mock do banco de dados com estrutura padrão"""
    return {
        "users": [],
        "clients": [],
        "points": []
    }


@pytest.fixture
def sample_user():
    """Usuário de exemplo para testes"""
    return {
        "name": "João Silva",
        "email": "joao@example.com",
        "password": "SenhaSegura123!"
    }


@pytest.fixture
def sample_client():
    """Cliente de exemplo para testes"""
    return {
        "owner_email": "joao@example.com",
        "name": "Cliente Teste",
        "cpf": "12345678901"
    }


@pytest.fixture
def sample_points():
    """Registro de pontos de exemplo para testes"""
    return {
        "owner_email": "joao@example.com",
        "client_cpf": "12345678901",
        "points": 100
    }


@pytest.fixture
def mock_load_db(mock_db):
    """Mock da função load_db"""
    with patch('storage.db.load_db', return_value=mock_db):
        yield mock_db


@pytest.fixture
def mock_save_db():
    """Mock da função save_db"""
    with patch('storage.db.save_db') as mock:
        yield mock
