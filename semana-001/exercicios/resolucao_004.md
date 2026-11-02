CIBERSEGURANÇA

Semana 01 — Aula 04: Linux e Organização de Pastas

---

1. Comandos Essenciais do Linux

Os comandos Linux permitem navegar pelo sistema de arquivos, criar diretórios, manipular arquivos e organizar o ambiente de trabalho.

1.1 "pwd" — Print Working Directory

Mostra o diretório de trabalho atual.

pwd

1.2 "ls" — List

Lista arquivos e diretórios.

ls

Para incluir arquivos ocultos:

ls -la

- "-l": Exibe informações detalhadas em formato longo.
- "-a": Inclui arquivos e diretórios ocultos.

1.3 "cd" — Change Directory

Muda de diretório.

cd nome-da-pasta

Para voltar ao diretório anterior:

cd ..

Para voltar ao diretório pessoal:

cd ~

1.4 "mkdir" — Make Directory

Cria diretórios.

mkdir nome-da-pasta

Para criar uma estrutura completa de diretórios, mesmo quando os diretórios pais ainda não existem:

mkdir -p projeto/semana1/anotacoes

A opção "-p" significa criar os diretórios pais necessários.

1.5 "touch"

Cria um arquivo vazio caso ele ainda não exista.

touch arquivo.txt

Se o arquivo já existir, atualiza seus horários de acesso e modificação, sem apagar seu conteúdo.

1.6 "cat" — Concatenate

Exibe o conteúdo de arquivos.

cat arquivo.txt

Também pode concatenar conteúdos de vários arquivos.

1.7 "cp" — Copy

Copia arquivos.

cp arquivo.txt copia.txt

Para copiar diretórios e seu conteúdo:

cp -r pasta-original pasta-copia

1.8 "mv" — Move

Move ou renomeia arquivos e diretórios.

Para renomear:

mv arquivo-antigo.txt arquivo-novo.txt

Para mover:

mv arquivo.txt pasta/

1.9 "rm" — Remove

Remove arquivos.

rm arquivo.txt

Para remover diretórios e seus conteúdos:

rm -r nome-da-pasta

Atenção: o comando "rm" pode apagar arquivos permanentemente. Sempre confira o caminho antes de executá-lo.

1.10 "find"

Procura arquivos e diretórios.

find . -name "arquivo.txt"

Nesse exemplo:

- "." representa o diretório atual.
- "-name" indica o nome que será procurado.
- ""arquivo.txt"" é o nome do arquivo procurado.

1.11 "clear"

Limpa a tela do terminal, sem apagar o histórico dos comandos executados.

clear

---

2. Parâmetros e Opções dos Comandos

É importante compreender que os parâmetros modificam o comportamento dos comandos.

2.1 Opção "-p"

Utilizada com "mkdir", permite criar diretórios pais necessários.

Exemplo:

mkdir -p projeto/semana1/anotacoes

2.2 Opção "-l"

Geralmente significa formato longo (Long Listing Format), como no comando "ls".

Exemplo:

ls -l

Em vez de mostrar apenas os nomes, apresenta informações detalhadas sobre os arquivos e diretórios.

Essas informações incluem:

- Permissões.
- Número de ligações.
- Proprietário.
- Grupo.
- Tamanho.
- Data e horário da última modificação.
- Nome do arquivo.

2.3 Opções combinadas

As opções podem ser combinadas.

Exemplo:

ls -la

Esse comando apresenta arquivos ocultos e informações detalhadas.

---

3. Exercícios e Respostas

Exercício 1 — Por que usar nomes de pastas padronizados?

Para manter o projeto organizado, previsível e fácil de administrar, mesmo quando ele cresce.

Também é recomendável:

- Utilizar letras minúsculas.
- Evitar espaços e acentos nos nomes.
- Separar palavras com hífen ("-") ou sublinhado ("_").
- Utilizar nomes claros e descritivos.

Exemplos:

semana-01
aula-01
laboratorio-linux
anotacoes-python

Essa padronização facilita a navegação, a automação e a administração dos projetos.

Exercício 2 — Como verificar se um arquivo foi copiado corretamente?

Existem três métodos principais.

A) Método simples: verificar a existência

Verifique se o arquivo original e o arquivo copiado aparecem no diretório.

ls -l

A presença dos dois arquivos confirma que ambos existem, mas não garante que seus conteúdos sejam idênticos.

B) Método intermediário: comparar o conteúdo

Utilize o comando "diff".

diff arquivo-original.txt arquivo-copia.txt

Se não houver saída, os arquivos de texto possuem conteúdo idêntico.

Se aparecerem diferenças, os conteúdos não são iguais.

Esse método é útil para arquivos de texto, como ".md", ".txt" e ".py".

C) Método profissional: comparar hashes SHA-256

O hash funciona como uma impressão digital do arquivo.

Utilize:

sha256sum arquivo-original.txt
sha256sum arquivo-copia.txt

Se os dois arquivos apresentarem o mesmo hash SHA-256, existe uma evidência muito forte de que seus conteúdos são idênticos.

