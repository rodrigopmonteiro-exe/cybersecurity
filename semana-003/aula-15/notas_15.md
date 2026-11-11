# AULA 15 — SEGUNDA-FEIRA, 09/11/2026

**Formação:** Cibersegurança  
**Disciplina:** Fundamentos de Python  
**Tema:** Atribuição e variáveis em Python  
**Nível:** Iniciante  
**Carga horária:** 2 horas

---

## 1. OBJETIVOS

- Entender o operador de atribuição `=`.
- Criar variáveis.
- Alterar valores armazenados.
- Compreender a diferença entre atribuição e comparação.
- Aplicar variáveis em pequenos programas.

---

## 2. CONTEÚDO TEÓRICO

### O que é atribuição?

Atribuição é o processo de associar um valor a uma variável.

**Exemplo:**

```python
idade = 25
```

Nesse exemplo:

- `idade`: nome da variável.
- `=`: operador de atribuição.
- `25`: valor atribuído.

**Importante:** o sinal `=` não significa igualdade matemática. Em Python, ele atribui um valor.

### Alterando o valor de uma variável

```python
saldo = 100
print(saldo)

saldo = 250
print(saldo)
```

**Resultado:**

```text
100
250
```

A variável passou a armazenar outro valor.

### Atribuição com operações

```python
numero = 10
numero = numero + 5

print(numero)
```

**Resultado:**

```text
15
```

Python também permite:

```python
numero += 5
numero -= 2
numero *= 3
numero /= 2
```

---

## 3. REGRAS PARA NOMEAR VARIÁVEIS

| Correto | Incorreto |
|---|---|
| idade = 25 | 25idade = 25 |
| nome = "Ana" | nome completo = "Ana" |
| saldo_bancario = 100 | saldo-bancario = 100 |
| total = 50 | class = 50 |

---

## 4. PRÁTICA ORIENTADA

### Execute no Termux:

```bash
mkdir -p ~/semana03
cd ~/semana03
nano aula15.py
```

### Digite:

```python
nome = "Carlos"
idade = 30
altura = 1.75
estudando = True

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Estudando:", estudando)
```

### Execute:

```bash
python aula15.py
```

---

## 5. EXERCÍCIOS

### Exercício 1

Crie cinco variáveis diferentes:

- Nome.
- Idade.
- Cidade.
- Altura.
- Estudante.

Apresente todas utilizando `print()`.

### Exercício 2

Crie uma variável chamada `saldo`, atribua 500 e depois acrescente 150.

### Exercício 3

Crie uma variável chamada `pontuacao`, atribua 10 e realize:

- Acrescente 5.
- Subtraia 3.
- Multiplique por 2.

Qual será o resultado?

### Exercício 4

Explique com suas palavras a diferença entre atribuição e comparação.

---

## 6. DESAFIO

Crie um programa chamado `perfil.py` que armazene informações pessoais fictícias em variáveis e apresente um pequeno perfil organizado.

---

## 7. TECHNICAL ENGLISH

### Vocabulário técnico

| Inglês | Português |
|---|---|
| Variable | Variável |
| Assignment | Atribuição |
| Value | Valor |
| Operator | Operador |
| Store | Armazenar |

### Traduza:

1. A variable stores a value.
2. Assignment uses the equals sign.
3. Python allows changing variable values.

---

**FORMAÇÃO COMPLETA EM CIBERSEGURANÇA**

**SEMANA 03 — FUNDAMENTOS DE PYTHON**

**AULA 15 — 09/11/2026**
