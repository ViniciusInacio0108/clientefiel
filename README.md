# ClienteFiel

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
