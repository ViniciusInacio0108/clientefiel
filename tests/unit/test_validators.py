"""
Testes unitários para o módulo de validadores.
Cobre validação de email, senha, nome e CPF com casos de sucesso, falha e edge cases.
"""

import pytest
from utils.validators import (
    is_valid_email,
    assert_password_strength,
    normalize_name,
    normalize_cpf
)


class TestEmailValidation:
    """Testes para validação de email"""

    def test_email_valido(self):
        """ARRANGE-ACT-ASSERT: Email válido deve retornar True"""
        # ARRANGE
        email = "usuario@example.com"
        
        # ACT
        resultado = is_valid_email(email)
        
        # ASSERT
        assert resultado is True

    def test_email_sem_arroba(self):
        """Testa email sem símbolo @"""
        # ARRANGE
        email = "usuarioexample.com"
        
        # ACT
        resultado = is_valid_email(email)
        
        # ASSERT
        assert resultado is False

    def test_email_vazio(self):
        """Testa email vazio (edge case)"""
        # ARRANGE
        email = ""
        
        # ACT
        resultado = is_valid_email(email)
        
        # ASSERT
        assert resultado is False

    def test_email_none(self):
        """Testa email None (edge case)"""
        # ARRANGE
        email = None
        
        # ACT
        resultado = is_valid_email(email)
        
        # ASSERT
        assert resultado is False

    def test_email_com_espaco(self):
        """Testa email com espaço (caso de falha)"""
        # ARRANGE
        email = "usuario @example.com"
        
        # ACT
        resultado = is_valid_email(email)
        
        # ASSERT
        assert resultado is False


class TestPasswordValidation:
    """Testes para validação de força de senha"""

    def test_senha_valida(self):
        """Senha com 6+ caracteres deve passar"""
        # ARRANGE
        senha = "SenhaSegura123!"
        
        # ACT & ASSERT - não deve lançar exceção
        assert_password_strength(senha)

    def test_senha_muito_curta(self):
        """Senha com menos de 6 caracteres deve falhar"""
        # ARRANGE
        senha = "123"
        
        # ACT & ASSERT
        with pytest.raises(ValueError, match="Senha deve ter pelo menos 6 caracteres"):
            assert_password_strength(senha)

    def test_senha_exatamente_6_caracteres(self):
        """Senha com exatamente 6 caracteres deve passar"""
        # ARRANGE
        senha = "123456"
        
        # ACT & ASSERT - não deve lançar exceção
        assert_password_strength(senha)

    def test_senha_vazia(self):
        """Senha vazia deve falhar"""
        # ARRANGE
        senha = ""
        
        # ACT & ASSERT
        with pytest.raises(ValueError):
            assert_password_strength(senha)

    def test_senha_none(self):
        """Senha None deve falhar"""
        # ARRANGE
        senha = None
        
        # ACT & ASSERT
        with pytest.raises(ValueError):
            assert_password_strength(senha)


class TestNameNormalization:
    """Testes para normalização de nomes"""

    def test_nome_valido(self):
        """Nome válido deve ser normalizado com capitalize"""
        # ARRANGE
        nome = "joao silva"
        
        # ACT
        resultado = normalize_name(nome)
        
        # ASSERT
        assert resultado == "Joao Silva"

    def test_nome_com_multiplos_espacos(self):
        """Nome com múltiplos espaços deve ser normalizado"""
        # ARRANGE
        nome = "  joao    silva  "
        
        # ACT
        resultado = normalize_name(nome)
        
        # ASSERT
        assert resultado == "Joao Silva"

    def test_nome_muito_curto(self):
        """Nome com menos de 2 caracteres deve falhar"""
        # ARRANGE
        nome = "J"
        
        # ACT & ASSERT
        with pytest.raises(ValueError, match="Nome inválido"):
            normalize_name(nome)

    def test_nome_vazio(self):
        """Nome vazio deve falhar"""
        # ARRANGE
        nome = ""
        
        # ACT & ASSERT
        with pytest.raises(ValueError):
            normalize_name(nome)

    def test_nome_apenas_espacos(self):
        """Nome com apenas espaços deve falhar"""
        # ARRANGE
        nome = "   "
        
        # ACT & ASSERT
        with pytest.raises(ValueError):
            normalize_name(nome)


class TestCPFNormalization:
    """Testes para normalização de CPF"""

    def test_cpf_valido(self):
        """CPF válido com 11 dígitos deve ser normalizado"""
        # ARRANGE
        cpf = "123.456.789-01"
        
        # ACT
        resultado = normalize_cpf(cpf)
        
        # ASSERT
        assert resultado == "12345678901"

    def test_cpf_com_apenas_digitos(self):
        """CPF com apenas dígitos deve passar"""
        # ARRANGE
        cpf = "12345678901"
        
        # ACT
        resultado = normalize_cpf(cpf)
        
        # ASSERT
        assert resultado == "12345678901"

    def test_cpf_com_poucos_digitos(self):
        """CPF com menos de 11 dígitos deve falhar"""
        # ARRANGE
        cpf = "123.456.789"
        
        # ACT & ASSERT
        with pytest.raises(ValueError, match="CPF deve conter 11 dígitos"):
            normalize_cpf(cpf)

    def test_cpf_vazio(self):
        """CPF vazio deve falhar"""
        # ARRANGE
        cpf = ""
        
        # ACT & ASSERT
        with pytest.raises(ValueError):
            normalize_cpf(cpf)

    def test_cpf_none(self):
        """CPF None deve falhar"""
        # ARRANGE
        cpf = None
        
        # ACT & ASSERT
        with pytest.raises(ValueError):
            normalize_cpf(cpf)
