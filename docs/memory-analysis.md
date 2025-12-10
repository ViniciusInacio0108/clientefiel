# Análise de memória

## Otimizações

### 1 - Evitar o uso de looping em listas de forma pouco performática.

Evitar o uso de Listas quando precisamos de uma acesso mais rápido como O(1), baseando-se na necessidade de uma key específica, como o CPF. Dessa forma, evitamos passar por uma Lista enorma antes de chegar de fato ao item que desejamos, sem a necessidade de verificações.

### 2 - Evitar o uso de sorting pouco performático, que não seja um algoritmo nativo do Python (com complexidade menor possível)

Evitar o uso de algoritmos de sorting menos performáticos e utilizar o padrão do Python, já visando performance.

### 3 - Estruturas de dados condizentes

- Set ao invés de listas para elementos únicos.
- HashMap ao invés de listas, para acessar itens por keys específicas.
- Inteiros com dados Int com uso de memória.