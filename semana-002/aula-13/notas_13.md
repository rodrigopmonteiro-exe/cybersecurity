# SÁBADO — 07/11

# Aula 06: Rastreamento manual de algoritmos (Dry Run)

**Duração:** 2 horas

**Tema:** Depuração lógica

**Objetivo:** aprender a acompanhar a execução de um algoritmo passo a passo, identificando mudanças nas variáveis e resultados.

---

# PARTE 1 — TEORIA (30 MINUTOS)

## Estude

1. O que é rastreamento manual.
2. O conceito de Dry Run.
3. Estado de uma variável.
4. Sequência de execução.
5. Identificação de erros lógicos.
6. Tabela de rastreamento.

## Exemplo

```python
a = 5
b = 3
c = a + b
a = 10

print(a)
print(b)
print(c)
```

## Tabela de rastreamento

| Instrução | a | b | c |
|---|---|---|---|
| a = 5 | 5 | — | — |
| b = 3 | 5 | 3 | — |
| c = a + b | 5 | 3 | 8 |
| a = 10 | 10 | 3 | 8 |

## Resultado final

```text
10
3
8
```

**Observe:** quando `a` muda para 10, `c` permanece 8 porque o cálculo já foi executado.

---

# PARTE 2 — PRÁTICA DE RASTREAMENTO (30 MINUTOS)

Faça o rastreamento manual.

## Exercício A

```python
x = 4
y = 6
z = x * y
y = 10

print(x)
print(y)
print(z)
```

## Exercício B

```python
a = 10
b = 2
a = a + b
b = a * 2

print(a)
print(b)
```

Monte tabelas mostrando o estado das variáveis em cada linha.

---

# PARTE 3 — EXERCÍCIOS (25 MINUTOS)

1. Explique o que é Dry Run.
2. Por que acompanhar o valor das variáveis?
3. Qual a diferença entre erro de sintaxe e erro lógico?
4. Qual o resultado do exercício A?
5. Qual o resultado do exercício B?
6. Identifique o erro lógico:

```python
preco = 100
desconto = 20
total = preco + desconto
print(total)
```

7. Corrija o algoritmo do exercício anterior.

---

# PARTE 4 — LABORATÓRIO PYTHON (25 MINUTOS)

## Crie o arquivo

```bash
nano aula06.py
```

## Digite

```python
numero = 5

print("Valor inicial:", numero)

numero = numero + 3
print("Segundo estado:", numero)

numero = numero * 2
print("Terceiro estado:", numero)

numero = numero - 4
print("Estado final:", numero)
```

## Execute

```bash
python aula06.py
```

**Instrução:** antes de executar, escreva no caderno qual será o resultado de cada etapa. Depois compare.

---

# PARTE 5 — TECHNICAL ENGLISH (10 MINUTOS)

## Vocabulário

| Inglês | Português |
|---|---|
| Debugging | Depuração |
| Variable | Variável |
| Execution | Execução |
| Trace | Rastrear |
| Bug | Defeito/erro |
| Expected result | Resultado esperado |

## Atividade

Explique em três frases o que significa rastrear a execução de um programa.

---

# ENTREGA DA AULA

- [ ] Duas tabelas de rastreamento.
- [ ] Sete exercícios.
- [ ] Arquivo `aula06.py`.
- [ ] Atividade de inglês.
