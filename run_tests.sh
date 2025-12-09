#!/bin/bash
# Script para executar testes rapidamente

echo "ClienteFiel - Test Suite"
echo "================================"

# Ativar virtual environment
if [ ! -d "venv" ]; then
    echo "Criando virtual environment..."
    python3 -m venv venv
fi

echo "Ativando virtual environment..."
source venv/bin/activate

# Instalar dependências se necessário
if ! python3 -c "import pytest" 2>/dev/null; then
    echo "Instalando dependências de teste..."
    pip install -q -r requirements-dev.txt
fi

echo ""
echo "Executando testes..."
echo "================================"

# Executar testes com cobertura
pytest tests/unit/ --cov=src --cov-report=html --cov-report=term-missing

echo ""
echo "Testes concluídos!"
echo "================================"
