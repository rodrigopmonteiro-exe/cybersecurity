CIBERSEGURANÇA

Semana 01 — Aula 03: Python — Interpretação, Verificação e Primeiro Script

---

1. Interpretador Python

1.1 O que é um interpretador Python?

É um programa responsável por executar o código escrito em Python, permitindo que o computador realize as instruções que você definiu.

Para entrar no interpretador, basta digitar "python" no terminal:

python

Você deverá ver um símbolo parecido com este:

>>>

Esse símbolo indica que você está dentro do interpretador interativo do Python.

Para sair do interpretador e voltar ao terminal, digite:

exit()

1.2 Como o Python executa o código?

Uma observação importante: o Python moderno normalmente transforma o código-fonte em bytecode antes de executá-lo na máquina virtual do Python.

Portanto, dizer que o interpretador simplesmente traduz o código diretamente para a linguagem de máquina é uma simplificação.

---

2. Bytecode

2.1 O que é Bytecode?

Bytecode é uma representação intermediária do código Python, criada antes de ser executada pela máquina virtual do Python.

Na implementação mais comum do Python, chamada CPython, o interpretador compila o código para bytecode e depois o executa.

Normalmente, você não precisa criar bytecode manualmente, pois o Python realiza essa transformação automaticamente.

2.2 Como visualizar o Bytecode?

Dentro do interpretador Python, digite:

import dis

Depois:

dis.dis("print(2+3)")

O comando "dis" mostra as instruções de bytecode que o Python gera para executar o código.

2.3 Por que o Bytecode é relevante?

O bytecode é relevante por alguns motivos:

- Análise de programas: Permite examinar instruções internas de um programa.
- Depuração: Ajuda a entender como determinadas operações são executadas.
- Análise de arquivos ".pyc": Esses arquivos geralmente armazenam bytecode compilado do Python e podem ser examinados em investigações técnicas.

Importante: Bytecode não é a mesma coisa que código de máquina nativo.

---

3. Por que transformar código em Bytecode?

Existem algumas razões importantes:

3.1 Eficiência na execução

O Python transforma o código em instruções intermediárias, evitando a necessidade de analisar todo o texto-fonte novamente para cada execução de uma instrução.

Isso faz parte do processo de execução do programa.

3.2 Reutilização de código compilado

O Python pode gerar e armazenar arquivos ".pyc", que contêm bytecode compilado.

Quando as condições permitem, esses arquivos podem ser reutilizados, evitando a recompilação do código-fonte.

3.3 Separação entre código e execução

O programador escreve código Python legível, enquanto a máquina virtual trabalha com instruções internas.

Isso facilita a programação e a implementação dos mecanismos de execução.

3.4 Análise e engenharia reversa

Ferramentas podem inspecionar o bytecode para auxiliar na depuração, análise de programas e engenharia reversa.

Importante: Várias linguagens utilizam bytecode. Essa é uma técnica comum para executar programas por meio de uma máquina virtual.

Exemplos:

- Java.
- C#.
- Kotlin.
- Python.

O bytecode do Python, por exemplo, não é diretamente executado pela JVM (Java Virtual Machine).

---

4. Conceitos Fundamentais

4.1 Máquina Virtual do Python (PVM)

É o mecanismo de execução que interpreta e executa as instruções de bytecode geradas pelo Python.

4.2 Código-fonte (Source Code)

É o código escrito pelo programador em uma linguagem de programação.

Exemplo:

print("Olá, mundo!")

4.3 Linguagem intermediária (Intermediate Language)

É uma representação intermediária utilizada em um ambiente de execução.

No Python, o bytecode representa essa etapa intermediária.

4.4 Código de máquina (Machine Code)

São instruções nativas executadas diretamente pelo processador.

4.5 Arquivo-fonte com extensão ".py"

É um arquivo de texto que contém código-fonte escrito na linguagem Python.

É nele que você escreve as instruções que deseja que o computador execute.

Exemplo:

calculadora.py

4.6 Saída de um programa (Program Output)

É o resultado que um programa apresenta depois de executar suas instruções.

Essa saída pode:

- Aparecer na tela.
- Ser gravada em um arquivo.
- Ser enviada pela rede.
- Ser utilizada por outro programa.

