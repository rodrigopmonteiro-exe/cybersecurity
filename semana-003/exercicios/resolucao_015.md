# FORMAÇÃO COMPLETA EM CIBERSEGURANÇA

# SEMANA 03 — FUNDAMENTOS DE PYTHON

# AULA 15 — ATRIBUIÇÃO E VARIÁVEIS EM PYTHON

**Data:** 09/11/2026  
**Carga horária:** 2 horas  
**Nível:** Iniciante  
**Status:** APROVADO

---

# 1. REGISTRO DAS ANOTAÇÕES TEÓRICAS

## 1.1. O que é uma variável?

Uma variável é o nome associado a um valor que pode ser utilizado e, quando necessário, atualizado durante a execução de um programa.

**Atenção:** Em Python, não precisamos declarar previamente o tipo da variável. Ele é determinado a partir do valor atribuído.

### Exemplos:

```python
nome = "Rodrigo"
idade = 44
altura = 1.78
estudando = True
```

Podemos verificar os tipos primitivos utilizando `type()`:

```python
print(type(nome))
print(type(idade))
```

**Resultados:**

```text
<class 'str'>
<class 'int'>
```

## 1.2. Conceito importante

Uma variável não é o valor em si. Ela é um identificador associado a esse valor.

## 1.3. Operador de atribuição

O símbolo `=` significa que estamos atribuindo um valor a uma variável.

### Exemplo:

```python
saldo = 500

print(saldo)
```

Ao executar, o valor 500 é atribuído à variável `saldo`.

## 1.4. Atribuindo uma variável a outra

Também podemos utilizar uma variável para atribuir um valor a outra.

```python
a = 10
b = a

print(a)
print(b)
```

**Resultado:**

```text
10
10
```

## 1.5. Atribuição com operações

```python
numero = 10
resultado = numero + 5

print(resultado)
```

**Resultado:**

```text
15
```

## 1.6. Operadores de atribuição combinada

Python permite escrever operações de maneira abreviada.

| Operador | Significado |
|---|---|
| `+=` | Soma e atribui |
| `-=` | Subtrai e atribui |
| `*=` | Multiplica e atribui |
| `/=` | Divide e atribui |

### Exemplo:

```python
numero = 10

numero += 5

print(numero)
```

**Equivale a:**

```python
numero = numero + 5
```

**Resultado:**

```text
15
```

## 1.7. Diferença entre atribuição e comparação

- `=`: modifica ou estabelece o valor associado a uma variável.
- `==`: verifica uma condição de igualdade e retorna um resultado booleano: `True` ou `False`.

### Exemplo:

```python
idade = 18

print(idade == 18)
```

**Resultado:**

```text
True
```

---

# 2. RESPOSTAS DOS EXERCÍCIOS

## Exercício 1 — Criando cinco variáveis

**Enunciado:** Criar cinco variáveis diferentes: nome, idade, cidade, altura e estudante. Apresentar todas utilizando `print()`.

### Minha resolução:

```python
nome = "Rodrigo"
idade = 44
cidade = "maceio"
altura = 1.78
estudante = True

print(nome)
print(idade)
print(Cidade)
print(Altura)
print(Estudante)
```

### Avaliação:

As cinco variáveis foram criadas corretamente.

Entretanto, foram identificadas inconsistências nos comandos `print()`:

- `Cidade` deveria ser `cidade`.
- `Altura` deveria ser `altura`.
- `Estudante` deveria ser `estudante`.

Python diferencia letras maiúsculas de minúsculas.

### Correção:

```python
nome = "Rodrigo"
idade = 44
cidade = "Maceió"
altura = 1.78
estudante = True

print(nome)
print(idade)
print(cidade)
print(altura)
print(estudante)
```

**Nota: 8,0/10**

---

## Exercício 2 — Alterando valores

**Enunciado:** Criar uma variável chamada `saldo`, atribuir 500 e depois acrescentar 150.

