Aula 4 — Linux e organização de pastas

Data:29/10/2026
Duração: 2 horas e 30 minutos

Objetivo: dominar a navegação básica no terminal e estruturar seu repositório de aprendizagem.

---

Parte A — Comandos essenciais (30 min)

Comando| Função
"pwd"| Mostra o diretório atual
"ls"| Lista arquivos e diretórios
"cd"| Muda de diretório
"mkdir"| Cria diretórios
"touch"| Cria arquivo vazio, se não existir
"cat"| Exibe o conteúdo de arquivos
"cp"| Copia arquivos
"mv"| Move ou renomeia arquivos
"rm"| Remove arquivos
"find"| Procura arquivos e diretórios

Parte B — Laboratório de organização (45 min)

1. Monte a estrutura

mkdir -p ~/cybersecurity/semana-01/aula-04
mkdir -p ~/cybersecurity/semana-01/evidencias
mkdir -p ~/cybersecurity/semana-01/exercicios

2. Crie um arquivo de teste

cd ~/cybersecurity/semana-01/exercicios
touch teste.txt
echo "Primeiro registro de laboratório" > teste.txt
cat teste.txt

3. Copie o arquivo para a pasta de evidências

cp teste.txt ../evidencias/teste.txt

4. Confirme o resultado

ls -l ../evidencias
cat ../evidencias/teste.txt

5. Pratique também a navegação

cd ..
pwd
cd ~
pwd

Atenção: entenda a diferença entre "~", que representa o diretório pessoal, e um caminho relativo, como "../evidencias/teste.txt".

---

Parte C — Desafio prático (40 min)

Sem copiar a sequência anterior, crie a estrutura abaixo dentro de "~/cybersecurity/semana-01/":

semana-01/
├── aula-01/
├── aula-02/
├── aula-03/
├── aula-04/
├── exercicios/
├── evidencias/
└── relatorio.md

O arquivo "relatorio.md" deverá conter:

- Data.
- Comandos utilizados.
- Resultado esperado.
- Resultado obtido.
- Dificuldades e correções.

Importante: se já houver arquivos nessas pastas, preserve-os. Não apague o trabalho anterior para recriar a estrutura.

---

Parte D — Exercícios (20 min)

1. Qual a diferença entre "cp" e "mv"?
2. O que acontece com "cd .."?
3. Como visualizar arquivos ocultos?
4. Por que usar nomes de pastas padronizados?
5. Como verificar se um arquivo foi copiado corretamente?

Execute o comando de visualização de arquivos ocultos:

ls -la

---

Parte E — Technical English (15 min)

Traduza:

- "Create a directory for your lab files."
- "Copy the file into the evidence folder."
- "Verify the file contents before submitting."

Escreva um pequeno parágrafo em inglês explicando como organizou seu laboratório.

---

Evidências da aula

- [ ] Captura da árvore de pastas.
- [ ] Captura da saída de "ls -la".
- [ ] Arquivo "relatorio.md".
- [ ] Registro dos exercícios respondidos.
- [ ] Pequeno parágrafo em inglês.

---

Critério de conclusão

Você deverá conseguir:

1. Explicar a função dos comandos Linux estudados.
2. Navegar entre diretórios sem depender de exemplos.
3. Criar, copiar e verificar arquivos.
4. Organizar seu repositório de aprendizagem.
5. Documentar o laboratório em Markdown.
