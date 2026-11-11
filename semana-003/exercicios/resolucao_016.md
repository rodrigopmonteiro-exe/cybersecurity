# FORMAÇÃO COMPLETA EM CIBERSEGURANÇA

# SEMANA 03 — FUNDAMENTOS DE PYTHON

# AULA 16 — TIPOS DE DADOS EM PYTHON

**Data:** 10/11/2026 
**Carga horária:** 2 horas 
**Nível:** Iniciante 
**Status:** APROVADO

---

# 1. REGISTRO DAS ANOTAÇÕES TEÓRICAS

## 1.1. O que são tipos de dados?

Quando criamos uma variável em Python, precisamos armazenar alguma informação.

São utilizados diferentes tipos de dados para representar essas informações.

## 1.2. Tipo String — str

Representa informações textuais.

Exemplos:

```python
nome = "Carlos"
cidade = "Rio de Janeiro"
telefone = "999999999"
```

**Observação importante:**

Textos ficam entre aspas. Mesmo que uma informação contenha apenas números, ela pode ser armazenada como string quando não precisamos realizar operações matemáticas.

Exemplos:

- Endereços.
- Telefones.
- Códigos de identificação.
- Senhas.

## 1.3. Tipo Inteiro — int

Representa números sem casas decimais.

Exemplos:

```python
idade = 25
quantidade = 10
temperatura = -5
```

## 1.4. Tipo Ponto Flutuante — float

Representa números que possuem casas decimais.

Exemplos:

```python
altura = 1.75
preco = 29.90
temperatura = 36.5
```

**Observação:** em Python, utilizamos ponto e não vírgula para separar casas decimais.

## 1.5. Tipo Booleano — bool

Representa apenas dois valores:

```python
True
False
```

Exemplos:

```python
usuario_ativo = True
senha_correta = False
```

Podemos utilizar booleanos em condições:

```python
idade = 20

maior_de_idade = idade >= 18

print(maior_de_idade)
```

**Resultado:**

```text
True
```

Na cibersegurança, os booleanos são muito importantes para controlar permissões e validar condições.

## 1.6. Identificando tipos com type()

O Python possui uma função chamada `type()`.

Ela permite descobrir qual é o tipo de dado armazenado em uma variável.

Exemplo:

```python
nome = "Rodrigo"
idade = 44

print(type(nome))
print(type(idade))
```

Resultados:

```text
<class 'str'>
<class 'int'>
```

## 1.7. Entrada de dados com input()

A função `input()` recebe informações digitadas pelo usuário.

Tudo que é recebido diretamente por `input()` chega como uma string (`str`).

Exemplo:

```python
idade = input("Digite sua idade: ")

print(type(idade))
```

Mesmo que o usuário digite 25, o resultado será:

```text
<class 'str'>
```

## 1.8. Conversão de tipos — Type Casting

Para transformar o valor recebido em um número inteiro, utilizamos `int()`.

Exemplo:

```python
idade = int(input("Digite sua idade: "))

print(type(idade))
```

Agora o resultado será:

```text
<class 'int'>
```

Isso é chamado de conversão de tipos (*type casting*).

---

# 2. RESPOSTAS DOS EXERCÍCIOS

## Exercício 1 — Classificação dos valores

**Enunciado:** Classificar os valores apresentados utilizando os tipos `int`, `float`, `str` e `bool`.

### Minhas respostas:

| Valor | Minha resposta |
|---|---|
| 15 | int |
| 15.5 | float |
| "15" | str |
| True | bool |
| False | bool |
| "Python" | str |
| -20 | int |
| 0.75 | float |

### Avaliação:

Todas as oito classificações estão corretas.

Demonstrei compreender as diferenças entre os quatro tipos fundamentais de dados.

**Nota: 10,0/10**

---

## Exercício 2 — Criando quatro variáveis

**Enunciado:** Criar quatro variáveis, cada uma utilizando um dos tipos estudados.

### Minha resolução:

```python
nome = "Rodrigo"
idade = 44
altura = 1.78
estudante = True
```

### Avaliação:

Todas as variáveis foram criadas corretamente.

