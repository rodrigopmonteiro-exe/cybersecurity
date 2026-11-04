# SEMANA 02 — ALGORITMOS E PENSAMENTO COMPUTACIONAL

## TERÇA-FEIRA — 03/11/2026

# Aula 02: Entrada, processamento e saída (IPO)

**Duração:** 2 horas
**Área:** Programação

## Objetivo

Compreender a estrutura básica de funcionamento de um programa.

---

## Parte 1 — Teoria (30 minutos)

Estude o modelo IPO:

- **Input:** dados recebidos.
- **Process:** operações realizadas.
- **Output:** resultados apresentados.

### Exemplo: calcular a média de duas notas.

| Etapa | Operação |
|---|---|
| Entrada | Receber nota 1 e nota 2 |
| Processamento | Somar as notas e dividir por 2 |
| Saída | Apresentar a média |


---

## Parte 2 — Construção de algoritmos (25 minutos)

Analise três situações:

1. Calcular a idade de uma pessoa a partir do ano de nascimento.
2. Converter quilômetros em metros.
3. Calcular o valor total de uma compra com quantidade e preço unitário.

Para cada situação, identifique entrada, processamento e saída.

---

## Parte 3 — Exercícios (25 minutos)

1. Identifique o IPO de uma calculadora.
2. Identifique o IPO de um sistema de login.
3. Identifique o IPO de um programa que calcula a área de um retângulo.
4. Identifique o IPO de um programa que converte Celsius para Fahrenheit.
5. Explique por que a entrada precisa ser validada.

---

## Parte 4 — Laboratório Python (30 minutos)

Crie o arquivo:

```bash
nano aula02.py

print("CALCULADORA DE MEDIA")

nome = input("Nome do aluno: ")

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2) / 2

print("\nRESULTADO")
print("Aluno:", nome)
print("Media:", media)

python aula02.py

---

## Parte 5 — Technical English (10 minutos)

Traduza:

1. Enter your name.
2. Enter two numbers.
3. Calculate the average.
4. Display the result.
5. The program processes the input data.

---

## Entrega da aula
- Cinco exercícios resolvidos.
- Arquivo aula02.py.
- Identificação do IPO dos três problemas.
- Traduções em inglês.
