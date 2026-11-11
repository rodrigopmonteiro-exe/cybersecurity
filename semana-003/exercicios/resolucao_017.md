# FORMAÇÃO COMPLETA EM CIBERSEGURANÇA

# SEMANA 03 — FUNDAMENTOS DE PYTHON

# AULA 17 — PRINT(), INPUT() E TYPE()

**Data:** 11/11/2026
**Numeração semanal:** Aula 03
**Disciplina:** Fundamentos de Python
**Carga horária:** 2 horas
**Nível:** Iniciante
**Status:** APROVADA NAS ATIVIDADES APRESENTADAS

---

# 1. REGISTRO DAS ANOTAÇÕES TEÓRICAS

## 1.1. Diferença entre "100" e 100

### Minha resposta:

"100" e 100 são diferentes porque "100" é uma string e não permite cálculos matemáticos diretamente como número.

Já 100 é um valor inteiro e permite cálculos matemáticos.

### Avaliação:

Resposta correta.

Explicação:

- "100": representa um texto (str).
- 100: representa um número inteiro (int).

Exemplo:

```python
texto = "100"
numero = 100

print(type(texto))
print(type(numero))
```

Resultado:

```text
<class 'str'>
<class 'int'>
```

**Nota: 10,0/10**

---

# 2. CONTEÚDO TEÓRICO — AULA 17

## 2.1. Função print()

Utilizada para apresentar informações na tela.

Exemplo:

```python
print("Bem-vindo ao Python!")
```

Também podemos apresentar variáveis:

```python
nome = "Carlos"

print(nome)
```

A função `print()` permite apresentar informações armazenadas em variáveis.

### Avaliação das anotações:

Compreensão correta da finalidade da função.

## 2.2. Função input()

Permite receber informações digitadas pelo usuário.

Exemplo:

```python
nome = input("Digite seu nome: ")

print("Bem-vindo,", nome)
```

### Atenção:

`input()` retorna uma string, mesmo quando o usuário digita um número.

Exemplo:

```python
idade = input("Digite sua idade: ")

print(idade)
print(type(idade))
```

Se o usuário digitar 25, o resultado será:

```text
<class 'str'>
```

### Avaliação das anotações:

Você registrou corretamente que o `input()` recebe inicialmente informações como texto.

## 2.3. Função type()

Identifica o tipo de dado de uma informação.

Exemplo:

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

Resultado:

```text
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
```

### Avaliação das anotações:

Compreensão correta da finalidade da função `type()`.

---

# 3. RESPOSTAS DOS EXERCÍCIOS

## Exercício 1 — Finalidade de print()

**Enunciado:** Explique a finalidade de `print()`.

**Avaliação:**

A função `print()` é utilizada para apresentar informações na tela.

A resposta foi registrada corretamente nas anotações teóricas.

**Nota: 10,0/10**

## Exercício 2 — Finalidade de input()

**Enunciado:** Explique a finalidade de `input()`.

**Avaliação:**

A função `input()` permite receber informações digitadas pelo usuário.

A resposta foi registrada corretamente nas anotações teóricas.

**Nota: 10,0/10**

## Exercício 3 — Tipo retornado por input()

**Enunciado:** Qual é o tipo retornado por `input()`?

**Resposta:**

`str` (string).

**Correção:**

Correto. O `input()` retorna inicialmente uma string, independentemente de o usuário digitar letras ou números.

**Nota: 10,0/10**

## Exercício 4 — Identificando tipos

**Enunciado:**

Identifique o resultado:

```python
x = 10
y = "10"

print(type(x))
print(type(y))
```

### Minha resposta:

```text
<class 'int'>
<class 'str'>
```

### Avaliação:

Resposta totalmente correta.

- x armazena um número inteiro.
- y armazena um texto.

**Nota: 10,0/10**

## Exercício 5 — Criando um programa

**Enunciado:**

Crie um programa que solicite:

- Nome.
- Idade.
- Profissão.

Depois apresente todas as informações e seus respectivos tipos.

### Minha resolução:

```python
nome = input("Nome:")
idade = int(input("Idade:"))
profissao = input("Profissão:")

print("\nDados Cadastrados")

print("Nome:", nome)
print("Idade:", idade)
print("Profissão:", profissao)

print("\nTipos de dados")

print(type(nome))
print(type(idade))
print(type(profissao))
```

### Avaliação técnica:

O programa está correto e apresenta:

- Entrada de dados com `input()`.
- Armazenamento em variáveis.
- Conversão de idade utilizando `int()`.
- Apresentação com `print()`.
- Identificação dos tipos com `type()`.

### Observação do professor:

Você utilizou:

```python
idade = int(input("Idade:"))
```

Isso converte a informação recebida em um número inteiro.

Embora o exercício tenha como foco `input()` e `type()`, sua solução antecipou corretamente o conceito de conversão de tipos.

Apenas é importante compreender que o `input()` recebe primeiro uma string e depois o `int()` realiza a conversão.

**Nota: 9,5/10**

---

# 4. TECHNICAL ENGLISH

## 4.1. Vocabulário técnico

| Inglês | Português |
|---|---|
| Input | Entrada |
| Output | Saída |
| Display | Exibir |
| User input | Entrada do usuário |
| Function | Função |

### Avaliação:

Todas as traduções estão corretas.

**Nota: 10,0/10**

## 4.2. Atividade de tradução

### Frase 1

**Original:**

The input function receives information.

**Minha tradução:**

A função input recebe informações.

**Avaliação:** Correta.

### Frase 2

**Original:**

The print function displays information.

**Minha tradução:**

A função print exibe informações.

