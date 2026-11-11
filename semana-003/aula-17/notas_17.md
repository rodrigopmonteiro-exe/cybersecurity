# AULA 17 — QUARTA-FEIRA, 11/11/2026

**Numeração semanal:** Aula 03
**Formação:** Cibersegurança 
**Disciplina:** Fundamentos de Python 
**Tema:** print(), input() e type() 
**Nível:** Iniciante 
**Carga horária:** 2 horas

---

# 1. OBJETIVOS

- Apresentar informações com `print()`.
- Receber informações com `input()`.
- Identificar tipos de dados com `type()`.
- Compreender o comportamento de `input()`.

---

# 2. CONTEÚDO TEÓRICO

## 2.1. Função print()

Utilizada para apresentar informações na tela.

### Exemplo 1

```python
print("Bem-vindo ao Python!")
```

### Exemplo 2 — Apresentando variáveis

```python
nome = "Carlos"

print(nome)
```

A função `print()` permite apresentar informações armazenadas em variáveis.

---

## 2.2. Função input()

Permite receber informações digitadas pelo usuário.

### Exemplo

```python
nome = input("Digite seu nome: ")

print("Bem-vindo,", nome)
```

### Atenção

`input()` retorna uma string, mesmo quando o usuário digita um número.

### Exemplo

```python
idade = input("Digite sua idade: ")

print(idade)
print(type(idade))
```

Se o usuário digitar 25, o resultado de `type()` será:

```text
<class 'str'>
```

Isso acontece porque o Python recebe inicialmente as informações de `input()` como texto.

---

## 2.3. Função type()

Identifica o tipo de dado de uma informação.

### Exemplo

```python
numero = 100
texto = "Python"
decimal = 10.5
ativo = True

print(type(numero))
print(type(texto))
print(type(decimal))
print(type(ativo))
```

### Resultado esperado

```text
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
```

A função `type()` permite descobrir qual é o tipo de dado armazenado em uma variável.

---

# 3. PRÁTICA ORIENTADA

## 3.1. Criando o arquivo

No Termux, execute:

```bash
mkdir -p ~/semana-003/aula-17
cd ~/semana-003/aula-17
nano aula03.py
```

## 3.2. Digite o código

```python
print("CADASTRO DE ESTUDANTE")

nome = input("Nome: ")
idade = input("Idade: ")
cidade = input("Cidade: ")

print("\nDADOS CADASTRADOS")
print("Nome:", nome)
print("Idade:", idade)
print("Cidade:", cidade)

print("\nTIPOS DOS DADOS")
print(type(nome))
print(type(idade))
print(type(cidade))
```

## 3.3. Executando

```bash
python aula03.py
```

Execute o programa e observe os tipos retornados.

**Atenção:** mesmo que a idade seja digitada como número, ela será recebida como `str`.

---

# 4. EXERCÍCIOS

## Exercício 1

Explique a finalidade de `print()`.

## Exercício 2

Explique a finalidade de `input()`.

## Exercício 3

Qual é o tipo retornado por `input()`?

## Exercício 4

Identifique o resultado:

```python
x = 10
y = "10"

print(type(x))
print(type(y))
```

## Exercício 5

Crie um programa que solicite:

- Nome.
- Idade.
- Profissão.

Depois apresente todas as informações e seus respectivos tipos.

---

# 5. DESAFIO

Crie um sistema de identificação de usuário que receba:

- Nome.
- E-mail.
- Idade.

O programa deverá apresentar os dados cadastrados.

**Utilize somente os conceitos estudados até agora.**

### Orientações

1. Crie as variáveis necessárias.
2. Utilize `input()` para receber as informações.
3. Utilize `print()` para apresentar os dados.
4. Utilize `type()` para identificar os tipos.
5. Execute o programa no Termux.

**Importante:** utilize informações fictícias. Não insira e-mails ou dados pessoais reais no exercício.

---

# 6. TECHNICAL ENGLISH

## 6.1. Vocabulário técnico

| Inglês | Português |
|---|---|
| Input | Entrada |
| Output | Saída |
| Display | Exibir |
| User input | Entrada do usuário |
| Function | Função |

## 6.2. Atividade de tradução

Traduza as frases:

1. The input function receives information.
2. The print function displays information.
3. The type function identifies data types.

---

# 7. ENCERRAMENTO

Ao concluir esta aula, deverei conseguir:

- [ ] Apresentar informações utilizando `print()`.
- [ ] Receber informações utilizando `input()`.
- [ ] Identificar tipos utilizando `type()`.
- [ ] Compreender por que `input()` retorna uma string.
- [ ] Desenvolver um pequeno programa interativo.
- [ ] Resolver os cinco exercícios.
- [ ] Concluir o desafio de identificação de usuário.
- [ ] Realizar a atividade de Technical English.
- [ ] Apresentar evidência prática da execução no Termux.

---

**FORMAÇÃO COMPLETA EM CIBERSEGURANÇA**

**SEMANA 03 — FUNDAMENTOS DE PYTHON**

**AULA 17 — AULA SEMANAL 03**

**DATA: 11/11/2026**
