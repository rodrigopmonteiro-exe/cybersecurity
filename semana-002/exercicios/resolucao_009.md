# AULA 09 — MODELO IPO (INPUT, PROCESS, OUTPUT)

**Data:** 03/11/2026
**Duração:** 2 horas
**Disciplina:** Programação
**Ambiente:** Termux (Android)
**Linguagem:** Python
**Tema:** Entrada, processamento e saída de dados.

---

# PARTE 1 — TEORIA

## 1. Modelo IPO (Input, Process, Output)

É um modelo fundamental da Ciência da Computação. Ele descreve como um programa recebe dados, realiza operações e apresenta resultados.

### 1.1 Input (Entrada)

É o momento em que o programa recebe informações.

**Exemplos:**

- Nome do usuário.
- Idade.
- Senha.
- Endereço IP.
- Arquivos enviados.

### 1.2 Process (Processamento)

É quando o programa executa operações com os dados recebidos.

**Exemplos:**

- Cálculos matemáticos.
- Comparações.
- Validação de informações.
- Conversão de dados.
- Análise de informações.

### 1.3 Output (Saída)

É o resultado apresentado após o processamento.

**Exemplos:**

- Mensagens na tela.
- Resultados de cálculos.
- Relatórios.
- Alertas de segurança.
- Dados armazenados.

---

## 2. Exemplo prático do modelo IPO

Calcular a média de duas notas.

| Etapa | Operação |
|---|---|
| Entrada | Receber nota 1 e nota 2 |
| Processamento | Somar as notas e dividir por 2 |
| Saída | Apresentar a média |

### Fórmula

M = (N1 + N2) / 2

Onde:

- M = Média.
- N1 = Primeira nota.
- N2 = Segunda nota.

---

# PARTE 2 — CONSTRUÇÃO DE ALGORITMOS

## 1. Análise de três situações

### Situação 1 — Calcular a idade de uma pessoa a partir do ano de nascimento

**Entrada:**
- Ano de nascimento.
- Ano atual.

**Processamento:**
- Ano atual - Ano de nascimento.

**Saída:**
- Idade calculada em anos.

### Situação 2 — Converter quilômetros em metros

**Entrada:**
- Distância em quilômetros.

**Processamento:**
- Km x 1000.

**Saída:**
- Distância convertida em metros.

### Situação 3 — Calcular o valor de uma compra com quantidade e preço unitário

**Entrada:**
- Quantidade de produtos.
- Preço unitário.

**Processamento:**
- Quantidade x Preço unitário.

**Saída:**
- Valor total da compra.

---

# PARTE 3 — EXERCÍCIOS

## Exercício 1 — Identifique o IPO de uma calculadora

### Entrada (Input)

São os dados fornecidos pelo usuário:

- Primeiro número.
- Segundo número.
- Operação matemática desejada.

### Processamento (Processing)

São os cálculos realizados pela calculadora:

- Recebe os dois números.
- Identifica a operação solicitada.
- Executa o cálculo matemático correspondente.

### Saída (Output)

É o resultado apresentado ao usuário:

- Resultado da operação matemática.

---

## Exercício 2 — Identifique o IPO de um sistema de login

### Input

- Nome de usuário ou e-mail.
- Senha.

### Processing

O sistema realiza as seguintes operações:

1. Recebe o nome de usuário e o e-mail.
2. Verifica se os campos foram preenchidos.
3. Consulta o cadastro do usuário.
4. Compara a senha informada com a senha armazenada na base de dados.
5. Verifica se as credenciais são válidas.

### Output

É o resultado apresentado pelo sistema:

- Login bem-sucedido: acesso autorizado.
- Login malsucedido: mensagem de erro, como "Usuário ou senha incorretos".
- Campos vazios: solicitação para preencher os campos.

---

## Exercício 3 — Identifique o IPO de um programa que calcula a área de um retângulo

### Input

- Comprimento de um retângulo.
- Largura do retângulo.

