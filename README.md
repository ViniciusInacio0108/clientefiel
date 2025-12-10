# ClienteFiel

Esse projeto foi realizado pelos discentes: Vinícius Inácio e Adrian Bandeira. Adrian ficou responsável pelo desenvolvimento junto a Vinícius na U1. Para a entrega da U3, os testes foram desenvolvidos por Adrian e as documentações e coverage por Vinícius.

Repositório reestruturado aplicando **código limpo** e **separação de responsabilidades**:
- `models/` — entidades de domínio (User, Client, Points)
- `services/` — regras de negócio e validações
- `controllers/` — interação CLI (I/O) e orquestração de serviços
- `storage/` — persistência simples em JSON (sem dependências externas)
- `utils/` — utilitários (validação e helpers)

## Como rodar

Na raíz do projeto rode:

```bash
cd src
python -m main
```

ou 

```bash
cd src
python3 -m main
```

Os dados são salvos em `storage/data.json`.

# Testes

## Dependências de Teste

As seguintes dependências foram instaladas:

```
pytest==7.4.3
pytest-cov==4.1.0
pytest-mock==3.12.0
```

Instalar com: `pip install -r requirements-dev.txt`

## Padrão FIRST

A suite segue rigorosamente os princípios FIRST:

### **Fast** (Rápido)
- Tempo total de execução: **~0.10 segundos** (bem abaixo do limite de 30s)
- Testes executam sem I/O real (uso de mocks)

### **Independent** (Independentes)
- Cada teste é isolado com suas próprias fixtures
- Nenhuma dependência entre testes
- Mocks garantem que testes não afetam uns aos outros

### **Repeatable** (Repetíveis)
- Resultados sempre consistentes
- Sem efeitos colaterais
- Fixtures regeneradas para cada teste

### **Self-validating** (Auto-validáveis)
- Todos os testes têm resultado claro: PASS ou FAIL
- Não requer verificação manual
- Assertions descritivas

### **Timely** (Oportunos)
- Testes criados junto com o código
- Cobrem funcionalidades principais
- Incluem casos de sucesso, falha e edge cases

## Como Executar

### Apenas para Linux Based (Linux e MacOS)
Pode ser executado o script run_tests.sh com a configuração completa do ambiente + tests + coverage com o comando (no root do projeto):

```bash
./run_tests.sh
```

Ou pode ser feito passo a passo com o seguinte setup (Todos sistemas):

```bash
# Criar virtual environment
python3 -m venv venv

# Ativar virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements-dev.txt
```

### Executar Todos os Testes

```bash
pytest tests/unit/ -v
```

### Executar Teste Específico

```bash
# Exemplo
pytest tests/unit/test_validators.py -v
```

### Gerar Relatório de Cobertura

```bash
pytest tests/unit/ --cov=src --cov-report=html --cov-report=term-missing
```

Relatório HTML gerado em `htmlcov/index.html`

## Referências

- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [Padrão AAA](https://betterprogramming.pub/arrange-act-assert-rethinking-unit-test-structure-6b33a27e2e37)
- [Princípios FIRST](https://github.com/ghsukumar/SFDC_Best_Practices/wiki/F.I.R.S.T-Principles-of-Good-Unit-Tests)

---