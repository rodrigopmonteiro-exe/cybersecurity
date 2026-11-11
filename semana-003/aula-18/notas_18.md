# FORMAÇÃO COMPLETA EM CIBERSEGURANÇA

# SEMANA 03 — FUNDAMENTOS DE PYTHON

# AULA 18 — CONVERSÃO DE TIPOS DE DADOS

**Data:** 12/11/2026
**Dia:** Quinta-feira
**Carga horária:** 2 horas
**Disciplina:** Fundamentos de Python
**Nível:** Iniciante

---

# 1. OBJETIVOS

Ao final desta aula, você deverá ser capaz de:

- Entender por que precisamos converter tipos.
- Utilizar `int()`, `float()` e `str()`.
- Converter informações recebidas pelo `input()`.
- Evitar erros de operações entre tipos incompatíveis.

---

# 2. CONTEÚDO TEÓRICO

## 2.1. Por que precisamos converter tipos?

Imagine o seguinte programa:

```python
idade = input("Digite sua idade: ")

resultado = idade + 5

print(resultado)
```

Se você digitar 20, ocorrerá um erro.

### Por quê?

Porque `input()` retorna uma string, e o Python não pode somar diretamente uma string com um inteiro.

Para resolver esse problema, precisamos converter o tipo de dado.

## 2.2. Conversão para inteiro — int()

A função `int()` converte um valor para número inteiro.

Exemplo:

```python
idade = int(input("Digite sua idade: "))

resultado = idade + 5

print(resultado)
```

Se o usuário digitar 20, o resultado será:

```text
25
```

Agora o Python consegue realizar a operação matemática porque a idade foi convertida para inteiro.

## 2.3. Conversão para decimal — float()

A função `float()` converte um valor para número decimal.

Exemplo:

```python
preco = float(input("Digite o preço: "))

print(preco)
```

Exemplo de entrada:

```text
9.99
```

Resultado:

```text
9.99
```

**Atenção:** Em Python, utilizamos ponto (`.`) para representar números decimais, não vírgula.

## 2.4. Conversão para texto — str()

A função `str()` converte um valor para texto.

Exemplo:

```python
idade = 25

mensagem = "Minha idade é " + str(idade)

print(mensagem)
```

Resultado:

```text
Minha idade é 25
```

A conversão é necessária porque estamos concatenando um texto com um número.

## 2.5. Conversão para booleano — bool()

A função `bool()` converte um valor para booleano.

Um booleano possui dois valores possíveis:

- True
- False

Exemplo:

```python
ativo = bool(1)

print(ativo)
```

Resultado:

```text
True
```

### Atenção importante

A conversão para booleano exige cuidado.

Por exemplo:

```python
print(bool("False"))
```

Resultado:

```text
True
```

Isso acontece porque `"False"` é uma string que contém texto. Ela não está vazia.

Portanto, uma string não vazia resulta em `True`, mesmo que seu conteúdo seja a palavra `"False"`.

---

# 3. COMPARAÇÃO ENTRE AS FUNÇÕES

| Função | Conversão |
|---|---|
| int() | Para inteiro |
| float() | Para decimal |
| str() | Para texto |
| bool() | Para booleano |

### Resumo

- `int()` transforma valores em números inteiros.
- `float()` transforma valores em números decimais.
- `str()` transforma valores em texto.
- `bool()` transforma valores em booleanos.

---

# 4. PRÁTICA ORIENTADA

## Calculadora de idade

Crie um arquivo chamado `aula04.py`.

### Código:

```python
print("CALCULADORA DE IDADE")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

idade_futura = idade + 10

print("\nRESULTADO")
print("Nome:", nome)
print("Idade atual:", idade)
print("Idade daqui a 10 anos:", idade_futura)
```

### Execução:

No Termux, execute:

```bash
python aula04.py
```

### Objetivos da prática:

- Receber o nome do usuário.
- Receber a idade.
- Converter a idade para inteiro.
- Realizar uma operação matemática.
- Apresentar os resultados.

### Observe:

A variável `nome` recebe uma string.

A variável `idade` recebe um número inteiro por meio de `int()`.

A variável `idade_futura` armazena o resultado de uma operação matemática.

---

# 5. EXERCÍCIOS

## Exercício 1 — Corrija o código

Observe o código:

```python
numero = input("Digite um número: ")

resultado = numero + 10

print(resultado)
```

### Tarefa:

Corrija o programa para que ele consiga realizar a soma corretamente.

Explique por que o código original apresenta erro.

## Exercício 2 — Soma de dois números

Receba dois números inteiros e apresente a soma.

### Requisitos:

- Solicitar o primeiro número.
- Solicitar o segundo número.
- Converter ambos para inteiro.
- Realizar a soma.
- Apresentar o resultado.

## Exercício 3 — Preço de um produto

Receba o preço de um produto e converta para `float`.

### Requisitos:

- Solicitar o preço.
- Converter o valor para decimal.
- Apresentar o preço.
- Apresentar o tipo de dado utilizando `type()`.

## Exercício 4 — Conversão para string

Converta o número 100 para string e apresente seu tipo.

### Requisitos:

- Criar uma variável com o número 100.
- Converter utilizando `str()`.
- Apresentar o resultado.
- Apresentar o tipo utilizando `type()`.

## Exercício 5 — Diferença entre conversões

Explique a diferença entre os dois códigos:

### Código A:

```python
numero = int(input("Número: "))
```

### Código B:

```python
numero = input("Número: ")
```

### Tarefa:

Explique:

1. Qual código converte a entrada para inteiro?
2. Qual código mantém a entrada como string?
3. Por que essa diferença é importante?

---

# 6. DESAFIO — CALCULADORA DE MÉDIA

Crie um programa que:

1. Solicite o nome do estudante.
2. Solicite três notas.
3. Converta as notas para `float`.
4. Calcule a média.
5. Apresente o nome e a média


**Importante:** Ainda não precisa utilizar estruturas condicionais.

---

# 7. TECHNICAL ENGLISH

## 7.1. Vocabulário técnico

| Inglês | Português |
|---|---|
| Type conversion | Conversão de tipos |
| Casting | Conversão |
| Integer conversion | Conversão para inteiro |
| Decimal number | Número decimal |
| Invalid input | Entrada inválida |

## 7.2. Tradução

Traduza as seguintes frases:

1. Type conversion changes the data type.
2. Input returns a string.
3. We use int to convert a value into an integer.

### Objetivo:

Compreender o vocabulário técnico relacionado à conversão de tipos de dados em Python.

---

# 8. REVISÃO FINAL

Antes de encerrar a aula, revise os seguintes conceitos:

- [ ] Entendo por que precisamos converter tipos.
- [ ] Sei utilizar `int()`.
- [ ] Sei utilizar `float()`.
- [ ] Sei utilizar `str()`.
- [ ] Conheço a função `bool()`.
- [ ] Sei converter informações recebidas pelo `input()`.
- [ ] Consigo realizar operações matemáticas com valores convertidos.
- [ ] Consigo identificar tipos utilizando `type()`.
- [ ] Entendo os erros provocados por tipos incompatíveis.

---

# 9. CRITÉRIOS DE AVALIAÇÃO

| Atividade | Peso |
|---|---:|
| Exercício 1 | 10 pontos |
| Exercício 2 | 10 pontos |
| Exercício 3 | 10 pontos |
| Exercício 4 | 10 pontos |
| Exercício 5 | 10 pontos |
| Desafio — Calculadora de média | 10 pontos |
| Technical English | 10 pontos |

**Critérios complementares:**

- Organização e legibilidade do código.
- Correção das conversões.
- Execução dos programas no Termux.
- Capacidade de explicar os resultados.
- Autonomia na resolução dos problemas.

---

# 10. EVIDÊNCIAS DE CONCLUSÃO

Ao terminar a aula, registre:

1. Anotações teóricas.
2. Respostas dos cinco exercícios.
3. Código da prática orientada.
4. Código do desafio.
5. Capturas de tela das execuções no Termux.
6. Atividade de Technical English.


---

# ENCERRAMENTO DA AULA 18

**Disciplina:** Fundamentos de Python

**Tema:** Conversão de tipos de dados.

**Carga horária:** 2 horas.

**Status:** Aguardando execução das atividades e avaliação.


---

# FORMAÇÃO COMPLETA EM CIBERSEGURANÇA

**SEMANA 03 — FUNDAMENTOS DE PYTHON**

**AULA 18 — CONVERSÃO DE TIPOS DE DADOS**
