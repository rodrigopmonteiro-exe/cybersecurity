Aula 2 — Termux e ambiente de estudo

Data: 27/10/2026
Duração: 2 horas
Módulo: Semana 1 — Fundamentos e preparação do ambiente

Objetivo

Verificar o ambiente de execução e compreender como o Termux fornece ferramentas Linux no Android.

---

Parte A — Conceitos (20 min)

Estude estes conceitos:

- Terminal: interface para executar comandos.
- Shell: programa que interpreta os comandos digitados.
- Pacote: conjunto de arquivos instalado para disponibilizar um programa.
- Repositório: fonte de pacotes.
- Dependência: componente necessário para outro programa funcionar.

O Termux oferece um ambiente de terminal Linux no Android, mas não é idêntico a uma instalação convencional de Linux para computador.

---

Parte B — Inspeção do ambiente (30 min)

Execute um comando por vez:

whoami
pwd
uname -a
echo $PREFIX
command -v python
command -v git

Anote o que cada comando retorna.

O comando "command -v" verifica se um executável está disponível no ambiente atual.

Se o Python ou Git não estiver instalado, registre isso antes de instalar.

O que observar

- "whoami": identifica o usuário atual.
- "pwd": mostra o diretório de trabalho atual.
- "uname -a": apresenta informações do sistema.
- "echo $PREFIX": mostra o caminho do prefixo do Termux.
- "command -v python": verifica a disponibilidade do Python.
- "command -v git": verifica a disponibilidade do Git.

---

Parte C — Atualização e verificação (30 min)

Execute:

pkg update

Leia a saída e observe se existem erros.

Depois, se necessário, atualize os pacotes instalados:

pkg upgrade

Confirme a operação antes de prosseguir e não interrompa uma atualização em andamento sem necessidade.

Instalação condicional do Python

Se o Python ainda não estiver disponível:

pkg install python

Instalação condicional do Git

Se o Git ainda não estiver disponível:

pkg install git

Verificação final

Verifique novamente:

python --version
git --version

Registre os resultados.

---

Parte D — Exercícios (25 min)

Responda às questões:

1. Qual sistema operacional está executando o Termux?
2. O que é um pacote?
3. Qual a diferença entre "pkg update" e "pkg upgrade"?
4. O que significa um comando não ser encontrado?o
5. Execute os comandos de verificação e registre os resultados.

---

Parte E — Technical English (15 min)

1. Traduza as frases

- The package manager checks available updates.
- The Python interpreter is installed.
- The command was not found.

2. Vocabulário técnico

Inglês| Português
Package manager| Gerenciador de pacotes
Available| Disponível
Updates| Atualizações
Installed| Instalado
Terminal| Terminal
Command| Comando
Python interpreter| Interpretador Python

3. Produção escrita

Escreva duas frases sobre seu ambiente usando as palavras:

- "installed"
- "available"
- "terminal"

---

Evidências da aula

Registre os resultados dos comandos:

python --version
git --version

Guarde capturas de tela dos resultados e registre eventuais erros encontrados durante a atividade.

---

Critério de conclusão

A aula será considerada concluída quando você conseguir:

- Explicar os conceitos de terminal, shell, pacote, repositório e dependência.
- Identificar informações básicas do ambiente Termux.
- Diferenciar atualização da lista de pacotes e atualização dos pacotes instalados.
- Verificar a disponibilidade e as versões do Python e Git.
- Responder aos exercícios.
- Realizar a atividade de inglês técnico.
- Registrar as evidências e dificuldades.
