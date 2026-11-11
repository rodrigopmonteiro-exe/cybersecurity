````markdown
# AULA 13 — RASTREAMENTO MANUAL DE ALGORITMOS (DRY RUN)

## PARTE 1 — TEORIA

### 1. O que é rastreamento manual?

É o processo de acompanhar a execução de um programa, instrução por instrução, observando os valores das variáveis ao longo do código.

Em vez de deixar o Python executar o programa, você acompanha manualmente o que acontece em cada linha.

### 2. Dry Run (execução a seco)

É a técnica utilizada para simular mentalmente ou no papel a execução de um algoritmo, sem executá-lo no computador.

O objetivo é verificar se o raciocínio funciona conforme o esperado.

### 3. Diferença entre rastreamento manual e Dry Run

- Rastreamento manual: acompanha os valores das variáveis e as instruções executadas.
- Dry Run: simula o algoritmo inteiro, verificando seu fluxo e comportamento.

Os dois conceitos são muito próximos e frequentemente utilizados juntos.

### 4. Estado de uma variável

É o valor que uma variável possui em determinado momento durante a execução de um programa.

Uma variável pode mudar de estado quando recebe um novo valor.

### 5. Sequência de execução

É a ordem em que as instruções de um programa são executadas.

Normalmente, o código é executado de cima para baixo, respeitando as estruturas de decisão, repetição e chamadas de funções.

### 6. Erro lógico

Acontece quando o código é executado normalmente, mas o resultado não corresponde ao objetivo do programa.

O computador executa as instruções recebidas. Cabe ao programador verificar se a lógica está correta.

### 7. Três categorias de erros

1. Erro de sintaxe: acontece quando o código é escrito de maneira incorreta.
2. Erro de execução: acontece durante a execução do programa, como uma divisão por zero.
3. Erro lógico: acontece quando o programa executa, mas apresenta um resultado incorreto.

---

## PARTE 2 — TABELA DE RASTREAMENTO

### O que é uma tabela de rastreamento?

Em inglês, chamada de Trace Table, é uma ferramenta utilizada para acompanhar passo a passo as alterações das variáveis durante a execução de um algoritmo.

Ela permite identificar:

- O valor de cada variável em determinado momento.
- A ordem de execução das instruções.
- O resultado das operações.
- Quais condições são verdadeiras ou falsas.
- Como o programa chega ao resultado final.

### Como construir uma tabela de rastreamento?

| Etapa | Instrução executada | Variável | Valor | Observação |
|---|---|---|---|---|
| 1 | Inicialização | x | 10 | Valor inicial |
| 2 | Operação | x | 15 | Novo valor |
| 3 | Operação | x | 20 | Valor atualizado |

### Por que utilizar uma tabela de rastreamento?

- Facilita a compreensão do funcionamento de um algoritmo.
- Ajuda a encontrar erros lógicos.
- Permite acompanhar mudanças nas variáveis.
- Desenvolve o raciocínio computacional.
- Prepara para trabalhar com condições, repetições e funções.

---

## PARTE 3 — PRÁTICA DE RASTREAMENTO

### Exercício A — Acompanhando variáveis

Analise o código:

```python
x = 4
y = 6
z = x * y

y = 10

print(x)
print(y)
print(z)
```

### Rastreamento manual

| Etapa | Instrução | x | y | z |
|---|---|---|---|---|
| 1 | x = 4 | 4 | - | - |
| 2 | y = 6 | 4 | 6 | - |
| 3 | z = x * y | 4 | 6 | 24 |
| 4 | y = 10 | 4 | 10 | 24 |

### Resultado esperado

```text
4
10
24
```

### Observação importante

Quando `y` recebe o valor 10, a variável `z` continua valendo 24.

Isso acontece porque `z` recebeu o resultado da multiplicação no momento em que a instrução foi executada. O Python não recalcula automaticamente uma variável quando outra muda.

### Exercício B — Atualização de variáveis

Analise o código:

```python
a = 10
b = 2

a = a + b
b = a * 2

print(a)
print(b)
```

### Rastreamento manual

| Etapa | Instrução | a | b |
|---|---|---|---|
| 1 | a = 10 | 10 | - |
| 2 | b = 2 | 10 | 2 |
| 3 | a = a + b | 12 | 2 |
| 4 | b = a * 2 | 12 | 24 |

### Resultado esperado

```text
12
24
```

### Observação importante

Na instrução `a = a + b`, o Python utiliza os valores atuais de `a` e `b`, calcula a soma e armazena o resultado novamente em `a`.

Na instrução seguinte, utiliza o novo valor de `a` para calcular `b`.

---

## PARTE 4 — EXERCÍCIOS E RESOLUÇÕES

### Exercício 1

O que significa Dry Run?

**Resposta:** É simular a execução de um algoritmo mentalmente ou no papel, sem executá-lo no computador.

### Exercício 2

Por que acompanhar as variáveis durante a execução de um programa?

**Resposta:** Para entender como os valores mudam, acompanhar a sequência de execução e identificar possíveis erros lógicos.

### Exercício 3