Importante: SHA-256 permite verificar integridade, mas não comprova, sozinho, a autenticidade ou a origem de um arquivo.

---

4. Organização do Ambiente de Cibersegurança

Uma boa organização de diretórios facilita o desenvolvimento de projetos, a documentação e a análise de evidências.

Exemplo de estrutura:

cybersecurity/
|
|-- semana-01/
|   |
|   |-- aula-01/
|   |-- aula-02/
|   |-- aula-03/
|   |-- aula-04/
|   |
|   |-- exercicios/
|   |-- laboratorios/
|   |-- evidencias/
|
|-- semana-02/
|
|-- projetos/
|
|-- scripts/
|
|-- relatorios/
|
|-- notas/

Cada pasta possui uma finalidade:

- Aulas: Material teórico e anotações.
- Exercícios: Respostas e atividades.
- Laboratórios: Práticas realizadas.
- Evidências: Registros dos resultados obtidos.
- Projetos: Trabalhos práticos.
- Scripts: Códigos desenvolvidos.
- Relatórios: Documentação técnica.
- Notas: Anotações complementares.

---

5. Verificação da Integridade de Arquivos

A integridade é um conceito fundamental da cibersegurança.

Quando copiamos ou transferimos um arquivo, precisamos verificar se ele chegou corretamente e se seu conteúdo não foi alterado.

5.1 O que é SHA-256?

SHA-256 é uma função de hash criptográfico que produz uma saída de 256 bits, normalmente representada por 64 caracteres hexadecimais.

Exemplo de utilização:

sha256sum arquivo.txt

Se o conteúdo do arquivo mudar, seu hash normalmente também mudará.

5.2 Git e controle de alterações

O Git é um sistema de controle de versão que permite acompanhar alterações nos arquivos de um projeto.

Ele é útil para:

- Registrar modificações.
- Comparar versões.
- Recuperar versões anteriores.
- Acompanhar o desenvolvimento de projetos.
- Manter o histórico de alterações.

Exemplo:

git status

Mostra o estado atual do repositório.

---

6. Technical English — Inglês Técnico

6.1 Vocabulário

Inglês| Português
Create a directory for your lab files| Crie um diretório para seus arquivos de laboratório
Copy the file into the evidence folder| Copie o arquivo para a pasta de evidências
Verify the file contents before submitting| Verifique o conteúdo do arquivo antes de enviar
Folders| Pastas
File names| Nomes de arquivos
File integrity| Integridade dos arquivos
Track changes| Acompanhar alterações
Consistent| Consistente / Padronizado
Evidence folder| Pasta de evidências

6.2 Prática de escrita

English:

I organized my cybersecurity lab into folders by week and lesson. Each folder contains Python exercises, notes, and reports. I used clear and consistent file names to keep everything organized and easy to find. I also used Git to track changes and SHA-256 hashes to verify file integrity.

Português:

Organizei meu laboratório de cibersegurança em pastas por semana e aula. Cada pasta contém exercícios de Python, anotações e relatórios. Utilizei nomes de arquivos claros e padronizados para manter tudo organizado e fácil de encontrar. Também utilizei o Git para acompanhar alterações e hashes SHA-256 para verificar a integridade dos arquivos.

---

7. Registro de Aprendizagem

Semana: 01

Aula: 04

Tema: Linux e organização de pastas.

Principais conhecimentos adquiridos

- Navegação pelo sistema de arquivos Linux.
- Utilização de "pwd", "ls" e "cd".
- Criação de diretórios com "mkdir".
- Criação de arquivos com "touch".
- Leitura de arquivos com "cat".
- Cópia de arquivos com "cp".
- Movimentação e renomeação com "mv".
- Remoção de arquivos com "rm".
- Pesquisa de arquivos com "find".
- Limpeza da tela com "clear".
- Utilização de parâmetros e opções.
- Organização de projetos e laboratórios.
- Comparação de arquivos com "diff".
- Verificação de integridade com SHA-256.
- Controle de versões com Git.
- Vocabulário técnico em inglês.

Evidências da aula

- Anotações manuscritas.
- Exercícios respondidos.
- Execução dos comandos no Termux.
- Estrutura de diretórios criada.
- Teste de cópia e comparação de arquivos.
- Verificação de integridade com SHA-256.

---

8. Revisão da Aula

Responda sem consultar suas anotações:

1. Qual é a diferença entre "cp" e "mv"?
2. Para que serve o comando "mkdir -p"?
3. Qual é a diferença entre "ls" e "ls -la"?
4. Para que serve o comando "find"?
5. Qual é a diferença entre "rm" e "rmdir"?
6. Como podemos verificar se dois arquivos possuem conteúdos idênticos?
7. O que é SHA-256?
8. Qual é a finalidade do Git?
9. Por que devemos padronizar os nomes de arquivos e diretórios?
10. O que significa integridade de arquivos no contexto da cibersegurança?

---

Fim da Aula 04 — Semana 01
