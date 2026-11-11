# AULA 11 — PSEUDOCÓDIGO E REPRESENTAÇÃO DE ALGORITMOS

## 1. Objetivo da aula

Aprender a representar algoritmos sem depender de uma linguagem de programação específica.

Desenvolver a capacidade de organizar o raciocínio lógico antes de transformar uma solução em código Python.

---

# PARTE 1 — CONTEÚDO TEÓRICO

## 2. O que é pseudocódigo?

Pseudocódigo é uma maneira de escrever os passos de um algoritmo usando uma linguagem simples, parecida com o português, mas seguindo a lógica de programação.

Exemplo:

Imagine que queremos criar um programa que receba a idade de uma pessoa e verifique se ela é maior de idade.

INÍCIO

    ESCREVA "Digite sua idade:"
    LEIA idade

    SE idade >= 18 ENTÃO
        ESCREVA "Maior de idade"
    SENÃO
        ESCREVA "Menor de idade"
    FIM SE

FIM

## 3. Conceitos fundamentais

### Algoritmo

Sequência lógica de passos para resolver um problema.

### Pseudocódigo

Representação textual de um algoritmo.

### Código-fonte

Implementação do algoritmo em uma linguagem de programação.

## 4. Por que pseudocódigo é importante?

- Para desenvolver o raciocínio lógico.
- Planejar programas antes de codificá-los.
- Compreender estruturas condicionais (if, else, elif).
- Trabalhar com repetições (for e while).
- Projetar algoritmos mais simples.
- Resolver problemas sem depender de uma linguagem específica.

## 5. Variáveis

Uma variável é um espaço identificado pelo nome que utilizamos para armazenar um valor durante a execução de um programa.

### Tipos fundamentais em Python

- str: texto.
- int: números inteiros.
- float: números decimais.
- bool: valores booleanos (True ou False).

## 6. Operadores aritméticos

Símbolos utilizados para realizar cálculos matemáticos.

| Operador | Finalidade |
|---|---|
| + | Soma |
| - | Subtração |
| * | Multiplicação |
| / | Divisão |
| // | Divisão inteira |
| % | Módulo (resto) |
| ** | Potenciação |

## 7. Sequência lógica

É uma série de etapas ou instruções organizadas em uma ordem correta, na qual cada etapa contribui para alcançar um objetivo ou resolver um problema.

---

# PARTE 2 — EXEMPLOS DE PSEUDOCÓDIGO

## 8. Exemplo: somar dois números

ALGORITMO Soma

INÍCIO

    LEIA numero1
    LEIA numero2

    resultado <- numero1 + numero2

    ESCREVA resultado

FIM

## 9. Exemplo: calcular a área de um retângulo

ALGORITMO AreaRetangulo

INÍCIO

    LEIA largura
    LEIA altura

    area <- largura * altura

    ESCREVA area

FIM

---

# PARTE 3 — EXERCÍCIOS DE PSEUDOCÓDIGO

## 10. Exercício 1 — Soma de três números

ALGORITMO "Soma de três números"

INÍCIO

    LEIA numero1
    LEIA numero2
    LEIA numero3

    soma <- numero1 + numero2 + numero3

    ESCREVA "Resultado:", soma

FIM

## 11. Exercício 2 — Média de quatro notas

ALGORITMO "Média de quatro notas"

INÍCIO

    LEIA nota1
    LEIA nota2
    LEIA nota3
    LEIA nota4

    media <- (nota1 + nota2 + nota3 + nota4) / 4

    ESCREVA "Média:", media

FIM

## 12. Exercício 3 — Converter horas em minutos

ALGORITMO "Converter horas em minutos"

INÍCIO

    LEIA horas

    minutos <- horas * 60

    ESCREVA "Total de minutos:", minutos

FIM

## 13. Exercício 4 — Perímetro de um quadrado

ALGORITMO "Perímetro de um quadrado"

INÍCIO

    LEIA lado

    perimetro <- lado * 4

    ESCREVA "Perímetro:", perimetro

FIM

## 14. Exercício 5 — Cadastro de pessoa

ALGORITMO "Cadastro de pessoa"

INÍCIO

    ESCREVA "Digite seu nome:"
    LEIA nome

    ESCREVA "Digite sua idade:"
    LEIA idade

    ESCREVA "Nome:", nome
    ESCREVA "Idade:", idade

FIM

## 15. Exercício 6 — Preço total dos produtos

ALGORITMO "Preço total dos produtos"

INÍCIO

    ESCREVA "Digite a quantidade:"
    LEIA quantidade

    ESCREVA "Digite o preço unitário:"
    LEIA preco_unitario

    total <- quantidade * preco_unitario

    ESCREVA "Preço total R$:", total

