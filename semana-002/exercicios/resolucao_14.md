# AULA 14 — RESPOSTAS TEÓRICAS E PRÁTICAS
## Projeto integrador, revisão e avaliação semanal

**Data:** 08/11/2026
**Projeto:** Sistema de cálculo de desempenho acadêmico
**Ambiente de desenvolvimento:** Termux — Android
**Linguagem:** Python

---

# PARTE 1 — TECHNICAL ENGLISH: AULA 13

## 1. Vocabulário técnico

| Inglês | Português |
|---|---|
| Debugging | Depuração |
| Variable | Variável |
| Execution | Execução |
| Trace | Rastrear |
| Bug | Defeito ou erro |
| Expected result | Resultado esperado |

## 2. Texto em inglês

Tracing a program's execution means following the code step by step as it runs. During the process, we observe changes in variable values and check which instructions are executed. This helps us identify logical errors, understand the program's behavior, and verify whether the result matches the expected result.

## 3. Tradução

Rastrear a execução de um programa significa acompanhar o código passo a passo enquanto ele é executado. Durante o processo, observamos as mudanças nos valores das variáveis e verificamos quais instruções são executadas. Isso nos ajuda a identificar erros lógicos, compreender o comportamento do programa e verificar se o resultado corresponde ao esperado.

## 4. Avaliação

- Vocabulário técnico: correto.
- Compreensão do texto: correta.
- Construção do parágrafo: adequada.
- Uso de termos técnicos: adequado.

**Nota do mentor:** Aprovado.


---


# PARTE 2 — AVALIAÇÃO TEÓRICA: AULA 14

## Questão 1 — O que é um algoritmo?

**Minha resposta:**

É uma sequência organizada, lógica e finita de instruções que devem ser executadas para resolver um problema.

**Avaliação:** Correta.

**Observação do mentor:** Uma boa definição. Você identificou três características essenciais: sequência, lógica e finitude.

## Questão 2 — Quais são os quatro pilares do pensamento computacional?

**Minha resposta:**

Reconhecimento de padrões, abstração, algoritmos e decomposição.

**Avaliação:** Correta.

**Observação do mentor:** Os quatro pilares são:

1. Decomposição.
2. Reconhecimento de padrões.
3. Abstração.
4. Algoritmos.

A ordem não altera a validade da resposta.

## Questão 3 — O que significa IPO?

**Minha resposta:**

Input, Processing e Output.

**Avaliação:** Correta.

**Explicação:**

- Input: entrada de dados.
- Processing: processamento dos dados.
- Output: saída dos resultados.

## Questão 4 — Qual a finalidade da decomposição?

**Minha resposta:**

Dividir um problema complexo em problemas menores e mais fáceis de resolver.

**Avaliação:** Correta.

**Observação do mentor:** Você compreendeu a finalidade da decomposição. Essa técnica permite organizar problemas grandes em tarefas menores e gerenciáveis.

## Questão 5 — O que é pseudocódigo?

**Minha resposta:**

É uma maneira de escrever os passos de um algoritmo usando uma linguagem simples, parecida com português, mas seguindo a lógica de programação.

**Avaliação:** Correta.

**Observação do mentor:** O pseudocódigo permite planejar a solução antes de escrever o programa em uma linguagem de programação.

## Questão 6 — Qual a diferença entre pseudocódigo e Python?

**Minha resposta:**

Pseudocódigo é a representação textual do algoritmo, já o Python é uma linguagem de programação utilizada para implementar um algoritmo.

**Avaliação:** Correta.

**Observação do mentor:**

- Pseudocódigo: representa a lógica da solução.
- Python: permite implementar e executar essa solução.

## Questão 7 — Qual símbolo representa uma decisão em um fluxograma?

**Minha resposta:**

Losango.

**Avaliação:** Correta.

**Observação do mentor:** O losango representa uma decisão ou condição, normalmente com caminhos como SIM e NÃO.

## Questão 8 — O que é Dry Run?

**Minha resposta:**

É a técnica de simular a execução de um algoritmo sem executá-lo realmente.

**Avaliação:** Correta.

**Observação do mentor:** Essa técnica permite acompanhar o funcionamento do algoritmo e identificar possíveis erros antes ou durante a implementação.

## Questão 9 — Qual a diferença entre erro de sintaxe e erro lógico?

