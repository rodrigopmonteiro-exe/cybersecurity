
# Aula 7 — Revisão, avaliação e fechamento da semana

## 1. Revisão dos fundamentos

### 1. O que é o Termux e qual sua relação com o Linux?

O Termux é um aplicativo para Android que oferece um ambiente de terminal Linux, permitindo executar comandos, instalar ferramentas, programas e realizar tarefas de administração de sistema diretamente pelo celular ou tablet.

O Linux é conhecido principalmente como um sistema operacional, mas tecnicamente é o nome do seu núcleo (kernel).

O kernel é a parte central do sistema, responsável por administrar o processador (CPU), memória RAM, dispositivos de armazenamento, processos de execução, comunicação com hardware, permissões e segurança.

**Observação técnica:** O Termux não é uma distribuição Linux completa. Ele utiliza o kernel Linux do Android e fornece seu próprio ambiente de ferramentas e bibliotecas.

Comandos:

```bash
uname -a
whoami
```

- `uname -a`: mostra informações sobre o kernel.
- `whoami`: mostra o usuário atual.

### 2. Qual a diferença entre terminal e shell?

O terminal é a interface onde se digitam comandos e são visualizados os resultados. Já o Shell é o programa que interpreta os comandos digitados e solicita sua execução ao sistema operacional.

### 3. Para que servem pwd, ls, cd e mkdir?

- `pwd`: mostra o diretório atual.
- `ls`: lista arquivos e diretórios.
- `cd`: entra ou muda de diretório.
- `mkdir`: cria um novo diretório (pasta).

### 4. Como executar um arquivo Python?

No Linux, você executa um arquivo Python usando o comando `python`, seguido do nome do arquivo.

Exemplo:

```bash
python teste.py
```

### 5. Qual a diferença entre entrada e saída de um programa?

Entrada (input) são os dados que o programa recebe para processar. Saída (output) são os resultados que o programa apresenta após o processamento.

## 2. Segurança da informação

### 6. O que são confidencialidade, integridade e disponibilidade?

- **Confidencialidade:** somente pessoas autorizadas podem acessar as informações.
- **Integridade:** as informações devem permanecer corretas, completas e sem alteração não autorizada.
- **Disponibilidade:** as informações e os sistemas devem estar acessíveis quando necessário.

### 7. Por que devemos restringir permissões e proteger segredos?

Para evitar acessos não autorizados, vazamentos e alterações indevidas.

### 8. Como comprovar que um programa foi executado corretamente?

Por meio de evidências de execução e testes.

**Principais formas:**

- **Saída esperada:** verificar se o programa apresentou o resultado correto.
- **Testes:** executar diferentes entradas e conferir os resultados.
- **Código de saída:** verificar se terminou sem erros (exit code).
- **Registro de execução:** guardar logs ou capturas de tela como evidência.

Exemplo:

```bash
python teste.py
echo $?
```

Se aparecer `0`, significa que o programa terminou sem indicar erro. O código de saída `0` não garante que a lógica do programa esteja correta.

## 3. Inglês técnico

### Texto

A cybersecurity lab needs a reliable and organized environment. Students use the terminal to execute commands and Python to automate simple tasks. They document their results, protect sensitive information, and verify their work before submitting evidence.

**Tradução:**

Um laboratório de cibersegurança precisa de um ambiente confiável e organizado. Os estudantes usam o terminal para executar comandos e Python para automatizar tarefas simples. Eles documentam seus resultados, protegem informações sensíveis e verificam seu trabalho antes de enviar as evidências.

### Perguntas e respostas

**1. What does a reliable lab need?**

A reliable cybersecurity lab needs more than hardware and software. It needs a controlled, isolated, reproducible, and secure environment where you can experiment, make mistakes, investigate vulnerabilities, simulate attacks, and develop defensive capabilities without compromising real systems.

**Tradução:**

Um laboratório de cibersegurança confiável precisa de mais do que hardware e software. Ele precisa de um ambiente controlado, isolado, reproduzível e seguro, onde você possa experimentar, cometer erros, investigar vulnerabilidades, simular ataques e desenvolver capacidades defensivas sem comprometer sistemas reais.

**2. What do students use the terminal for?**

Students use the terminal to communicate directly with a computer through text commands instead of clicking buttons and navigating graphical menus.

**Tradução:**

Os estudantes usam o terminal para se comunicar diretamente com um computador por meio de comandos de texto, em vez de clicar em botões e navegar por menus gráficos.

**3. Why should students protect sensitive information?**

Students should protect sensitive information because it helps prevent identity theft, cyberattacks, privacy violations, and financial losses.

**Tradução:**

Os estudantes devem proteger informações sensíveis porque isso ajuda a prevenir roubo de identidade, ataques cibernéticos, violações de privacidade e perdas financeiras.

**4. What should students verify before submitting evidence?**

Before submitting evidence, students should verify that it is complete, correct, clear, and properly organized.

**Tradução:**

Antes de enviar evidências, os estudantes devem verificar se elas estão completas, corretas, claras e devidamente organizadas.

## 4. Resumo da semana

- During this week, I learned the basics of cybersecurity and how to use the Linux terminal.
- I practiced Python programming, including variables, input, output, lists and loops.
- I also learned how to organize files, manage file permissions, protect sensitive information, and apply basic security principles.
- Finally, I created a small laboratory project, executed Python scripts, documented my results, and learned the importance of verifying code integrity.

**Tradução:**

- Durante esta semana, aprendi os fundamentos da cibersegurança e como utilizar o terminal Linux.
- Pratiquei programação em Python, incluindo variáveis, entrada, saída, listas e laços de repetição.
- Também aprendi a organizar arquivos, gerenciar permissões de arquivos, proteger informações sensíveis e aplicar princípios básicos de segurança.
- Finalmente, criei um pequeno projeto de laboratório, executei scripts Python, documentei meus resultados e aprendi a importância de verificar a integridade do código.

