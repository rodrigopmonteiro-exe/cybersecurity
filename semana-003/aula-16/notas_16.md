# AULA 16 — TERÇA-FEIRA, 10/11/2026

**Formação:** Cibersegurança 
**Disciplina:** Fundamentos de Python 
**Tema:** Tipos de dados — int, float, str e bool 
**Nível:** Iniciante
**Carga horária:** 2 horas

---

# 1. OBJETIVOS

- Conhecer os quatro tipos fundamentais de dados.
- Identificar suas diferenças.
- Armazenar informações corretamente.
- Compreender quando utilizar cada tipo.

---

# 2. CONTEÚDO TEÓRICO

## 2.1. Tipo int — números inteiros

Representa números sem casas decimais.

Exemplos:

```python
idade = 25
quantidade = 10
temperatura = -5
```

O tipo `int` é utilizado para armazenar números inteiros positivos, negativos ou zero.

## 2.2. Tipo float — números decimais

Representa números com casas decimais.

Exemplos:

```python
altura = 1.75
preco = 29.90
temperatura = 36.5
```

**Atenção:** em Python, utilizamos ponto decimal, não vírgula.

Exemplo:

```python
preco = 29.90
```

## 2.3. Tipo str — textos

Representa sequências de caracteres.

Exemplos:

```python
nome = "Carlos"
cidade = "Rio de Janeiro"
curso = "Cibersegurança"
```

Uma string pode conter letras, números, espaços e símbolos.

Exemplo:

```python
cpf = "12345678900"
```

Mesmo contendo apenas números, o CPF deve ser tratado como texto quando não precisamos realizar operações matemáticas com ele.

## 2.4. Tipo bool — valores booleanos

Representa apenas dois valores:

```python
True
False
```

Exemplos:

```python
autorizado = True
acesso_bloqueado = False
```

O tipo booleano é muito importante na programação e na cibersegurança, especialmente para representar condições de autorização, permissões e estados de segurança.

**Atenção:** em Python, `True` e `False` começam com letras maiúsculas.

---

# 3. COMPARAÇÃO DOS TIPOS DE DADOS

| Tipo | Exemplo | Aplicação |
|---|---|---|
| int | 25 | Idade |
| float | 1.75 | Altura |
| str | "Python" | Nome |
| bool | True | Autorização |

## 3.1. Identificando os tipos com type()

Podemos utilizar a função `type()` para descobrir o tipo de uma variável.

Exemplo:

```python
idade = 25
altura = 1.75
nome = "Carlos"
autorizado = True

print(type(idade))
print(type(altura))
print(type(nome))
print(type(autorizado))
```

Resultado esperado:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

---

# 4. PRÁTICA ORIENTADA

## 4.1. Preparando o ambiente no Termux

Execute:

```bash
mkdir -p ~/semana-003/aula-16
cd ~/semana-003/aula-16
nano aula16.py
```

## 4.2. Digite o seguinte código

```python
nome = "Ana"
idade = 28
altura = 1.68
tem_acesso = True

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Tem acesso:", tem_acesso)
```

## 4.3. Execute

```bash
python aula16.py
```

Resultado esperado:

```text
Nome: Ana
Idade: 28
Altura: 1.68
Tem acesso: True
```

## 4.4. Experimente identificar os tipos

Acrescente ao código:

```python
print("\nTIPOS DE DADOS")

print(type(nome))
print(type(idade))
print(type(altura))
print(type(tem_acesso))
```

Execute novamente e observe os resultados.

---

# 5. EXERCÍCIOS

## Exercício 1 — Identificação de tipos

Classifique os valores abaixo:

```python
15
15.5
"15"
True
False
"Python"
-20
0.75
```

Identifique se cada valor pertence ao tipo `int`, `float`, `str` ou `bool`.

## Exercício 2 — Criando variáveis

Crie quatro variáveis, cada uma utilizando um dos tipos estudados.

Apresente todas utilizando `print()`.

## Exercício 3 — Escolhendo o tipo adequado

