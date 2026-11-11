# FORMAÇÃO COMPLETA EM CIBERSEGURANÇA

# SEMANA 03 — FUNDAMENTOS DE PYTHON

# AULA 18 — RELATÓRIO DE DESEMPENHO

**Tema:** Conversão de tipos de dados
**Data:** 12/11/2026
**Carga horária:** 2 horas
**Disciplina:** Fundamentos de Python
**Ambiente:** Termux — Android
**Aluno:** Rodrigo Monteiro

---

# 1. CONTEÚDO TEÓRICO — RESPOSTAS DO ALUNO

## 1.1. Por que precisamos converter tipos?

**Resposta registrada:**

Tudo que recebemos através do `input()` é inicialmente uma string (`str`).

O problema acontece nas operações incompatíveis.

Imagine que queremos calcular a idade de uma pessoa daqui a cinco anos:

```python
idade = input("Digite sua idade: ")

resultado = idade + 5

print(resultado)
```

Esse código apresenta um erro:

```text
TypeError: can only concatenate str (not "int") to str
```

**Explicação:**

O erro acontece porque estamos tentando somar texto (`str`) com número inteiro (`int`).

O Python não realiza essa conversão automaticamente.

Precisamos converter o texto em número.

## 1.2. Funções de conversão

### int() — Conversão para inteiro

```python
idade = int(input("Digite sua idade: "))

resultado = idade + 5

print(resultado)
```

A função `int()` converte o valor recebido para número inteiro.

### float() — Conversão para decimal

```python
peso = float(input("Digite seu peso: "))

altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é {imc}")
```

A função `float()` converte valores para números decimais.

### str() — Conversão para texto

```python
numero = 10

mensagem = "O número escolhido foi " + str(numero)

print(mensagem)
```

A função `str()` converte um valor para texto.

Sem `str()`, não conseguimos concatenar diretamente texto e número utilizando o operador `+`.

### bool() — Conversão para booleano

A conversão para booleano também existe, mas exige atenção.

Exemplo:

```python
print(bool("False"))
```

Resultado:

```text
True
```

Isso acontece porque a string não está vazia.

---

# 2. EXERCÍCIOS — RESPOSTAS DO ALUNO

## Exercício 1 — Corrigir o código

**Enunciado:**

Corrigir o seguinte programa:

```python
numero = input("Digite um número: ")

resultado = numero + 10

print(resultado)
```

**Resposta do aluno:**

```python
numero = int(input("Digite um número: "))

resultado = numero + 10

print(resultado)
```

**Avaliação: CORRETO**

**Nota: 10/10**

**Comentário do mentor:**

Excelente. Você identificou que precisava converter a entrada para inteiro antes de realizar a soma.

---

## Exercício 2 — Soma de dois números

**Enunciado:**

Receber dois números inteiros e apresentar a soma.

**Resposta do aluno:**

```python
n1 = int(input("Digite um número: "))

n2 = int(input("Digite outro número: "))

soma = n1 + n2

print(f"A soma de {n1} e {n2} é {soma}")
```

**Avaliação: CORRETO**

**Nota: 10/10**

**Comentário do mentor:**

Você utilizou corretamente:

- `input()` para receber informações.
- `int()` para converter os valores.
- `+` para realizar a soma.
- F-string para apresentar o resultado.

Excelente aplicação dos conceitos.

---

## Exercício 3 — Conversão para float

**Enunciado:**

Receber o preço de um produto e converter para `float`.

**Resposta original do aluno:**

```python
preco = input("Digite um preço: ")

print(f"O preço do produto é {float(preco)}")
```

**Avaliação: PARCIALMENTE CORRETO**

**Nota: 7/10**

**Comentário do mentor:**

Você utilizou corretamente `float()` para converter o valor recebido.

Entretanto, a conversão aconteceu somente dentro do `print()`.

A variável `preco` continuou armazenando uma string.

A forma recomendada é:

```python
preco = float(input("Digite um preço: "))

print(f"O preço do produto é {preco}")

print(type(preco))
```

Agora a própria variável `preco` armazena um número decimal.

Resultado esperado:

```text
<class 'float'>
```

**Aprendizado:** a conversão pode acontecer durante a atribuição, permitindo que a variável armazene diretamente o tipo desejado.

---

## Exercício 4 — Conversão para string

**Enunciado:**

Converter o número 100 para string e apresentar seu tipo.

**Resposta do aluno:**

```python
numero = str(100)

print("O número é: " + numero)

print(type(numero))
```

**Avaliação: CORRETO**

**Nota: 10/10**

