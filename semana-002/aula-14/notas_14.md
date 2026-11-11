# AULA 14 — PROJETO INTEGRADOR, REVISÃO E AVALIAÇÃO SEMANAL

**DOMINGO — 08/11**

**Duração:** 2 a 3 horas
**Tipo:** Projeto prático

## OBJETIVO

Demonstrar que você consegue utilizar os conhecimentos da semana para analisar um problema, construir um algoritmo, representá-lo e implementá-lo.

---

## PARTE 1 — REVISÃO TEÓRICA (25 MINUTOS)

Revise os seguintes conteúdos:

- Algoritmos.
- Pensamento computacional.
- Os quatro pilares.
- Entrada, processamento e saída.
- Decomposição.
- Pseudocódigo.
- Fluxogramas.
- Rastreamento manual.

---

## PARTE 2 — PROJETO INTEGRADOR (60 MINUTOS)

### Projeto da semana: Sistema de cálculo de desempenho acadêmico

Desenvolva um programa que receba os dados de um estudante e calcule sua média final.

### Requisitos

1. Solicitar o nome do estudante.
2. Solicitar três notas.
3. Calcular a média.
4. Apresentar o nome e a média.
5. Informar se o estudante foi aprovado ou reprovado.

Para este exercício, utilize média mínima 7,0.

### Etapa A — Decomposição

Divida o projeto em cinco tarefas:

- Receber os dados.
- Processar as notas.
- Calcular a média.
- Verificar a condição.
- Apresentar o resultado.

### Etapa B — Pseudocódigo

Escreva o algoritmo antes de programar.

### Etapa C — Fluxograma

Desenhe a sequência de execução, incluindo a decisão de aprovação.

### Etapa D — Python

Crie o arquivo:

```bash
nano projeto_semana02.py
```

Implemente:

```python
print("SISTEMA DE DESEMPENHO ACADEMICO")

nome = input("Nome do estudante: ")

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("\nRESULTADO")
print("Estudante:", nome)
print("Media:", round(media, 2))

if media >= 7:
print("Situacao: APROVADO")
else:
print("Situacao: REPROVADO")
```

### Etapa E — Testes

Execute três cenários:

| Teste | Notas | Resultado esperado |
|---|---|---|
| 1 | 8, 9, 10 | Aprovado |
| 2 | 5, 6, 4 | Reprovado |
| 3 | 7, 7, 7 | Aprovado |

Faça também o rastreamento manual de pelo menos um cenário.

---

## PARTE 3 — AVALIAÇÃO SEMANAL (25 MINUTOS)

Responda sem consultar as anotações:

1. O que é um algoritmo?
2. Quais são os quatro pilares do pensamento computacional?
3. O que significa IPO?
4. Qual a finalidade da decomposição?
5. O que é pseudocódigo?
6. Qual a diferença entre pseudocódigo e Python?
7. Qual símbolo representa uma decisão em um fluxograma?
8. O que é Dry Run?
9. Qual a diferença entre erro de sintaxe e erro lógico?
10. Por que testar diferentes cenários é importante?

---

## PARTE 4 — TECHNICAL ENGLISH (10 MINUTOS)

Leia e traduza:

> An algorithm is a sequence of instructions designed to solve a problem. It receives input, processes data, and produces output. Programmers use pseudocode and flowcharts to represent algorithms before implementing them in a programming language.

Depois, escreva um pequeno parágrafo em inglês explicando o funcionamento do projeto acadêmico.

---

## PARTE 5 — ORGANIZAÇÃO DAS EVIDÊNCIAS

Organize os materiais produzidos durante o projeto:

- Pseudocódigo.
- Fluxograma.
- Arquivo Python `projeto_semana02.py`.
- Resultados dos três testes.
- Rastreamento manual de pelo menos um cenário.
- Respostas da avaliação semanal.
- Atividade de inglês.

---

## PARTE 6 — FINALIZAÇÃO

Revise o projeto e verifique se todos os requisitos foram cumpridos.

- [ ] O programa solicita o nome do estudante.
- [ ] O programa solicita três notas.
- [ ] O programa calcula a média corretamente.
- [ ] O programa apresenta o nome e a média.
- [ ] O programa informa aprovação ou reprovação.
- [ ] O programa utiliza média mínima 7,0.
- [ ] Os três cenários de teste foram executados.
- [ ] Foi realizado o rastreamento manual.
- [ ] O pseudocódigo foi elaborado.
- [ ] O fluxograma foi construído.
- [ ] A avaliação semanal foi respondida.
- [ ] A atividade de inglês foi concluída.
- [ ] As evidências foram organizadas.

---

## RESULTADO FINAL — PROJETO INTEGRADOR E AVALIAÇÃO SEMANAL

Ao concluir esta aula, você deverá demonstrar que consegue:

1. Analisar um problema e dividi-lo em tarefas menores.
2. Elaborar um algoritmo em pseudocódigo.
3. Representar o algoritmo por meio de um fluxograma.
4. Implementar a solução utilizando Python.
5. Testar o funcionamento do programa com diferentes entradas.
6. Realizar o rastreamento manual da execução.
7. Explicar conceitos fundamentais de algoritmos em português e inglês.

**Entrega final:** um projeto funcional de cálculo de desempenho acadêmico, acompanhado de pseudocódigo, fluxograma, testes, rastreamento manual e atividade de inglês técnico.
````
