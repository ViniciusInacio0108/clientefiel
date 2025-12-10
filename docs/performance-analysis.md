# Análise de performance

## Gargalos Identificados

### 1 - Salvar em memória

As operações eram salvas em memória, podendo causar overflow em casos de muitos dados e também podendo gerar lentidão.

**Otimizações Realizadas**

Foi alterado de memória para um arquivo de dados.

**Tempo de execução**

Baixo em ambas as soluções. Milisegundos em ambos, quase não notável.

**Uso de memória**

O real ganho está aqui. A memória teve uma diminuição enorme de uso para casos com muitos dados salvos e transitados, além dos dados ficarem salvos sem perda de informação após fim de execução.

**Tradeoffs**

Ganho em memória. Porém, leve perda de ms em leitura.

### 2 - Salvar dados como JSON

Os dados salvos no arquivo local, agora são salvos como JSON. Melhorando performance comparado a String.

**Otimizações Realizadas**

Agora os dados são estruturados como JSON, melhorando então a leitura do arquivo e também a transformação do arquivo para uma estrutura de dados no Python. Assim, possibilitando melhor identificação dos itens nas listas, sem necessidade de ler o arquivo linha a linha e iterar.

**Tempo de execução**

O tempo de execução foi melhorado em 70%, de: 40ms para 28ms.

**Uso de memória**

Uso de memória melhorado, já que o arquivo não precisa ser lido e iterado e transformado em lista como antes.

**Tradeoffs**

Ganho de performance claro, e também mais facilidade em lidar com a nova estrutura. Eliminando a necessidade de iterar em um String com padrões diferentes como antes.

**Análise de complexidade**

Com Json, a falta de necessidade de iteração numa String sem padrão, fez com que a nossa complexidade tenha saído de Exponencial para Linear. E em algumas partes, até mesmo O(1).