| Variável | Tipo | Avaliação |
|---|---|---|
| nome | str | Correto |
| idade | int | Correto |
| altura | float | Correto |
| estudante | bool | Correto |

Demonstrei capacidade de escolher e utilizar os quatro tipos fundamentais.

**Nota: 10,0/10**

---

## Exercício 3 — Escolhendo o tipo adequado

**Enunciado:** Identificar o tipo de dado mais adequado para cada informação.

### Minhas respostas:

| Informação | Minha resposta |
|---|---|
| Nome de usuário | String |
| Quantidade de tentativas | Integer |
| Versão de um programa | Float |
| Conta autorizada | Boolean |
| Preço de um produto | Float |

### Avaliação:

Quatro respostas estão adequadas.

A questão da versão de um programa merece um ajuste conceitual.

Uma versão simples como `1.5` pode ser representada como `float`.

Entretanto, versões como `3.11.8` devem ser representadas como strings.

Exemplo:

```python
versao = "3.11.8"

print(type(versao))
```

Resultado:

```text
<class 'str'>
```

**Correção recomendada:** utilizar `str` para representar versões de software em geral.

**Nota: 9,0/10**

---

## Exercício 4 — Diferença entre texto e número

**Enunciado:** Explicar por que `"100"` e `100` são diferentes.

### Minha resposta:

O valor `"100"` é uma string e não participa diretamente de operações matemáticas como número.

O valor `100` é um número inteiro e permite realizar cálculos matemáticos.

### Complementação técnica:

```python
numero = 100
texto = "100"

print(type(numero))
print(type(texto))
```

Resultado:

```text
<class 'int'>
<class 'str'>
```

A diferença está no tipo de dado.

Uma string pode participar de outras operações, como concatenação, mas não é automaticamente interpretada como número.

**Nota: 10,0/10**

---

# 3. TECHNICAL ENGLISH

## 3.1. Vocabulário técnico

| Inglês | Português |
|---|---|
| Integer | Inteiro |
| Float | Número decimal |
| String | Texto |
| Boolean | Booleano |
| Data type | Tipo de dado |

### Avaliação:

Todos os termos foram traduzidos corretamente.

## 3.2. Atividade de tradução

### Frase 1

**Original:**

Python supports different data types.

**Minha tradução:**

Python suporta diferentes tipos de dados.

### Frase 2

**Original:**

A string stores text.

**Minha tradução:**

Uma string armazena texto.

### Frase 3

**Original:**

A boolean has two possible values.

**Minha tradução:**

Um booleano tem dois valores possíveis.

### Avaliação:

As três traduções estão corretas.

Demonstrei compreensão do vocabulário técnico relacionado aos tipos de dados.

**Nota: 10,0/10**

---

# 4. EVIDÊNCIAS PRÁTICAS NO TERMUX

## 4.1. Primeiro programa — Identificação dos tipos

**Arquivo executado:** `aula.py`

### Comando utilizado:

```bash
python aula.py
```

### Resultado apresentado:

```text
Nome: Ana
Idade: 28
Altura: 1.68
Tem acesso: True

TIPOS DE DADOS
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

### Avaliação técnica:

Todos os resultados foram apresentados corretamente.

| Informação | Tipo identificado |
|---|---|
| Nome | str |
| Idade | int |
| Altura | float |
| Tem acesso | bool |

**Resultado:** execução bem-sucedida.

## 4.2. Segundo programa — Controle de acesso

**Arquivo executado:** `controle_de_acesso.py`

### Comando utilizado:

```bash
python controle_de_acesso.py
```

### Código utilizado:

```python
usuario = "admin"
tentativas = 3
versao = 1.5
autorizado = True

print("USUÁRIO:", usuario)
print("TENTATIVAS:", tentativas)
print("VERSÃO:", versao)
print("AUTORIZADO:", autorizado)

print("\nTIPOS DE DADOS")

print(type(usuario))
print(type(tentativas))
print(type(versao))
print(type(autorizado))
```

### Resultado apresentado:

```text
CONTROLE DE ACESSO

Usuário: admin
Tentativas: 3
Versão: 1.5
Autorizado: True

TIPOS DE DADOS
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

### Avaliação técnica:

O programa foi executado com sucesso.