### Processing

O programa multiplica o comprimento pela largura.

### Output

- Área do retângulo em unidades quadradas.

---

## Exercício 4 — Identifique o IPO de um programa que converte Celsius para Fahrenheit

### Input

- Temperatura em graus Celsius (°C).

### Processing

Aplicar a seguinte fórmula de conversão:

F = (C x 9 / 5) + 32

Onde:

- C = Temperatura em Celsius.
- F = Temperatura em Fahrenheit.

### Output

- Temperatura convertida em graus Fahrenheit (°F).

---

## Exercício 5 — Explique por que a entrada precisa ser validada

Para garantir que os dados fornecidos pelo usuário sejam consistentes, estejam no formato esperado e possam ser processados pelo programa sem causar erros ou resultados incorretos.

**Importante:** Todo dado externo deve ser tratado como não confiável até sua validação.

---

# PARTE 4 — LABORATÓRIO PYTHON

## 1. Objetivo

Criar um programa em Python que receba o nome de um aluno e duas notas, calcule a média aritmética e apresente o resultado.

## 2. Criar o arquivo

Comando utilizado no Termux:

```bash
nano aula09.py
```

## 3. Código executado

```python
print("CALCULADORA DE MÉDIA")

nome = input("Nome do aluno: ")

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2) / 2

print("\nRESULTADO")
print("Aluno:", nome)
print("Média:", media)
```

## 4. Executar o programa

Comando utilizado:

```bash
python aula09.py
```

---

# PARTE 5 — EVIDÊNCIAS DA EXECUÇÃO

O programa foi executado três vezes no Termux, utilizando diferentes valores de entrada.

## Teste 1

### Entrada

- Nome: Rodrigo Monteiro
- Primeira nota: 9.8
- Segunda nota: 7.5

### Saída

```text
CALCULADORA DE MÉDIA
Nome do aluno: Rodrigo Monteiro
Primeira nota: 9.8
Segunda nota: 7.5

RESULTADO
Aluno: Rodrigo Monteiro
Média: 8.65
```

### Conferência

(9.8 + 7.5) / 2 = 8.65

**Resultado: CORRETO**

---

## Teste 2

### Entrada

- Nome: Rodrigo Monteiro
- Primeira nota: 7.0
- Segunda nota: 5.0

### Saída

```text
CALCULADORA DE MÉDIA
Nome do aluno: Rodrigo Monteiro
Primeira nota: 7.0
Segunda nota: 5.0

RESULTADO
Aluno: Rodrigo Monteiro
Média: 6.0
```

### Conferência

(7.0 + 5.0) / 2 = 6.0

**Resultado: CORRETO**

---

## Teste 3

### Entrada

- Nome: Rodrigo Monteiro
- Primeira nota: 4.0
- Segunda nota: 7.0

### Saída

```text
CALCULADORA DE MÉDIA
Nome do aluno: Rodrigo Monteiro
Primeira nota: 4.0
Segunda nota: 7.0

RESULTADO
Aluno: Rodrigo Monteiro
Média: 5.5
```

### Conferência

(4.0 + 7.0) / 2 = 5.5

**Resultado: CORRETO**

---

## 5. Resumo dos testes

| Teste | Nota 1 | Nota 2 | Média | Resultado |
|---|---:|---:|---:|---|
| 1 | 9.8 | 7.5 | 8.65 | Correto |
| 2 | 7.0 | 5.0 | 6.0 | Correto |
| 3 | 4.0 | 7.0 | 5.5 | Correto |

- Total de testes: 3.
- Testes corretos: 3.
- Testes com erros: 0.
- Taxa de sucesso: 100%.

---

# PARTE 6 — TECHNICAL ENGLISH

## Traduções realizadas

| Inglês | Português |
|---|---|
| Enter your name. | Entre com seu nome. |
| Enter two numbers. | Entre com dois números. |
| Calculate the average. | Calcule a média. |
| Display the result. | Mostre o resultado. |
| The program processes the input data. | O programa processa os dados de entrada. |

