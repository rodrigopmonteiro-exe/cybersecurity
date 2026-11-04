# QUARTA-FEIRA — 04/11

## Aula 03: Decomposição de problemas

**Duração:** 2 horas

**Disciplina:** Raciocínio lógico

**Objetivo:** aprender a dividir problemas complexos em partes menores e administráveis.

---

## Parte 1 — Teoria (30 minutos)

Estude:

1. O que é decomposição.
2. Problemas complexos e problemas menores.
3. Divisão de tarefas.
4. Identificação de entradas e resultados.
5. Modularização.
6. Relação entre decomposição e programação.

### Exemplo: sistema de cadastro de usuários

Problema principal: desenvolver um sistema de cadastro.

**Divisão:**

- Módulo 1: solicitar nome.
- Módulo 2: solicitar idade.
- Módulo 3: validar os dados.
- Módulo 4: armazenar os dados.
- Módulo 5: apresentar confirmação.

Cada módulo tem uma responsabilidade específica.

## Parte 2 — Aplicação (30 minutos)

Decomponha os seguintes problemas:

1. Sistema de cadastro de usuários.
2. Sistema de autenticação.
3. Calculadora de despesas mensais.

Para cada um, identifique pelo menos cinco tarefas menores.

## Parte 3 — Exercícios (25 minutos)

1. Defina decomposição.
2. Qual a vantagem de dividir um problema?
3. O que é modularização?
4. Qual a relação entre decomposição e reutilização de código?
5. Divida o desenvolvimento de uma calculadora em etapas.
6. Explique o que aconteceria se todas as responsabilidades estivessem concentradas em uma única parte do programa.

## Parte 4 — Laboratório Python (25 minutos)

Crie:

```bash
nano aula03.py

def solicitar_nome():
    return input("Digite seu nome: ")

def solicitar_idade():
    return int(input("Digite sua idade: "))

def apresentar_resultado(nome, idade):
    print("\nCADASTRO")
    print("Nome:", nome)
    print("Idade:", idade)

nome = solicitar_nome()
idade = solicitar_idade()

apresentar_resultado(nome, idade)

## Parte 5 — Technical English (10 minutos)

### Vocabulário

| Inglês | Português |
|---|---|
| Decomposition | Decomposição |
| Function | Função |
| Module | Módulo |
| Task | Tarefa |
| Responsibility | Responsabilidade |
| Reusability | Reutilização |

### Atividade

Explique em inglês, utilizando três frases, por que dividir um programa em funções é útil.

## Entrega da aula

- [ ] Três problemas decompostos.
- [ ] Seis exercícios respondidos.
- [ ] Arquivo `aula03.py`.
- [ ] Atividade de inglês.