### Minha resolução:

```python
saldo = 500
saldo = saldo + 150

print(saldo)
```

### Resultado:

```text
650
```

### Avaliação:

Resposta correta.

Demonstrei compreender como atualizar o valor armazenado em uma variável utilizando uma operação matemática.

**Nota: 10/10**

---

## Exercício 3 — Operações com atribuição

**Enunciado:** Criar uma variável chamada `pontuacao`, atribuir 10 e realizar:

- Acrescentar 5.
- Subtrair 3.
- Multiplicar por 2.

### Minha resolução:

```python
pontuacao = 10

pontuacao += 5
pontuacao -= 3
pontuacao *= 2

print(pontuacao)
```

### Cálculo:

| Operação | Resultado |
|---|---:|
| Valor inicial | 10 |
| Acrescentar 5 | 15 |
| Subtrair 3 | 12 |
| Multiplicar por 2 | 24 |

### Resultado:

```text
24
```

### Avaliação:

Resposta correta.

Demonstrei compreender os operadores de atribuição combinada.

**Nota: 10/10**

---

## Exercício 4 — Atribuição versus comparação

**Enunciado:** Explicar com minhas palavras a diferença entre atribuição e comparação.

### Minha resposta:

- Atribuição: estabelece ou modifica o valor associado a uma variável.
- Comparação: verifica uma condição e retorna `True` ou `False`.

### Avaliação:

Resposta correta.

Demonstrei compreender a diferença entre os operadores `=` e `==`.

**Nota: 10/10**

---

# 3. TECHNICAL ENGLISH

## 3.1. Vocabulário técnico

| Inglês | Português |
|---|---|
| Variable | Variável |
| Assignment | Atribuição |
| Value | Valor |
| Operator | Operador |
| Store | Armazenar |

## 3.2. Atividade de tradução

### Frase 1

**Original:**

A variable stores a value.

**Minha tradução:**

Uma variável armazena um valor.

### Frase 2

**Original:**

Assignment uses the equals sign.

**Minha tradução:**

A atribuição utiliza o sinal de igual.

### Frase 3

**Original:**

Python allows changing variable values.

**Minha tradução:**

Python permite alterar os valores das variáveis.

### Avaliação do Technical English

As três traduções estão corretas.

Demonstrei compreender o vocabulário técnico e o significado das frases relacionadas à programação.

**Nota: 10/10**

---

# 4. EVIDÊNCIAS PRÁTICAS

## 4.1. Identificação dos tipos de dados

**Arquivo executado:** `aula.py`

### Comando utilizado:

```bash
python aula.py
```

### Resultado apresentado no Termux:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

### Avaliação técnica:

Os quatro tipos foram identificados corretamente:

| Tipo | Significado |
|---|---|
| str | Texto |
| int | Número inteiro |
| float | Número decimal |
| bool | Valor booleano |

**Resultado:** execução bem-sucedida.

## 4.2. Desafio prático — Perfil de cadastro

**Arquivo executado:** `perfil.py`

### Comando utilizado:

```bash
python perfil.py
```

### Resultado apresentado no Termux:

```text
================================
       PERFIL DE CADASTRO
================================
Nome: Lucas Henrique Martins
Idade: 28
Sexo: Masculino
CPF: [DADO FICTÍCIO OMITIDO]
Nacionalidade: Brasileira
Estado civil: Solteiro
Profissão: Desenvolvedor de Software
Empresa: NexaTech Soluções
Renda mensal: R$4500.00
```

### Avaliação técnica:

O programa foi executado com sucesso.

Foram demonstradas as seguintes competências:

- Criação de variáveis.
- Atribuição de valores.
- Armazenamento de informações textuais e numéricas.
- Utilização de `print()`.
- Organização da apresentação dos dados.
- Execução de um arquivo Python pelo Termux.

**Resultado:** desafio concluído.