**Resultado: 5 de 5 traduções corretas.**

---

# PARTE 7 — OBSERVAÇÕES TÉCNICAS DO PROFESSOR

## 1. Modelo IPO

O modelo IPO é uma estrutura fundamental para compreender o funcionamento de programas e sistemas computacionais.

Sua aplicação também é importante na cibersegurança.

Exemplo:

- Input: dados recebidos por uma aplicação.
- Process: validação e processamento dos dados.
- Output: resposta apresentada ao usuário.

## 2. Segurança de sistemas de login

No exercício sobre autenticação, existe um aprimoramento técnico importante.

Em sistemas reais, as senhas não devem ser armazenadas em texto puro.

O procedimento adequado envolve:

- Armazenamento de hashes de senhas.
- Utilização de algoritmos próprios para armazenamento seguro de senhas, como Argon2id.
- Verificação segura das credenciais.
- Proteção contra tentativas excessivas de autenticação.
- Validação das entradas recebidas.

## 3. Validação de entradas

A validação de entradas é essencial para evitar:

- Erros de processamento.
- Dados inconsistentes.
- Entradas inesperadas.
- Vulnerabilidades decorrentes de dados não confiáveis.

## 4. Melhorias futuras no programa Python

O programa executado apresentou resultados matematicamente corretos.

Entretanto, ainda pode evoluir com:

1. Validação de entradas numéricas.
2. Bloqueio de notas negativas.
3. Limitação das notas ao intervalo de 0 a 10.
4. Tratamento de erros com `try` e `except`.
5. Formatação da média com duas casas decimais.

Essas melhorias são sugestões de evolução, não erros identificados nos testes realizados.

## 5. Observação sobre o cálculo de idade

Para calcular a idade exata de uma pessoa, não basta subtrair o ano de nascimento do ano atual.

Também é necessário verificar se a pessoa já fez aniversário naquele ano.

---

# PARTE 8 — COMPETÊNCIAS DESENVOLVIDAS

- [x] Compreensão do modelo IPO.
- [x] Identificação de entradas, processamentos e saídas.
- [x] Construção de algoritmos.
- [x] Identificação do IPO de uma calculadora.
- [x] Identificação do IPO de um sistema de login.
- [x] Identificação do IPO de um programa de cálculo de área.
- [x] Identificação do IPO de um conversor de temperatura.
- [x] Compreensão da importância da validação de entradas.
- [x] Criação de programa Python.
- [x] Utilização de `input()`.
- [x] Utilização de `float()`.
- [x] Utilização de variáveis.
- [x] Operações matemáticas.
- [x] Utilização de `print()`.
- [x] Execução de programas no Termux.
- [x] Realização de três testes práticos.
- [x] Tradução de cinco expressões técnicas em inglês.

---

# PARTE 9 — AVALIAÇÃO FINAL

| Critério | Status |
|---|---|
| Conteúdo teórico | Aprovado |
| Construção de algoritmos | Aprovado |
| Exercícios conceituais | Aprovado |
| Technical English | Aprovado |
| Laboratório Python | Aprovado |
| Execução dos testes | Aprovado |

## Resultado final

**STATUS: APROVADO**

A avaliação teórica e prática da Aula 09 foi concluída com sucesso.

O estudante demonstrou compreensão do modelo IPO, capacidade de decomposição de problemas, aplicação de operações matemáticas e execução de programas em Python utilizando o Termux.

Foram realizados três testes práticos, todos com resultados corretos.

**Evidência prática:** captura de tela das três execuções do arquivo `aula09.py` no Termux.

---

# REGISTRO ACADÊMICO

**Disciplina:** Programação
**Aula:** 09
**Tema:** Modelo IPO (Input, Process, Output)
**Data:** 03/11/2026
**Ambiente:** Termux / Android
**Linguagem:** Python

**Resultado:** APROVADO
