# Aula 3 — Python: instalação, verificação e primeiro script

**Data:** 28/10/2026  
**Duração:** 2 horas  
**Módulo:** Semana 01 — Fundamentos e ambiente de estudo

## Objetivo

Executar programas Python a partir do Termux e aprender a registrar e interpretar resultados.

---

## Parte A — Conceitos (20 min)

Estude:

- Interpretador Python.
- Arquivo-fonte com extensão `.py`.
- Saída do programa.
- Erros de sintaxe.
- Diferença entre executar um comando no shell e executar código Python.

### Conceitos importantes

**Interpretador Python:** programa responsável por interpretar e executar instruções escritas em Python.

**Arquivo-fonte:** arquivo que contém o código de um programa. Em Python, normalmente utiliza a extensão `.py`.

**Saída do programa (Output):** resultado apresentado pelo programa durante sua execução.

**Erro de sintaxe (Syntax error):** erro causado por uma instrução escrita incorretamente, contrariando as regras da linguagem.

**Shell:** ambiente que interpreta comandos do sistema operacional.

---

## Parte B — Primeiro programa (25 min)

### 1. Crie a pasta da aula

Execute:

```bash
mkdir -p ~/cybersecurity/semana-01/aula-03
cd ~/cybersecurity/semana-01/aula-03
```

### 2. Crie o arquivo

Execute:

```bash
cat > primeiro.py <<'EOF'
print("Meu primeiro laboratório de Python")
print("Estou estudando cibersegurança.")
EOF
```

### 3. Execute o programa

```bash
python primeiro.py
```

### 4. Resultado esperado

```text
Meu primeiro laboratório de Python
Estou estudando cibersegurança.
```

Compare o código com a saída.

Depois, altere a segunda mensagem e execute novamente.

---

## Parte C — Variáveis e entrada de dados (30 min)

### 1. Crie o arquivo `perfil.py`

Execute:

```bash
cat > perfil.py <<'EOF'
nome = input("Seu nome: ")
objetivo = input("Seu objetivo de estudo: ")

print("Estudante:", nome)
print("Objetivo:", objetivo)
EOF
```

### 2. Execute

```bash
python perfil.py
```

### 3. Compreenda o funcionamento

- `input()` recebe informações digitadas pelo usuário.
- `nome` e `objetivo` são variáveis.
- `print()` apresenta informações na tela.
- Os dados recebidos por `input()` são tratados inicialmente como texto (`str`).

**Atenção:** não insira senhas reais, tokens, chaves privadas ou outras informações confidenciais nesses exercícios.

---

## Parte D — Exercícios (30 min)

Resolva os exercícios:

1. Crie um programa que exiba três objetivos de aprendizagem.

2. Crie um programa que receba seu nome e mostre uma saudação.

3. Crie um programa que receba duas palavras e as exiba em linhas separadas.

4. Modifique `primeiro.py` para apresentar a data da aula como texto.

5. Introduza deliberadamente um erro simples, como retirar uma aspa, execute o programa e registre a mensagem de erro. Depois, corrija-o.

### Registro dos exercícios

Para cada exercício, registre:

- Código utilizado.
- Resultado da execução.
- Dificuldades encontradas.
- Correções realizadas.

---

## Parte E — Technical English (15 min)

### Vocabulário técnico

| Inglês | Português |
|---|---|
| Source code | Código-fonte |
| Output | Saída |
| Input | Entrada |
| Variable | Variável |
| Syntax error | Erro de sintaxe |

### Tradução

Traduza a seguinte frase:

**The program receives input and displays output.**

Registre a tradução e procure compreender o significado de cada palavra.

### Evidência

Guarde:

- Os arquivos `.py`.
- As saídas executadas.
- Uma nota explicando o erro que você provocou e corrigiu.

---

## Critério de conclusão

A aula será considerada concluída quando você conseguir:

- Criar e executar um arquivo Python.
- Utilizar `print()` para apresentar informações.
- Criar variáveis.
- Receber dados com `input()`.
- Identificar e corrigir um erro simples de sintaxe.
- Explicar o funcionamento dos programas desenvolvidos.
- Registrar as evidências dos exercícios.