Qual é a diferença entre erro de sintaxe e erro lógico?

**Resposta:**

- Erro de sintaxe: o código apresenta uma construção incorreta e pode impedir sua execução.
- Erro lógico: o código executa, mas produz um resultado diferente do esperado.

### Exercício 4

Qual será a saída do código do Exercício A?

**Resposta:**

```text
4
10
24
```

### Exercício 5

Qual será a saída do código do Exercício B?

**Resposta:**

```text
12
24
```

### Exercício 6 — Identificando um erro lógico

Analise o código:

```python
preco = 100
desconto = 20

total = preco + desconto

print(total)
```

**Pergunta:** Existe algum erro lógico?

**Resposta:** Sim. O programa está somando o desconto ao preço, quando deveria subtraí-lo.

O resultado esperado é 80, mas o programa apresenta 120.

### Exercício 7 — Corrigindo o erro lógico

Código corrigido:

```python
preco = 100
desconto = 20

total = preco - desconto

print(total)
```

**Resultado esperado:**

```text
80
```

---

## PARTE 5 — TECHNICAL ENGLISH

### Vocabulário técnico

| Inglês | Português |
|---|---|
| Debugging | Depuração |
| Variable | Variável |
| Execution | Execução |
| Trace | Rastrear |
| Bug | Defeito ou erro |
| Expected result | Resultado esperado |

### Atividade de inglês técnico

**Texto em inglês:**

Tracing a program's execution means following the code step by step as it runs. During the process, we observe changes in variable values and check which instructions are executed. This helps us identify logical errors, understand the program's behavior, and verify whether the result matches the expected result.

### Tradução

Rastrear a execução de um programa significa acompanhar o código passo a passo enquanto ele é executado. Durante o processo, observamos as mudanças nos valores das variáveis e verificamos quais instruções são executadas. Isso nos ajuda a identificar erros lógicos, compreender o comportamento do programa e verificar se o resultado corresponde ao esperado.

### Resposta produzida

Tracing a program's execution means following the code step by step as it runs. During the process, we observe changes in variable values and check which instructions are executed. This helps us identify logical errors, understand the program's behavior, and verify whether the result matches the expected result.

---

## PARTE 6 — LABORATÓRIO PYTHON NO TERMUX

### Objetivo

Criar e executar um programa Python para acompanhar as mudanças de uma variável durante a execução.

### 1. Criar o arquivo

No Termux, execute:

```bash
nano aula13.py
```

### 2. Código do laboratório

```python
numero = 5

print("Valor inicial:", numero)

numero = numero + 3
print("Segundo estado:", numero)

numero = numero * 2
print("Terceiro estado:", numero)

numero = numero - 4
print("Estado final:", numero)
```

### 3. Salvar o arquivo

No Nano:

- Pressione CTRL + O para salvar.
- Pressione ENTER para confirmar.
- Pressione CTRL + X para sair.

### 4. Executar o programa

```bash
python aula13.py
```

### 5. Resultado esperado

```text
Valor inicial: 5
Segundo estado: 8
Terceiro estado: 16
Estado final: 12
```

### 6. Tabela de rastreamento do laboratório

| Etapa | Instrução | Valor de numero |
|---|---|---|
| 1 | numero = 5 | 5 |
| 2 | numero = numero + 3 | 8 |
| 3 | numero = numero * 2 | 16 |
| 4 | numero = numero - 4 | 12 |

### 7. Conclusão do laboratório

O programa demonstrou como uma variável pode receber novos valores durante a execução.

O rastreamento manual permitiu acompanhar cada alteração e compreender a sequência das operações.

---

## RESULTADO FINAL — AVALIAÇÃO DA AULA 13

### Conteúdos estudados

- Rastreamento manual de algoritmos.
- Dry Run.
- Estado de uma variável.
- Sequência de execução.
- Identificação de erros lógicos.
- Categorias de erros em programação.
- Construção de tabelas de rastreamento.
- Atualização de variáveis.
- Depuração e análise de resultados.

### Atividades concluídas

- [x] Parte 1 — Teoria.
- [x] Parte 2 — Tabela de rastreamento.
- [x] Parte 3 — Prática de rastreamento.
- [x] Parte 4 — Exercícios e resoluções.
- [x] Parte 5 — Technical English.
- [x] Parte 6 — Laboratório Python no Termux.

### Avaliação

| Critério | Resultado |
|---|---|
| Compreensão teórica | Aprovado |
| Rastreamento de variáveis | Aprovado |
| Identificação de erros lógicos | Aprovado |
| Resolução dos exercícios | 7/7 |
| Laboratório Python | Concluído |
| Technical English | Aprovado |

### Pontos fortes demonstrados

1. Boa compreensão da atualização de variáveis.
2. Capacidade de acompanhar a sequência de execução.
3. Identificação e correção de erros lógicos.

### Resultado final

**STATUS: APROVADO**

A Aula 13 foi concluída com êxito. Os objetivos de aprendizagem foram alcançados, incluindo a parte teórica, os exercícios, o laboratório prático e o inglês técnico.

