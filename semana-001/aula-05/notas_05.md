Aula 5 — Segurança básica do ambiente

Data:30/10/2026
Duração: 2 horas e 30 minutos

Objetivo: aprender a reduzir riscos no ambiente de estudo antes de trabalhar com ferramentas de cibersegurança.

---

Parte A — Fundamentos (30 min)

Estude os conceitos:

- Confidencialidade: impedir acesso indevido à informação.
- Integridade: proteger a informação contra alterações não autorizadas.
- Disponibilidade: manter sistemas e dados acessíveis quando necessários.
- Privilégio mínimo: conceder somente as permissões necessárias.
- Superfície de ataque: conjunto de pontos pelos quais um sistema pode ser atacado.
- Segredo: senha, token, chave privada ou outra informação que não deve ser exposta.

---

Parte B — Checklist de segurança (30 min)

Marque cada item somente depois de verificar:

Checklist de segurança

- [ ] O Termux e seus pacotes estão atualizados ou os erros de atualização foram registrados.
- [ ] Não compartilho senhas, tokens ou chaves privadas em capturas de tela.
- [ ] Não executo comandos desconhecidos sem entender seus efeitos.
- [ ] Instalo ferramentas somente de fontes confiáveis.
- [ ] Mantenho os arquivos de estudo organizados e preservo os originais.
- [ ] Utilizo apenas sistemas e laboratórios que tenho autorização para testar.

Observação: esse checklist é uma autoavaliação, não uma certificação de que o ambiente está seguro.

---

Parte C — Permissões e arquivos (35 min)

1. Crie um arquivo de teste

cd ~/cybersecurity/semana-01/aula-05
printf 'Arquivo de teste\n' > exemplo.txt
ls -l exemplo.txt

Observe as permissões exibidas. Em sistemas Unix, elas normalmente são apresentadas com símbolos como "r", "w" e "x", correspondendo a leitura, escrita e execução.

2. Aplique permissões restritas ao arquivo de teste

chmod 600 exemplo.txt
ls -l exemplo.txt

3. Interprete o resultado

"600" permite leitura e escrita ao proprietário e nenhuma permissão aos demais usuários.

Essa é uma prática de restrição para o arquivo de exemplo, não uma regra universal para todos os arquivos.

Importante: o Termux funciona com o modelo de permissões do Android. Não presuma que seu usuário tenha acesso de root.

---

Parte D — Exercícios (30 min)

1. Explique confidencialidade, integridade e disponibilidade com um exemplo de cada.
2. Por que uma chave privada não deve ser publicada no Git?
3. O que significa o modo "600"?
4. Qual o risco de executar um comando copiado da internet sem compreendê-lo?
5. Explique o princípio do privilégio mínimo.

---

Parte E — Technical English (25 min)

Vocabulário

- Access control — controle de acesso.
- File permissions — permissões de arquivo.
- Least privilege — privilégio mínimo.
- Sensitive information — informação sensível.
- Authorized testing — teste autorizado.

Traduza

"Never expose private keys or passwords in public repositories."

---

Evidências da aula

- [ ] Arquivo "exemplo.txt".
- [ ] Saída de "ls -l" antes do "chmod".
- [ ] Saída de "ls -l" depois do "chmod".
- [ ] Checklist de segurança preenchido.
- [ ] Respostas dos cinco exercícios.
- [ ] Tradução da frase em inglês.