**Minha resposta:**

O erro de sintaxe impede que o código seja executado. O erro lógico permite que o código execute, mas produz um resultado incorreto.

**Avaliação:** Correta.

**Observação do mentor:** A distinção está correta. Um erro de sintaxe pode impedir a interpretação do programa; um erro lógico pode passar despercebido porque o programa executa normalmente.

## Questão 10 — Por que testar diferentes cenários é importante?

**Minha resposta:**

Porque permite descobrir se um programa, sistema ou aplicação funciona corretamente em diferentes condições, e não apenas na situação ideal.

Testar diferentes cenários ajuda a:

- Encontrar bugs.
- Verificar limites.
- Identificar vulnerabilidades.
- Validar entradas.
- Garantir confiabilidade.
- Prevenir falhas.

Um programa não deve ser considerado confiável apenas porque funciona quando tudo dá certo. Ele precisa demonstrar que também sabe lidar com situações inesperadas.

**Avaliação:** Correta.

**Observação do mentor:** Excelente resposta. Você relacionou os testes à confiabilidade e à identificação de vulnerabilidades, fazendo uma conexão importante com a cibersegurança.

## Resultado da avaliação teórica

| Questão | Resultado |
|---|---|
| 1 | Correta |
| 2 | Correta |
| 3 | Correta |
| 4 | Correta |
| 5 | Correta |
| 6 | Correta |
| 7 | Correta |
| 8 | Correta |
| 9 | Correta |
| 10 | Correta |

**Nota: 10/10 — 100% de aproveitamento.**

**Status: Aprovado.**


---


# PARTE 3 — PROJETO INTEGRADOR

## Sistema de cálculo de desempenho acadêmico

### Objetivo

Desenvolver um programa que receba os dados de um estudante e calcule sua média final, informando se ele foi aprovado ou reprovado.

### Requisitos

1. Solicitar o nome do estudante.
2. Solicitar três notas.
3. Calcular a média.
4. Apresentar o nome e a média.
5. Informar se o estudante foi aprovado ou reprovado.

**Média mínima para aprovação: 7,0.**

---

## ETAPA A — DECOMPOSIÇÃO

**Minha resolução:**

Dividi o projeto em cinco tarefas:

1. Receber os dados.
2. Processar as notas.
3. Calcular a média.
4. Verificar a condição.
5. Apresentar o resultado.

**Avaliação:** Correta.

**Observação do mentor:** A decomposição está organizada e contempla as etapas necessárias para resolver o problema.

---

## ETAPA B — PSEUDOCÓDIGO

**Minha resolução:**

```text
INÍCIO

Escreva("Digite o nome do estudante:")
Leia(nome)

Escreva("Digite a primeira nota:")
Leia(nota1)

Escreva("Digite a segunda nota:")
Leia(nota2)

Escreva("Digite a terceira nota:")
Leia(nota3)

media <- (nota1 + nota2 + nota3) / 3

Escreva("--------------------------")
Escreva("RESULTADO ACADÊMICO")
Escreva("--------------------------")

Escreva("Estudante:", nome)
Escreva("Média final:", media)

SE media >= 7.0 ENTÃO
Escreva("Situação: Aprovado")
SENÃO
Escreva("Situação: Reprovado")
FIMSE

FIM
```

**Avaliação:** Correta.

**Observação do mentor:** O algoritmo apresenta entrada, processamento, saída e decisão. A lógica corresponde aos requisitos do projeto.

---

## ETAPA C — FLUXOGRAMA

**Minha resolução:**

O fluxograma foi desenhado à mão utilizando:

- Oval para início e fim.
- Paralelogramo para entrada e saída.
- Retângulo para processamento.
- Losango para decisão.

### Correções identificadas pelo mentor

1. O ramo NÃO da decisão precisa apresentar "Reprovado", e não "Aprovado".
2. O fluxograma precisa mostrar a entrada do nome do estudante.
3. O fluxograma precisa mostrar a apresentação do nome e da média.

### Fluxo corrigido

```text
INÍCIO
|
v
Ler nome do estudante
|
v
Ler primeira nota
|
v
Ler segunda nota
|
v
Ler terceira nota
|
v
Calcular a média
|
v
Exibir nome e média
|
v
Média >= 7?
/ \
SIM NÃO
| |
v v
APROVADO REPROVADO
| |
\ /
\ /
FIM
```