4.7 Erro de sintaxe (Syntax Error)

Acontece quando você escreve um código que não respeita as regras gramaticais da linguagem de programação.

Exemplo:

print("Olá, mundo!"

Nesse exemplo, falta fechar o parêntese.

Forma correta:

print("Olá, mundo!")

---

5. Diferença entre executar comandos no Shell e executar código Python

O Shell interpreta comandos do sistema operacional, enquanto o Python interpreta instruções da linguagem Python.

5.1 Exemplo no Shell

echo "Olá, mundo!"

O Shell executa o comando "echo", que exibe o texto na tela.

5.2 Exemplo no Python

Primeiro, entre no interpretador:

python

Depois, digite:

print("Olá, mundo!")

O interpretador Python executa a instrução "print()".

5.3 Comparação prática

Shell| Python
Interpreta comandos do sistema| Executa instruções Python
Utiliza "echo" para exibir texto| Utiliza "print()"
Trabalha com comandos e ferramentas do sistema| Trabalha com lógica e programação
Pode executar scripts de Shell| Executa scripts ".py"

Os dois ambientes podem trabalhar juntos, mas possuem funções diferentes.

---

6. Primeiro Script Python — Calculadora

Imagine que você criou um arquivo chamado "calculadora.py" com o seguinte código:

a = 10
b = 5

print(a + b)

6.1 Entendendo o código

- "a = 10": Cria uma variável chamada "a" e armazena o valor 10.
- "b = 5": Cria uma variável chamada "b" e armazena o valor 5.
- "print(a + b)": Soma os valores das variáveis e mostra o resultado.

6.2 Como executar no Termux?

Siga estas etapas:

Etapa 1 — Criar o arquivo

No Shell, digite:

nano calculadora.py

Etapa 2 — Escrever o código

a = 10
b = 5

print(a + b)

Etapa 3 — Salvar o arquivo

- "CTRL + O": Salvar.
- "ENTER": Confirmar.
- "CTRL + X": Sair.

Etapa 4 — Executar o programa

No terminal, digite:

python calculadora.py

Etapa 5 — Verificar o resultado

A saída esperada será:

15

O Python executou o código e apresentou o resultado da soma.

---

7. Technical English — Inglês Técnico

7.1 Vocabulário

Inglês| Português
Source code| Código-fonte
Output| Saída
Input| Entrada
Variable| Variável
Syntax error| Erro de sintaxe
Bytecode| Código intermediário
Interpreter| Interpretador
Virtual machine| Máquina virtual
Program execution| Execução do programa

7.2 Frase técnica

English:

The program receives input and displays output.

Português:

O programa recebe uma entrada e apresenta uma saída.

---

8. Registro de Aprendizagem

Semana: 01

Aula: 03

Tema: Python — Interpretação, verificação e primeiro script.

Principais conhecimentos adquiridos

- Conceito de interpretador Python.
- Utilização do interpretador interativo.
- Diferença entre código-fonte e bytecode.
- Funcionamento básico da máquina virtual do Python.
- Utilização do módulo "dis".
- Conceito de arquivos ".py" e ".pyc".
- Diferença entre bytecode e código de máquina.
- Conceito de saída de um programa.
- Identificação de erros de sintaxe.
- Diferença entre comandos do Shell e instruções Python.
- Criação e execução do primeiro script Python.
- Utilização de variáveis e da função "print()".
- Vocabulário técnico em inglês.

Evidências da aula

- Anotações manuscritas.
- Exemplos de código Python.
- Visualização de bytecode.
- Primeiro script "calculadora.py".
- Execução do programa no Termux.
- Registro do resultado obtido.

---

9. Revisão da Aula

Responda sem consultar suas anotações:

1. O que é um interpretador Python?
2. O que é bytecode?
3. Qual é a função da máquina virtual do Python?
4. Qual é a diferença entre código-fonte e código de máquina?
5. Para que serve o módulo "dis"?
6. Qual é a diferença entre executar "echo" no Shell e "print()" no Python?
7. O que é um arquivo ".py"?
8. O que significa um erro de sintaxe?
9. Qual foi o resultado da execução do script "calculadora.py"?

---

Fim da Aula 03 — Semana 01
