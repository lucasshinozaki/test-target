# Projeto de Estágio Target - São Paulo

Este repositório contém soluções para exercícios técnicos relacionados ao estágio em São Paulo. Cada exercício está implementado em um arquivo Python separado. Abaixo estão os detalhes e instruções para cada exercício.

## Exercícios

### Exercício 1 - Soma dos Números

**Descrição:**
- Dado o trecho de código:
  ```cpp
  int INDICE = 13, SOMA = 0, K = 0;
  Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
  Imprimir(SOMA);

  Determine o valor da variável `SOMA` ao final do processamento.

**Arquivo:** `ex01.py`

### Exercício 2 - Sequência de Fibonacci

**Descrição:**
- Escreva um programa que, dado um número, calcule se ele pertence à sequência de Fibonacci. A sequência de Fibonacci inicia-se com 0 e 1, e cada número subsequente é a soma dos dois anteriores.

**Arquivo:** `ex02.py`

**Importante:** O número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código.

### Exercício 3 - Faturamento Diário

**Descrição:**
- Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa que:
  - Calcule o menor valor de faturamento ocorrido em um dia do mês.
  - Calcule o maior valor de faturamento ocorrido em um dia do mês.
  - Conte o número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

**Arquivo:** `ex03.py`

**Importante:**
- Os dados de faturamento devem ser lidos de um arquivo JSON ou XML.
- Ignore os dias sem faturamento, como finais de semana e feriados, no cálculo da média.

### Exercício 4 - Percentual de Representação por Estado

**Descrição:**
- Dados os valores de faturamento mensal de uma distribuidora por estado:
  - SP – R$67.836,43
  - RJ – R$36.678,66
  - MG – R$29.229,88
  - ES – R$27.165,48
  - Outros – R$19.849,53
- Escreva um programa que calcule o percentual de representação de cada estado dentro do valor total mensal da distribuidora.

**Arquivo:** `ex04.py`

### Exercício 5 - Inversão de String

**Descrição:**
- Escreva um programa que inverta os caracteres de uma string sem usar funções prontas, como `reverse`.

**Arquivo:** `ex05.py`

**Importante:**
- A string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código.

## Instruções para Execução

1. **Clone o Repositório:**
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Execute os Arquivos:**
   Cada arquivo pode ser executado individualmente usando o Python:
   ```sh
   python ex01.py
   python ex02.py
   python ex03.py
   python ex04.py
   python ex05.py
   ```