**Avaliação:** Aprovado com correções necessárias no desenho original.

---

## ETAPA D — IMPLEMENTAÇÃO EM PYTHON

### Ambiente utilizado

- Sistema: Android.
- Terminal: Termux.
- Editor: Nano.
- Linguagem: Python.
- Diretório: `~/cybersecurity/semana-002`
- Arquivo: `projeto_semana2.py`

### Comando utilizado para executar

```bash
python projeto_semana2.py
```

### Código implementado

```python
print("SISTEMA DE DESEMPENHO ACADEMICO")

nome = input("Nome do aluno: ")

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("==============================")
print(" RESULTADO ACADEMICO ")
print("==============================")

print("Estudante:", nome)
print("Media:", round(media, 2))

if media >= 7.0:
print("Situação: Aprovado")
else:
print("Situação: Reprovado")
```

### Avaliação da implementação

- Solicitação do nome: correta.
- Entrada das três notas: correta.
- Conversão para números decimais com `float()`: correta.
- Cálculo da média: correto.
- Apresentação do nome e da média: correta.
- Condição `if/else`: correta.
- Critério de aprovação: correto.

**Avaliação: Aprovado.**

---

# PARTE 4 — TESTES PRÁTICOS

Foram executados três cenários no Termux.

## Teste 1 — Estudante aprovado

**Entradas:**

```text
Nome do aluno: Rodrigo Monteiro
Primeira nota: 8
Segunda nota: 9
Terceira nota: 10
```

**Resultado obtido:**

```text
RESULTADO ACADEMICO

Estudante: Rodrigo Monteiro
Media: 9.0
Situação: Aprovado
```

**Cálculo:**

```text
(8 + 9 + 10) / 3 = 9
```

**Avaliação:** Correto.

## Teste 2 — Estudante reprovado

**Entradas:**

```text
Nome do aluno: Rodrigo Monteiro
Primeira nota: 5
Segunda nota: 6
Terceira nota: 4
```

**Resultado obtido:**

```text
RESULTADO ACADEMICO

Estudante: Rodrigo Monteiro
Media: 5.0
Situação: Reprovado
```

**Cálculo:**

```text
(5 + 6 + 4) / 3 = 5
```

**Avaliação:** Correto.

## Teste 3 — Média exatamente igual ao mínimo

**Entradas:**

```text
Nome do aluno: Rodrigo Monteiro
Primeira nota: 7
Segunda nota: 7
Terceira nota: 7
```

**Resultado obtido:**

```text
RESULTADO ACADEMICO

Estudante: Rodrigo Monteiro
Media: 7.0
Situação: Aprovado
```

**Cálculo:**

```text
(7 + 7 + 7) / 3 = 7
```

**Avaliação:** Correto.

O terceiro teste confirmou que a condição `media >= 7.0` funciona corretamente, incluindo a média mínima de aprovação.

## Resultado dos testes

| Teste | Notas | Média | Resultado esperado | Resultado obtido |
|---|---|---:|---|---|
| 1 | 8, 9, 10 | 9,0 | Aprovado | Aprovado |
| 2 | 5, 6, 4 | 5,0 | Reprovado | Reprovado |
| 3 | 7, 7, 7 | 7,0 | Aprovado | Aprovado |

**Resultado: 3/3 testes corretos.**

---

# PARTE 5 — RASTREAMENTO MANUAL

Foi realizada uma tabela de rastreamento utilizando o primeiro cenário.

### Dados de entrada

```text
nome = Rodrigo Monteiro
nota1 = 8
nota2 = 9
nota3 = 10
```

### Rastreamento

| Etapa | Instrução | Nome | Nota 1 | Nota 2 | Nota 3 | Média |
|---|---|---|---:|---:|---:|---:|
| 1 | Inicialização | - | - | - | - | - |
| 2 | Receber nome | Rodrigo Monteiro | - | - | - | - |
| 3 | Receber nota 1 | Rodrigo Monteiro | 8 | - | - | - |
| 4 | Receber nota 2 | Rodrigo Monteiro | 8 | 9 | - | - |
| 5 | Receber nota 3 | Rodrigo Monteiro | 8 | 9 | 10 | - |
| 6 | Calcular média | Rodrigo Monteiro | 8 | 9 | 10 | 9 |
| 7 | Verificar condição | Rodrigo Monteiro | 8 | 9 | 10 | 9 |
| 8 | Apresentar resultado | Rodrigo Monteiro | 8 | 9 | 10 | 9 |