FIM

---

# PARTE 4 — LABORATÓRIO PYTHON

## 16. Transformando pseudocódigo em Python

### Programa: Soma de três números

Código-fonte:

    print("SOMA DE TRES NUMEROS")

    n1 = float(input("Numero 1: "))
    n2 = float(input("Numero 2: "))
    n3 = float(input("Numero 3: "))

    resultado = n1 + n2 + n3

    print("Resultado:", resultado)

### Execução no Termux

Comandos utilizados:

    nano soma.py

    python soma.py

### Resultado obtido

    SOMA DE TRES NUMEROS
    Numero 1: 10
    Numero 2: 80
    Numero 3: 67
    Resultado: 157.0

### Verificação matemática

10 + 80 + 67 = 157

Resultado: CORRETO.

### Comparação entre pseudocódigo e Python

| Pseudocódigo | Python |
|---|---|
| INÍCIO | Início do programa |
| LEIA numero1 | input() |
| numero1 <- valor | Atribuição com = |
| ESCREVA resultado | print() |
| FIM | Final do programa |

---

# PARTE 5 — TECHNICAL ENGLISH

## 17. Vocabulário técnico

| Inglês | Português |
|---|---|
| Read | Receber informação |
| Store | Armazenar o valor |
| Calculate | Calcular o resultado |
| Display the output | Exibir o resultado |
| End the algorithm | Finalizar o algoritmo |

### Sequência de execução

1. Read the input.
   Receber a entrada.

2. Store the value.
   Armazenar o valor.

3. Calculate the result.
   Calcular o resultado.

4. Display the output.
   Exibir o resultado.

5. End the algorithm.
   Finalizar o algoritmo.

---

# PARTE 6 — OBSERVAÇÕES E NOTAS TÉCNICAS

## 18. Observações sobre o aprendizado

### 18.1. Lógica antes da programação

O pseudocódigo permite organizar o raciocínio antes de escrever o código-fonte.

Isso reduz erros de lógica e facilita a implementação em diferentes linguagens.

### 18.2. Diferença entre atribuição e comparação

No pseudocódigo, o símbolo <- representa atribuição de um valor.

Em Python, utilizamos = para atribuir valores.

Já o operador == é utilizado para comparar se dois valores são iguais.

### 18.3. Utilização de float()

A função float() converte uma entrada textual em um número decimal.

Exemplo:

    numero = float(input("Digite um número: "))

Isso permite trabalhar com números inteiros e decimais.

### 18.4. Entrada e saída de dados

- input(): recebe informações do usuário.
- print(): apresenta informações na tela.

### 18.5. Operações matemáticas

A ordem das operações deve ser respeitada.

Exemplo:

    media = (nota1 + nota2 + nota3 + nota4) / 4

Os parênteses garantem que a soma seja realizada antes da divisão.

---

# PARTE 7 — EVIDÊNCIAS E ENTREGA DA AULA

## 19. Evidências produzidas

- [x] Anotações teóricas realizadas.
- [x] Conceitos de algoritmo e pseudocódigo estudados.
- [x] Variáveis e tipos de dados revisados.
- [x] Operadores aritméticos estudados.
- [x] Seis pseudocódigos elaborados.
- [x] Programa Python desenvolvido.
- [x] Arquivo soma.py criado.
- [x] Programa executado no Termux.
- [x] Resultado matemático conferido.
- [x] Vocabulário técnico em inglês registrado.
- [x] Evidência de execução capturada por print.

## 20. Resultado da avaliação prática

Programa: soma.py

Ambiente: Termux (Android)

Linguagem: Python

Entradas utilizadas:

- Número 1: 10
- Número 2: 80
- Número 3: 67

Resultado esperado: 157

Resultado obtido: 157.0

Status: APROVADO.

## 21. Considerações finais

Nesta aula, foi desenvolvido o entendimento sobre como representar algoritmos utilizando pseudocódigo e como transformar essa representação em código Python.

Os exercícios permitiram trabalhar com entrada de dados, variáveis, operações matemáticas, atribuição e saída de informações.

A execução prática demonstrou que o algoritmo de soma de três números funcionou corretamente no Termux.

O conteúdo constitui uma base importante para o estudo posterior de estruturas condicionais, estruturas de repetição, funções e desenvolvimento de programas mais complexos.

---

# STATUS FINAL DA AULA 11

Aula: Pseudocódigo e Representação de Algoritmos

Teoria: CONCLUÍDA.

Exercícios: CONCLUÍDOS.

Laboratório Python: CONCLUÍDO.

Technical English: REGISTRADO.

Evidências: REGISTRADAS.

Resultado geral: APROVADO.
