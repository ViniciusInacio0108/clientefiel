# Code Smells Identificados

## 1. Long file
- **Arquivo**: src/main.py
- **Linha**: 46-95
- **Descrição**: Arquivo main contendo muitos métodos que deveriam estar em controllers para cada função
- **Severidade**: Baixa
- **Ferramenta**: pylint
- **Status**: Corrigido em Sprint 1

## 2. Poor naming
- **Arquivos**: src/controllers/client_controller.py
- **Linhas**: 42
- **Descrição**: For loop com index variável de nome ruim
- **Severidade**: Média
- **Status**: Corrigido na Sprint 2

## 3. Long Method
- **Arquivos**: src/services/points_service.py
- **Linhas**: 16-57
- **Descrição**: Métodos muito longos e com validações
- **Severidade**: Alta
- **Status**: Corrigido na Sprint 2