**Avaliação:** Correta.

### Frase 3

**Original:**

The type function identifies data types.

**Minha tradução:**

A função type identifica os tipos de dados.

**Avaliação:** Correta.

**Nota: 10,0/10**

---

# 5. EVIDÊNCIAS PRÁTICAS NO TERMUX

## 5.1. Organização dos arquivos

No Termux, foi utilizada a pasta:

```bash
~/semana-003/aula-17
```

Comando executado:

```bash
ls
```

Resultado:

```text
aula.py
dados.py
```

A presença dos dois arquivos confirma a organização dos programas da aula.

## 5.2. Primeiro programa — Cadastro de estudantes

**Arquivo:** `aula.py`

### Comando executado:

```bash
python aula.py
```

### Resultado apresentado:

```text
CADASTRO DE ESTUDANTES
Nome: Rodrigo Monteiro
Idade: 44
Cidade: Macaé

DADOS CADASTRADOS
Nome: Rodrigo Monteiro
Idade: 44
Cidade: Macaé

TIPOS DE DADOS

<class 'str'>
<class 'str'>
<class 'str'>
```

### Avaliação técnica:

O programa foi executado corretamente.

As três informações foram recebidas utilizando `input()`.

O resultado de `type()` confirmou que:

| Variável | Tipo |
|---|---|
| nome | str |
| idade | str |
| cidade | str |

### Conclusão:

O resultado demonstrou corretamente que `input()` recebe inicialmente as informações como strings.

**Nota: 10,0/10**

## 5.3. Segundo programa — Cadastro de usuários

**Arquivo:** `dados.py`

### Comando executado:

```bash
python dados.py
```

### Resultado apresentado:

```text
Nome: [DADO OMITIDO]
Email: [DADO OMITIDO]
Idade: 44

CADASTRO DE USUÁRIOS

Nome: [DADO OMITIDO]
Email: [DADO OMITIDO]
Idade: 44 anos.

<class 'str'>
<class 'str'>
<class 'int'>
```

### Avaliação técnica:

O programa foi executado corretamente.

Os tipos foram identificados da seguinte maneira:

| Informação | Tipo |
|---|---|
| Nome | str |
| E-mail | str |
| Idade | int |

### Conclusão:

Você aplicou a conversão de tipos utilizando `int()` na entrada da idade.

Isso demonstra que compreendeu a diferença entre receber uma informação e convertê-la para outro tipo de dado.

**Nota: 10,0/10**

---

# 6. COMPETÊNCIAS PRÁTICAS ADQUIRIDAS

Ao realizar as atividades, demonstrei capacidade de:

- [x] Utilizar `print()` para apresentar informações.
- [x] Utilizar `input()` para receber informações.
- [x] Armazenar informações em variáveis.
- [x] Identificar tipos utilizando `type()`.
- [x] Diferenciar `str` de `int`.
- [x] Compreender o comportamento do `input()`.
- [x] Organizar informações em programas.
- [x] Criar programas interativos.
- [x] Utilizar conversão de tipos com `int()`.
- [x] Executar arquivos Python no Termux.
- [x] Desenvolver dois programas independentes.

---

# 7. AVALIAÇÃO GERAL

## 7.1. Notas por atividade

| Critério | Nota |
|---|---:|
| Anotações teóricas | 10,0 |
| Exercício 1 | 10,0 |
| Exercício 2 | 10,0 |
| Exercício 3 | 10,0 |
| Exercício 4 | 10,0 |
| Exercício 5 | 9,5 |
| Technical English | 10,0 |
| Prática — aula.py | 10,0 |
| Prática — dados.py | 10,0 |

## 7.2. Média das atividades

Soma das notas: 89,5

Quantidade de avaliações: 9

Média:

89,5 / 9 = 9,944...

**NOTA FINAL ARREDONDADA: 9,9/10**

---

# 8. PARECER ACADÊMICO

O estudante apresentou excelente desempenho na Aula 17.

Demonstrou compreensão das funções fundamentais `print()`, `input()` e `type()`.

As respostas teóricas demonstraram domínio da diferença entre números inteiros e strings, além da compreensão do comportamento da função `input()`.

Na parte prática, desenvolveu e executou dois programas independentes no Termux.

O primeiro programa demonstrou que as informações recebidas diretamente por `input()` são armazenadas como strings.

O segundo programa demonstrou a aplicação da conversão de tipos utilizando `int()`.

Um ponto positivo foi a capacidade de antecipar conceitos da próxima aula, aplicando conversão de tipos antes mesmo do estudo formal desse conteúdo.

### Pontos fortes

1. Boa compreensão dos conceitos fundamentais.
2. Organização dos programas.
3. Utilização correta das funções estudadas.
4. Boa interpretação dos resultados.
5. Aplicação prática dos conhecimentos.
6. Bom desempenho em Technical English.

### Ponto de atenção

Aprofundar a compreensão da conversão de tipos e dos possíveis erros provocados por entradas inválidas.

---

# 9. RESULTADO ACADÊMICO

**AULA 17 — CONCLUÍDA**

**Nota final:** 9,9/10

**Situação:** APROVADO

**Desempenho:** Excelente.

**Evidências:** Anotações teóricas, exercícios resolvidos, Technical English e dois programas executados no Termux.


---

# ENCERRAMENTO

**FORMAÇÃO COMPLETA EM CIBERSEGURANÇA**

**SEMANA 03 — FUNDAMENTOS DE PYTHON**

**REGISTRO ACADÊMICO — AULA 17**

**NOTA FINAL: 9,9/10**

**STATUS: APROVADO**