Resultado esperado:

```text
O número é: 100
<class 'str'>
```

**Comentário do mentor:**

Correto. Você utilizou `str()` para transformar o número inteiro em texto.

---

## Exercício 5 — Diferença entre conversões

**Enunciado:**

Explique a diferença entre:

Código A:

```python
numero = int(input("Número: "))
```

Código B:

```python
numero = input("Número: ")
```

**Resposta do aluno:**

- `numero = int(input("Número: "))` → converte para int.
- `numero = input("Número: ")` → retorna uma string.

**Avaliação: CORRETO**

**Nota: 10/10**

**Comentário do mentor:**

Sua explicação está correta.

No primeiro código, o valor recebido é convertido para inteiro.

No segundo, o valor permanece como string.

Essa diferença é fundamental para evitar erros em operações matemáticas.

---

# 3. AVALIAÇÃO TEÓRICA

| Critério | Nota |
|---|---:|
| Exercício 1 | 10/10 |
| Exercício 2 | 10/10 |
| Exercício 3 | 7/10 |
| Exercício 4 | 10/10 |
| Exercício 5 | 10/10 |

**Resultado:** 47/50 pontos.

**Aproveitamento:** 94%.

---

# 4. PARTE PRÁTICA — TERMUX

Foram executados dois programas no ambiente Termux.

## 4.1. Programa 1 — Calculadora de idade

**Arquivo:** `aula.py`

**Execução:**

```bash
python aula.py
```

**Código utilizado:**

```python
print("CALCULADORA DE IDADE")

nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))

idade_futura = idade + 10

print("========== RESULTADO ==========")

print("Nome:", nome)

print("Idade Atual:", idade, "anos.")

print("Sua idade daqui a 10 anos será", idade_futura, "anos.")
```

**Dados utilizados:**

```text
Nome: Rodrigo Monteiro
Idade: 44
```

**Resultado apresentado:**

```text
========== RESULTADO ==========
Nome: Rodrigo Monteiro
Idade Atual: 44 anos.
Sua idade daqui a 10 anos será 54 anos.
```

**Avaliação: APROVADO**

O programa executou corretamente.

Competências demonstradas:

- Recebimento de informações com `input()`.
- Conversão para inteiro com `int()`.
- Atribuição de variáveis.
- Operações matemáticas.
- Apresentação dos resultados com `print()`.

---

## 4.2. Programa 2 — Calculadora de média

**Arquivo:** `calculadora_media.py`

**Execução:**

```bash
python calculadora_media.py
```

**Dados utilizados:**

```text
Aluno: Rodrigo Monteiro

Primeira nota: 9.0
Segunda nota: 10.0
Terceira nota: 8.5
```

**Cálculo:**

```python
media = (nota1 + nota2 + nota3) / 3
```

Resultado matemático:

```text
(9.0 + 10.0 + 8.5) / 3

Média = 9.166666666666666
```

### Primeira execução

O programa apresentou:

```text
========== BOLETIM ESCOLAR ==========
Aluno: Rodrigo Monteiro.
Média: 9.166666666666666
```

### Primeira melhoria

O aluno identificou que a apresentação de muitas casas decimais não era adequada.

Realizou alterações no código.

### Segunda execução

Resultado:

```text
========== BOLETIM ESCOLAR ==========
Aluno: Rodrigo Monteiro.
Média: 9.17
```

### Terceira execução

Após nova edição, o programa continuou apresentando o resultado esperado:

```text
CALCULADORA DE MÉDIA

Aluno: Rodrigo Monteiro

Digite a primeira nota: 9.0
Digite a segunda nota: 10.0
Digite a terceira nota: 8.5

========== BOLETIM ESCOLAR ==========
Aluno: Rodrigo Monteiro.
Média: 9.17
```

**Avaliação: APROVADO COM EXCELÊNCIA**

O aluno demonstrou capacidade de:

- Receber três valores.
- Converter as entradas para números decimais.
- Realizar operações matemáticas.
- Calcular uma média.
- Identificar um problema de apresentação.
- Melhorar a saída do programa.
- Executar novamente o código para verificar a correção.

### Observação técnica

Uma forma recomendada de apresentar duas casas decimais é:

```python
print(f"Média: {media:.2f}")
```

O especificador `:.2f` determina a apresentação de duas casas decimais.

---

# 5. AVALIAÇÃO DA PRÁTICA

| Critério | Resultado |
|---|---|
| Execução da calculadora de idade | Correta |
| Conversão com int() | Correta |
| Execução da calculadora de média | Correta |
| Conversão com float() | Aplicada |
| Cálculo matemático | Correto |
| Formatação decimal | Corrigida |
| Execução no Termux | Concluída |

