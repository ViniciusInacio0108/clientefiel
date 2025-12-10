# Debugging Log

## Bug #1: Emails inválidos sendo permitidos para cadastro

### Identificação
- **Data:** 08-10-2025
- **Reportado por:** Teste automatizado
- **Severidade:** Alta
- **Módulo:** utils/validators.py

### Descrição
Ao realizar algum input que envolvesse a validação do e-mail, o mesmo poderia ser considerado válido mesmo não sendo.

### Reprodução
1. Selecionar a opção de login
2. Digitar e-mail inválido
3. Resultado: e-mail inválido sendo criado/aceito pelo sistema.

### Investigação

**Técnica utilizada:** Teste manual + Breakpoint

**Código problemático:**
```python
def is_valid_email(email: str) -> bool:
    if not email or "@" not in email:
        return False
```

**Causa raíz** 
Falta de Regex validando o e-mail incorreto.

**Código corrigido:**
```python
def is_valid_email(email: str) -> bool:
    if not email or "@" not in email:
        return False
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email) is not None
```

## Bug #2: CPFs inválidos podiam ser cadastrados

### Identificação
- **Data:** 08-12-2025
- **Reportado por:** Teste manual + Breakpoint
- **Severidade:** Alta
- **Módulo:** utils/validators.py

### Descrição
Ao realizar algum input que envolvesse a validação do CPF, o mesmo consideraria válido qualquer set de dígitos com length 11, o que acabava por aceitar CPFs inválidos.

### Reprodução
1. Logar
2. Adicionar cliente
3. Digitar qualquer set de números com 11 dígitos
4. Resultado: cadastrava cliente
5. Resultado esperado: erro por CPF inválido.

### Investigação

**Técnica utilizada:** Testes unitários automatizados

**Código problemático:**
```python
def normalize_cpf(cpf: str) -> str:
    digits = re.sub(r"\D", "", cpf or "")
    if len(digits) != 11:
        raise ValueError("CPF deve conter 11 dígitos.")
    return digits
```

**Causa raíz** 
Falta de validação dos dígitos em relação ao padrão de validação do CPF.

**Código corrigido:**
```python
def normalize_cpf(cpf: str) -> str:
    cpf = re.sub(r"\D", "", cpf or "")

    if len(cpf) != 11:
        raise ValueError("CPF deve conter 11 dígitos.")
    
    soma = 0
    peso = 10 
    
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = soma % 11
    
    dv1_calculado = 0 if resto < 2 else 11 - resto
    
    if dv1_calculado != int(cpf[9]):
        raise ValueError("CPF inválido!")

    soma = 0
    peso = 11
    
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1
        
    resto = soma % 11
    
    dv2_calculado = 0 if resto < 2 else 11 - resto
    
    if dv2_calculado != int(cpf[10]):
        raise ValueError("CPF inválido!")

    return cpf
```

## Bug #3: String ao adicionar pontos (int)

### Identificação
- **Data:** 09-10-2025
- **Reportado por:** Testes automatizados
- **Severidade:** Média
- **Módulo:** controllers/points_controller.py

### Descrição
Ao realizar o troca de valores de pontos cadastrados para o cliente, adição dos mesmo ou remoção, caso seja digitado algum caractere que não seja dígito, um erro genérico é estourado.

### Reprodução
1. Logar
2. Ir no menu de pontos
3. Adicionar ou editar e digitar o valor com um caractere que não seja apenas dígitos
4. Resultado: erro com mensagem clara
5. Resultado esperado: erro com messagem incerta

### Investigação

**Técnica utilizada:** Breakpoint + Logging

**Código problemático:**
```python
def menu(self, owner_email: str):
        while True:
            print("\n--- Pontos & Recompensas ---")
            print("1 - Adicionar pontos")
            print("2 - Ajustar pontos (definir valor)")
            print("3 - Remover pontos")
            print("4 - Listar")
            print("0 - Voltar")
            choosed_option = input("Opção: ").strip()
            try:
                if choosed_option == "1":
                    cpf = input("CPF do cliente: ")
                    to_add_points = int(input("Pontos a adicionar: "))
                    self.service.add_points(owner_email, cpf, to_add_points)
                    print("Pontos adicionados.")
                elif choosed_option == "2":
                    cpf = input("CPF do cliente: ")
                    new_points_value = int(input("Novo total de pontos: "))
                    self.service.set_points(owner_email, cpf, new_points_value)
                    print("Pontos ajustados.")
                elif choosed_option == "3":
                    cpf = input("CPF do cliente: ")
                    to_remove_points = int(input("Pontos a remover: "))
                    self.service.remove_points(owner_email, cpf, to_remove_points)
                    print("Pontos removidos.")
                elif choosed_option == "4":
                    for point in self.service.list_points(owner_email):
                        print(f"- CPF {point['client_cpf']}: {point['points']} ponto(s)")
                elif choosed_option == "0":
                    break
                else:
                    print("Opção inválida.")
            except Exception as e:
                print(f"Erro: {e}")
```

**Causa raíz** 
Adição de try-catch para pegar o erro de inpur e enviar uma mensagem condizente.

**Código corrigido:**
```python
def menu(self, owner_email: str):
        while True:
            print("\n--- Pontos & Recompensas ---")
            print("1 - Adicionar pontos")
            print("2 - Ajustar pontos (definir valor)")
            print("3 - Remover pontos")
            print("4 - Listar")
            print("0 - Voltar")
            choosed_option = input("Opção: ").strip()
            try:
                if choosed_option == "1":
                    cpf = input("CPF do cliente: ")
                    to_add_input = input("Pontos a adicionar: ").strip()
                    try:
                        to_add_points = int(to_add_input)
                    except ValueError:
                        print("Entrada inválida: por favor digite apenas dígitos para os pontos (ex.: 10).")
                        continue
                    self.service.add_points(owner_email, cpf, to_add_points)
                    print("Pontos adicionados.")
                elif choosed_option == "2":
                    cpf = input("CPF do cliente: ")
                    new_points_input = input("Novo total de pontos: ").strip()
                    try:
                        new_points_value = int(new_points_input)
                    except ValueError:
                        print("Entrada inválida: por favor digite apenas dígitos para o novo total de pontos (ex.: 100).")
                        continue
                    self.service.set_points(owner_email, cpf, new_points_value)
                    print("Pontos ajustados.")
                elif choosed_option == "3":
                    cpf = input("CPF do cliente: ")
                    to_remove_input = input("Pontos a remover: ").strip()
                    try:
                        to_remove_points = int(to_remove_input)
                    except ValueError:
                        print("Entrada inválida: por favor digite apenas dígitos para os pontos a remover (ex.: 5).")
                        continue
                    self.service.remove_points(owner_email, cpf, to_remove_points)
                    print("Pontos removidos.")
                elif choosed_option == "4":
                    for point in self.service.list_points(owner_email):
                        print(f"- CPF {point['client_cpf']}: {point['points']} ponto(s)")
                elif choosed_option == "0":
                    break
                else:
                    print("Opção inválida.")
            except Exception as e:
                print(f"Erro: {e}")
```

## Lição aprendida
É preciso sempre cuidar em relação ao inputs dos clientes. Garantindo sempre que os mesmos sejam condizentes com as regras corretas e também que os possíveis edge cases para inputs inesperados sejam bem tratados.