**Observação de segurança:** utilizar somente dados fictícios em projetos e capturas destinados ao portfólio. Não publicar CPF ou outros dados pessoais reais.

---

# 5. AVALIAÇÃO GERAL DA AULA

## 5.1. Desempenho por atividade

| Atividade | Nota |
|---|---:|
| Anotações teóricas | 10,0 |
| Exercício 1 | 8,0 |
| Exercício 2 | 10,0 |
| Exercício 3 | 10,0 |
| Exercício 4 | 10,0 |
| Technical English | 10,0 |

## 5.2. Cálculo da nota

Média aritmética das seis avaliações:

(10 + 8 + 10 + 10 + 10 + 10) / 6 = 9,67

**Nota final arredondada: 9,7/10.**

## 5.3. Resultado

**SITUAÇÃO: APROVADO**

Desempenho excelente.

O estudante demonstrou boa compreensão dos fundamentos de atribuição e variáveis em Python, conseguiu resolver os exercícios propostos e desenvolveu um programa funcional no Termux.

---

# 6. PONTOS FORTES IDENTIFICADOS

1. Compreensão do conceito de variável.
2. Domínio do operador de atribuição.
3. Capacidade de modificar valores armazenados.
4. Utilização correta de operadores de atribuição combinada.
5. Compreensão da diferença entre atribuição e comparação.
6. Identificação dos tipos primitivos com `type()`.
7. Capacidade de construir e executar pequenos programas.
8. Boa compreensão do vocabulário técnico em inglês.

---

# 7. PONTO A MELHORAR

## Sensibilidade a maiúsculas e minúsculas

Foi identificado um pequeno erro no primeiro exercício.

Python diferencia identificadores escritos com letras maiúsculas e minúsculas.

Exemplo:

```python
nome = "Rodrigo"

print(nome)
```

É diferente de:

```python
nome = "Rodrigo"

print(Nome)
```

O segundo exemplo gera `NameError`, pois a variável `Nome` não foi definida.

**Recomendação:** manter consistência na escrita dos nomes das variáveis e utilizar o padrão `snake_case`.

---

# 8. REGISTRO DE COMPETÊNCIAS ADQUIRIDAS

Ao concluir a Aula 15, demonstrei capacidade de:

- [x] Criar variáveis.
- [x] Atribuir valores.
- [x] Modificar valores armazenados.
- [x] Utilizar operadores de atribuição combinada.
- [x] Diferenciar atribuição de comparação.
- [x] Trabalhar com diferentes tipos de valores.
- [x] Identificar tipos utilizando `type()`.
- [x] Utilizar `print()`.
- [x] Desenvolver pequenos programas.
- [x] Executar arquivos Python no Termux.
- [x] Compreender vocabulário técnico em inglês.

---

# 9. PARECER ACADÊMICO

O estudante apresentou excelente aproveitamento na Aula 15.

Demonstrou domínio dos conceitos fundamentais de atribuição e variáveis, compreendeu a utilização dos operadores matemáticos combinados e conseguiu aplicar os conhecimentos em uma atividade prática.

O pequeno erro identificado no primeiro exercício está relacionado à sensibilidade de Python a letras maiúsculas e minúsculas, não representando uma dificuldade conceitual significativa.

A atividade prática foi concluída com sucesso, demonstrando capacidade de transformar os conhecimentos teóricos em código executável.

**Recomendação acadêmica:** avançar para a próxima aula, mantendo atenção à sintaxe e à consistência na nomenclatura das variáveis.

---

# 10. ENCERRAMENTO

**AULA 15 — CONCLUÍDA**

**Data:** 09/11/2026

**Nota final:** 9,7/10

**Situação:** APROVADO


---

**FORMAÇÃO COMPLETA EM CIBERSEGURANÇA**

**SEMANA 03 — FUNDAMENTOS DE PYTHON**

**REGISTRO OFICIAL DE APRENDIZAGEM — AULA 15**