**Resultado prático:** Aprovado.

**Nota prática:** 10/10.

---

# 6. TECHNICAL ENGLISH

## Vocabulário apresentado

| Inglês | Português |
|---|---|
| Type conversion | Conversão de tipos |
| Casting | Conversão |
| Integer conversion | Conversão para inteiro |
| Decimal number | Número decimal |
| Invalid input | Entrada inválida |

## Frases traduzidas pelo aluno

**1. Type conversion changes the data type.**

Tradução: A conversão de tipos altera o tipo de dado.

**2. Input returns a string.**

Tradução: Input retorna uma string.

**3. We use int to convert a value into an integer.**

Tradução: Usamos int para converter um valor em um número inteiro.

**Avaliação: CORRETO**

**Nota: 10/10**

Observação: Em inglês técnico, também é importante conhecer a expressão `data type`, que significa tipo de dado.

---

# 7. BOLETIM DE DESEMPENHO — AULA 18

| Critério | Nota |
|---|---:|
| Teoria | 9,0 |
| Exercícios | 9,5 |
| Prática orientada | 10,0 |
| Desafio prático | 10,0 |
| Technical English | 10,0 |

**NOTA FINAL REGISTRADA: 9,5/10**

**SITUAÇÃO: APROVADO COM EXCELÊNCIA**

---

# 8. COMPETÊNCIAS ADQUIRIDAS

Ao concluir a Aula 18, o aluno demonstrou capacidade de:

- [x] Compreender a necessidade de conversão de tipos.
- [x] Utilizar `int()`.
- [x] Utilizar `float()`.
- [x] Utilizar `str()`.
- [x] Compreender a conversão com `bool()`.
- [x] Receber informações com `input()`.
- [x] Identificar tipos utilizando `type()`.
- [x] Realizar operações matemáticas com dados convertidos.
- [x] Desenvolver pequenos programas em Python.
- [x] Executar programas no Termux.
- [x] Identificar e corrigir problemas.
- [x] Melhorar a apresentação dos resultados.

---

# 9. PARECER DO MENTOR

O aluno demonstrou excelente evolução na compreensão dos fundamentos de Python.

Na parte teórica, conseguiu explicar a necessidade de conversão de tipos e identificar situações em que operações entre dados incompatíveis provocam erros.

Nos exercícios, apresentou soluções corretas para a maioria das atividades, demonstrando domínio de `int()`, `float()` e `str()`.

O principal ponto de atenção foi o exercício 3, no qual a conversão foi realizada apenas durante a apresentação do resultado, sem alterar o tipo armazenado na variável original.

Na prática, demonstrou capacidade de desenvolver, executar, observar e melhorar programas.

Um destaque positivo foi a iniciativa de ajustar a apresentação da média de 9.166666666666666 para 9.17.

Essa atitude demonstra atenção à qualidade da saída e preocupação com a apresentação das informações.

### Recomendação acadêmica

Continuar praticando conversões de tipos em programas que recebam informações do usuário.

Nas próximas aulas, esses conhecimentos serão utilizados em estruturas de decisão, validação de informações e desenvolvimento de programas mais completos.

---

# 10. REGISTRO ACADÊMICO

**FORMAÇÃO:** Ciência da Computação e Cibersegurança

**SEMANA:** 03

**AULA:** 18

**DISCIPLINA:** Fundamentos de Python

**TEMA:** Conversão de tipos de dados

**CARGA HORÁRIA:** 2 horas

**AMBIENTE:** Termux — Android

**NOTA FINAL:** 9,5/10

**SITUAÇÃO:** APROVADO

**EVIDÊNCIAS:**

- Anotações teóricas manuscritas.
- Cinco exercícios resolvidos.
- Capturas de execução no Termux.
- Calculadora de idade.
- Calculadora de média.
- Atividade de Technical English.

---

# ENCERRAMENTO

Aula 18 concluída com sucesso.

O aluno consolidou conhecimentos fundamentais sobre conversão de tipos de dados em Python e demonstrou capacidade de aplicar esses conceitos em programas práticos.


---

# FORMAÇÃO COMPLETA EM CIBERSEGURANÇA

**DO ZERO À ESPECIALIZAÇÃO AVANÇADA**

**SEMANA 03 — FUNDAMENTOS DE PYTHON**

**AULA 18 — CONVERSÃO DE TIPOS DE DADOS**

**REGISTRO ACADÊMICO INDIVIDUAL**