Foram demonstradas as seguintes competências:

- Criação de variáveis.
- Utilização dos quatro tipos fundamentais.
- Atribuição de valores.
- Apresentação de informações com `print()`.
- Identificação dos tipos com `type()`.
- Organização de informações em um programa.
- Execução de arquivos Python pelo Termux.

**Resultado:** execução bem-sucedida.

---

# 5. AVALIAÇÃO GERAL DA AULA

## 5.1. Desempenho por atividade

| Atividade | Nota |
|---|---:|
| Anotações teóricas | 10,0 |
| Exercício 1 | 10,0 |
| Exercício 2 | 10,0 |
| Exercício 3 | 9,0 |
| Exercício 4 | 10,0 |
| Technical English | 10,0 |
| Prática no Termux | 10,0 |

## 5.2. Cálculo da nota

Média aritmética das sete avaliações:

(10 + 10 + 10 + 9 + 10 + 10 + 10) / 7 = 9,857

**Nota final arredondada: 9,9/10.**

## 5.3. Resultado

**SITUAÇÃO: APROVADO**

O estudante demonstrou excelente aproveitamento na compreensão e aplicação dos quatro tipos fundamentais de dados em Python.

---

# 6. PONTOS FORTES IDENTIFICADOS

1. Compreensão dos quatro tipos fundamentais.
2. Capacidade de classificar valores corretamente.
3. Diferenciação entre textos e números.
4. Compreensão dos valores booleanos.
5. Utilização adequada de `type()`.
6. Compreensão do funcionamento de `input()`.
7. Conhecimento inicial sobre conversão de tipos.
8. Aplicação dos conceitos em um cenário de controle de acesso.
9. Execução correta dos programas no Termux.
10. Boa compreensão do vocabulário técnico em inglês.

---

# 7. PONTOS A MELHORAR

## 7.1. Representação de versões de software

Uma versão como `3.11.8` não deve ser tratada como um número decimal.

Para representar versões de software em geral, utilizar `str`.

Exemplo:

```python
versao_python = "3.11.8"
```

## 7.2. Escolha dos tipos de dados

É importante compreender que a escolha do tipo depende da finalidade da informação.

Exemplos:

- Idade: int.
- Altura: float.
- Nome: str.
- Autorização: bool.
- Telefone: str.
- Versão de software: str.

---

# 8. REGISTRO DE COMPETÊNCIAS ADQUIRIDAS

Ao concluir a Aula 16, demonstrei capacidade de:

- [x] Identificar o tipo int.
- [x] Identificar o tipo float.
- [x] Identificar o tipo str.
- [x] Identificar o tipo bool.
- [x] Diferenciar texto de número.
- [x] Criar variáveis com diferentes tipos.
- [x] Utilizar a função type().
- [x] Compreender a função input().
- [x] Compreender a conversão de tipos.
- [x] Desenvolver programas com diferentes tipos de dados.
- [x] Executar programas Python no Termux.
- [x] Relacionar tipos de dados com situações de cibersegurança.

---

# 9. PARECER ACADÊMICO

O estudante apresentou excelente desempenho na Aula 16.

Demonstrou compreensão dos quatro tipos fundamentais de dados, conseguiu classificá-los corretamente e aplicou os conceitos em programas executáveis.

As atividades práticas foram concluídas com sucesso no Termux.

O principal ponto de melhoria identificado está na representação de versões de software, que exige atenção à diferença entre números decimais e identificadores textuais.

O estudante demonstrou capacidade de relacionar os conhecimentos adquiridos com situações práticas de cibersegurança, especialmente no contexto de controle de acesso.

**Recomendação acadêmica:** avançar para a próxima aula, mantendo a prática de programação e o registro das evidências.

---

# 10. ENCERRAMENTO

**AULA 16 — CONCLUÍDA**

**Data:** 10/11/2026

**Nota final:** 9,9/10

**Situação:** APROVADO

---

**FORMAÇÃO COMPLETA EM CIBERSEGURANÇA**

**SEMANA 03 — FUNDAMENTOS DE PYTHON**

**REGISTRO OFICIAL DE APRENDIZAGEM — AULA 16**