### Decisão

```python
if media >= 7.0:
print("Situação: Aprovado")
else:
print("Situação: Reprovado")
```

Como a média é 9,0, a condição é verdadeira.

**Resultado: APROVADO.**

**Observação do mentor:** A tabela original registrou corretamente as entradas. A versão acima complementa o rastreamento com a média e o resultado da decisão, deixando a análise mais completa.


---


# PARTE 6 — TECHNICAL ENGLISH: AULA 14

## 1. Texto original

An algorithm is a sequence of instructions designed to solve a problem. It receives input, processes data, and produces output. Programmers use pseudocode and flowcharts to represent algorithms before implementing them in a programming language.

## 2. Minha tradução

Um algoritmo é uma sequência de instruções projetada para resolver um problema. Ele recebe dados de entrada, processa essas informações e produz uma saída. Os programadores utilizam pseudocódigo e fluxogramas para representar algoritmos antes de implementá-los em uma linguagem de programação.

**Avaliação:** Correta.

## 3. Meu parágrafo em inglês

This project is a simple Student Grade Management System developed in Python. It receives three grades from the user, calculates the average, and determines whether the student has passed or failed. The program uses functions, variables, conditional statements, and user input. The main goal is to practice basic programming concepts and develop problem-solving skills.

## 4. Correção técnica

O texto está bem construído. Entretanto, o código desenvolvido não utiliza funções. Por isso, a versão tecnicamente mais precisa é:

```text
This project is a simple Student Grade Management System developed in Python. It receives three grades from the user, calculates the average, and determines whether the student has passed or failed. The program uses variables, conditional statements, arithmetic operations, and user input. The main goal is to practice basic programming concepts and develop problem-solving skills.
```

**Avaliação:** Aprovado, com uma correção de precisão técnica.


---


# PARTE 7 — AVALIAÇÃO FINAL DO MENTOR

## 1. Resultados acadêmicos

| Critério | Resultado |
|---|---|
| Revisão teórica | 10/10 |
| Decomposição | Aprovado |
| Pseudocódigo | Aprovado |
| Fluxograma | Aprovado com correções |
| Implementação Python | Aprovado |
| Testes práticos | 3/3 |
| Rastreamento manual | Aprovado |
| Technical English | Aprovado |

## 2. Competências demonstradas

- Compreensão de algoritmos.
- Pensamento computacional.
- Decomposição de problemas.
- Representação de algoritmos.
- Construção de fluxogramas.
- Programação em Python.
- Utilização de variáveis.
- Operações aritméticas.
- Estruturas condicionais.
- Testes de software.
- Rastreamento manual.
- Inglês técnico.

## 3. Pontos fortes

1. Boa capacidade de organizar um problema em etapas.
2. Compreensão da lógica de programação.
3. Boa execução dos testes práticos.
4. Capacidade de explicar conceitos com suas próprias palavras.
5. Aplicação dos conceitos no ambiente Termux.

## 4. Pontos a melhorar

1. Representar todas as entradas, saídas e decisões nos fluxogramas.
2. Melhorar as tabelas de rastreamento, incluindo variáveis calculadas e resultados das condições.
3. Manter precisão técnica no vocabulário de programação em inglês.
4. Continuar praticando estruturas condicionais e testes com entradas diferentes.

## 5. Parecer final

O projeto integrador foi concluído com sucesso.

O estudante demonstrou capacidade de transformar um problema em uma solução computacional, desde a decomposição até a implementação e os testes.

A solução Python funcionou corretamente nos três cenários apresentados.

A avaliação teórica obteve 10/10, e os testes práticos obtiveram 3/3.

---

# RESULTADO FINAL — AULA 14 E SEMANA 02

**STATUS ACADÊMICO: APROVADO**

| Indicador | Resultado |
|---|---|
| Aula 14 | Aprovada |
| Projeto integrador | Concluído |
| Avaliação teórica | 10/10 |
| Testes práticos | 3/3 |
| Implementação Python | Funcional |
| Evidências | Registradas |
| Semana 02 | Concluída |


**Registro acadêmico:** Semana 02 concluída e aprovada.

