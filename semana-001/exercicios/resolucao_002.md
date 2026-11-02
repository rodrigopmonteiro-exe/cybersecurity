CIBERSEGURANÇA

Semana 01 — Aula 02: Ambiente de Estudo

---

1. Permissões e Privilégios no Linux

1.1 O que são permissões elevadas?

Normalmente, um usuário possui permissões limitadas sobre os arquivos e recursos do sistema.

Um administrador ou usuário com privilégios elevados pode realizar operações que um usuário comum não pode.

No Linux, o usuário "root" possui privilégios administrativos muito amplos.

Um profissional de segurança verifica a origem, analisa o comportamento, minimiza os privilégios (Least Privilege) e os riscos antes de executar códigos desconhecidos.

---

2. Conceitos Fundamentais do Ambiente de Estudo

- Terminal: Interface para executar comandos.
- Shell: Programa que interpreta os comandos digitados.
- Pacote (Package): Conjunto de arquivos instaláveis que disponibiliza um programa ou recurso.
- Repositório (Repository): Fonte onde os pacotes ficam armazenados e são disponibilizados para instalação.
- Dependência (Dependency): Componente necessário para que outro programa funcione corretamente.

Diferença entre Terminal e Shell

O terminal é a interface utilizada para digitar e visualizar comandos.

O Shell é o programa responsável por interpretar esses comandos e solicitar sua execução ao sistema operacional.

---

3. Explicação dos Comandos

3.1 Identificação do usuário

"whoami"

Identifica o usuário atual associado à sessão do terminal.

whoami

"id"

Mostra a identidade numérica do usuário atual e os grupos aos quais ele pertence.

id

No Linux, o UID 0 corresponde ao usuário "root", que possui privilégios administrativos amplos.

3.2 Diretório de trabalho

"pwd"

Mostra o diretório de trabalho atual.

pwd

3.3 Informações do sistema

"uname -a"

Exibe informações sobre o sistema, incluindo nome do kernel, versão, arquitetura e outros dados disponíveis.

- "uname": Exibe informações do sistema.
- "-a": Significa apresentar todas as informações disponibilizadas por esse comando.

uname -a

3.4 Variáveis de ambiente

"echo $PREFIX"

Exibe o valor de uma variável de ambiente.

- "echo": Imprime um texto ou valor no terminal.
- "$PREFIX": Solicita o valor armazenado na variável "PREFIX".

echo $PREFIX

No Termux, essa variável normalmente indica o diretório principal do ambiente, geralmente:

/data/data/com.termux/files/usr

3.5 Localização de programas

"command -v python"

Verifica se o comando Python está disponível e onde ele está localizado.

command -v python

"command -v git"

Verifica se o comando Git está disponível e onde ele está localizado.

command -v git

Esses comandos ajudam a verificar se os programas estão acessíveis pelo terminal.

---

4. Gerenciamento de Pacotes no Termux

O Termux utiliza o gerenciador de pacotes "pkg", que facilita a instalação e atualização de programas.

4.1 Atualização dos repositórios

"pkg update"

Consulta os repositórios e atualiza as listas de versões dos programas disponíveis para instalação.

Imagine uma loja de aplicativos: antes de saber quais versões estão disponíveis, você atualiza o catálogo.

pkg update

Importante: Esse comando atualiza as listas de pacotes, mas não atualiza, por si só, os programas já instalados.

4.2 Atualização dos programas instalados

"pkg upgrade"

Instala as versões mais recentes disponíveis dos pacotes que você já possui, respeitando as dependências.

pkg upgrade

Essa atualização pode corrigir erros, melhorar o desempenho e corrigir vulnerabilidades de segurança.

4.3 Verificação da versão do Python

python --version

Mostra a versão do Python instalada e disponível no terminal.

4.4 Verificação da versão do Git

git --version

Mostra a versão do Git instalada.

4.5 Instalação de programas

"pkg install nome-do-programa"

Instala um programa disponível nos repositórios configurados do Termux.

Exemplo:

pkg install python

Outro exemplo:

pkg install git

---

5. Technical English — Inglês Técnico

5.1 Vocabulário

Inglês| Português
Package manager| Gerenciador de pacotes
Available updates| Atualizações disponíveis
Python interpreter| Interpretador Python
Command not found| Comando não encontrado
Installed| Instalado
Repository| Repositório
Dependency| Dependência
Working environment| Ambiente de trabalho

5.2 Frases técnicas

1. The package manager checks available updates.

O gerenciador de pacotes verifica as atualizações disponíveis.

2. The Python interpreter is installed.

O interpretador Python está instalado.

3. The command was not found.

O comando não foi encontrado.

4. Python is installed in my Termux environment.

O Python está instalado no meu ambiente Termux.

5. The terminal provides the commands and tools available for my cybersecurity studies.

O terminal disponibiliza os comandos e ferramentas necessários para meus estudos de cibersegurança.

---

6. Exercícios e Respostas

Exercício 1 — O que significa um comando não ser encontrado?

Quando aparece a mensagem "command not found", significa que o Shell não conseguiu localizar o comando que você tentou executar.

Isso pode acontecer por alguns motivos:

1. O comando foi escrito incorretamente.
2. O programa não está instalado.
3. O programa está fora dos diretórios de pesquisa do sistema (PATH).
4. O comando não existe ou não está disponível naquele ambiente.

Como investigar:

Primeiro, verifique se escreveu o comando corretamente.

Depois, utilize:

command -v nome-do-programa

Se o programa não estiver instalado, verifique se ele está disponível nos repositórios antes de instalá-lo.

---

7. Prática de Laboratório — Termux

7.1 Objetivo

Verificar o ambiente de estudo, identificar o usuário, consultar informações do sistema e confirmar a disponibilidade das ferramentas fundamentais.

7.2 Comandos para executar

Execute cada comando individualmente no Termux:

Etapa 1 — Identificação

whoami
id

Etapa 2 — Diretório atual

pwd

Etapa 3 — Informações do sistema

uname -a

Etapa 4 — Variável de ambiente

echo $PREFIX

Etapa 5 — Verificação do Python

command -v python
python --version

Etapa 6 — Verificação do Git

command -v git
git --version

Etapa 7 — Atualização dos pacotes

pkg update
pkg upgrade

---

8. Registro de Aprendizagem

Semana: 01

Aula: 02

Tema: Ambiente de estudo.

Principais conhecimentos adquiridos

- Diferença entre terminal e Shell.
- Conceitos de pacotes, repositórios e dependências.
- Identificação do usuário com "whoami".
- Identificação de usuários e grupos com "id".
- Verificação do diretório atual com "pwd".
- Consulta de informações do sistema com "uname -a".
- Consulta de variáveis de ambiente com "echo".
- Localização de programas com "command -v".
- Gerenciamento de pacotes com "pkg".
- Atualização de repositórios e programas.
- Instalação de ferramentas no Termux.
- Vocabulário técnico em inglês.

Evidências da aula

- Anotações manuscritas.
- Exercícios respondidos.
- Execução dos comandos no Termux.
- Verificação do Python e Git.
- Registro de eventuais erros e suas soluções.

---

9. Revisão da Aula

Responda sem consultar suas anotações:

1. Qual é a diferença entre terminal e Shell?
2. Para que serve o comando "whoami"?
3. Qual é a diferença entre "pkg update" e "pkg upgrade"?
4. Para que serve o comando "command -v"?
5. O que significa a mensagem "command not found"?
6. O que é uma dependência?
7. Por que devemos manter os pacotes atualizados?

---

Fim da Aula 02 — Semana 01