Identifique o tipo de dado mais adequado para armazenar cada informação:

- Nome de usuário.
- Quantidade de tentativas.
- Versão de um programa.
- Conta autorizada.
- Preço de um produto.

Explique brevemente suas escolhas.

## Exercício 4 — Diferença entre texto e número

Explique por que os valores abaixo são diferentes:

```python
numero = 100
texto = "100"
```

Identifique o tipo de cada variável e explique a diferença entre elas.

---

# 6. DESAFIO — CONTROLE DE ACESSO

Crie um programa chamado `controle_acesso.py`.

Utilize os seguintes dados:

```python
usuario = "admin"
tentativas = 3
versao = 1.5
autorizado = True

print("USUÁRIO:", usuario)
print("TENTATIVAS:", tentativas)
print("VERSÃO:", versao)
print("AUTORIZADO:", autorizado)
```

## Sua missão

1. Criar as quatro variáveis.
2. Utilizar corretamente os tipos de dados.
3. Apresentar todas as informações com `print()`.
4. Identificar os tipos utilizando `type()`.
5. Modificar os valores e observar os resultados.

**Execute no Termux:**

```bash
python controle_acesso.py
```

## Perguntas do desafio

1. Qual é o tipo da variável `usuario`?
2. Qual é o tipo da variável `tentativas`?
3. Qual é o tipo da variável `versao`?
4. Qual é o tipo da variável `autorizado`?
5. Por que o estado de autorização pode ser representado por um valor booleano?

---

# 7. TECHNICAL ENGLISH

## 7.1. Vocabulário técnico

| Inglês | Português |
|---|---|
| Integer | Inteiro |
| Float | Número decimal |
| String | Texto |
| Boolean | Booleano |
| Data type | Tipo de dado |

## 7.2. Atividade de tradução

Traduza as frases abaixo:

1. Python supports different data types.
2. A string stores text.
3. A boolean has two possible values.

## 7.3. Atividade complementar

Escreva três frases em inglês utilizando pelo menos três palavras do vocabulário estudado.

---

# 8. REGISTRO DE APRENDIZAGEM

Após concluir a aula, registre:

1. O que aprendi sobre os tipos de dados?
2. Qual a diferença entre `int` e `float`?
3. Por que `"100"` é diferente de `100`?
4. Quando devo utilizar o tipo `bool`?
5. Qual tipo de dado apresentou maior dificuldade?
6. Consegui desenvolver o desafio sem copiar o exemplo?

---

# 9. EVIDÊNCIAS DE CONCLUSÃO

Para considerar esta aula concluída, organize:

- [ ] Notas próprias da aula.
- [ ] Exercício 1 resolvido.
- [ ] Exercício 2 resolvido.
- [ ] Exercício 3 resolvido.
- [ ] Exercício 4 respondido.
- [ ] Desafio `controle_acesso.py` concluído.
- [ ] Identificação dos tipos utilizando `type()`.
- [ ] Atividade de Technical English concluída.
- [ ] Captura de tela da execução dos programas.
- [ ] Registro das dificuldades encontradas.

---

# 10. CRITÉRIO DE DOMÍNIO

Ao terminar esta aula, devo conseguir:

1. Identificar os quatro tipos fundamentais de dados.
2. Diferenciar números inteiros de números decimais.
3. Diferenciar textos de valores numéricos.
4. Compreender valores booleanos.
5. Criar variáveis utilizando os tipos adequados.
6. Identificar tipos utilizando `type()`.
7. Desenvolver um pequeno programa utilizando diferentes tipos de dados.
8. Compreender aplicações dos tipos de dados em situações relacionadas à cibersegurança.

**Meta:** compreender e diferenciar os quatro tipos fundamentais antes de avançar para entrada e saída de dados.

---

**FORMAÇÃO COMPLETA EM CIBERSEGURANÇA**

**SEMANA 03 — FUNDAMENTOS DE PYTHON**

**AULA 16 — 10/11/2026**
