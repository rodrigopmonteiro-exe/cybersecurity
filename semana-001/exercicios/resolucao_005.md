# Aula 5 — Segurança básica do ambiente

## 1. Fundamentos da Segurança da Informação

A segurança da informação é baseada em três princípios fundamentais,
conhecidos como Tríade CIA.

### 1.1 Confidencialidade (Confidentiality)

É o princípio que garante que uma informação seja acessada apenas
por pessoas, sistemas ou entidades autorizadas.

### 1.2 Integridade (Integrity)

Protege a informação contra alterações não autorizadas.

Garante que os dados permaneçam corretos, completos e confiáveis.

### 1.3 Disponibilidade (Availability)

Garante que sistemas e dados estejam acessíveis quando necessário.

**Tríade CIA:**
- Confidentiality = Confidencialidade
- Integrity = Integridade
- Availability = Disponibilidade

---

## 2. Como a confidencialidade é protegida?

### 2.1 Autenticação

Verifica quem está tentando acessar um sistema.

Exemplos:
- Senha.
- Autenticação multifator (MFA).
- Biometria.

### 2.2 Controle de acesso

Determina quais recursos cada usuário pode consultar,
modificar ou executar.

### 2.3 Criptografia

Transforma os dados em um formato ilegível para quem
não possui a chave necessária para acessá-los.

### 2.4 Princípio do menor privilégio (Least Privilege)

Cada usuário deve receber apenas as permissões necessárias
para realizar suas atividades.

### 2.5 Proteção de credenciais

Evitar a exposição de senhas, tokens e chaves de acesso privadas.

---

## 3. Exercícios

### Questão 1

Por que uma chave privada não pode ser publicada no Git?

**Resposta:**

Porque ela é um segredo que comprova a capacidade de acessar
sistemas que utilizam aquela chave.

Se outra pessoa obtiver a chave privada, poderá utilizá-la
para se passar pelo proprietário ou acessar recursos protegidos.

Se uma chave privada for exposta:
1. Revogue a chave comprometida.
2. Gere uma nova chave.
3. Atualize os serviços que utilizavam a chave anterior.
4. Verifique se houve algum acesso não autorizado.

**Importante:**
A chave pública pode ser compartilhada.
A chave privada deve permanecer secreta.

---

## 4. Permissões de arquivos no Linux

O Linux utiliza permissões para determinar quem pode acessar,
modificar ou executar arquivos e diretórios.

O comando utilizado para alterar permissões é:

`chmod`

### 4.1 O que significa o modo 600?

É uma configuração de permissões de arquivos no Linux.

Determina quem pode ler, escrever ou executar um arquivo.

Interpretação:

- 6 = Proprietário: leitura e escrita.
- 0 = Grupo: nenhuma permissão.
- 0 = Outros: nenhuma permissão.

### 4.2 Representação numérica das permissões

| Número | Permissão | Significado |
|---|---|---|
| 4 | r (read) | Ler |
| 2 | w (write) | Escrever ou modificar |
| 1 | x (execute) | Executar ou acessar diretórios |

Somamos os valores para combinar permissões:

- 4 = Leitura.
- 2 = Escrita.
- 1 = Execução.
- 6 = Leitura + escrita.
- 7 = Leitura + escrita + execução.
- 0 = Nenhuma permissão.

### 4.3 Exemplos

`chmod 600 arquivo.txt`

Somente o proprietário poderá ler e modificar o arquivo.

`chmod 700 script.sh`

Somente o proprietário poderá ler, modificar e executar o arquivo.

`chmod 644 arquivo.txt`

O proprietário poderá ler e modificar.
Grupo e outros poderão apenas ler.

### 4.4 Aplicação na segurança

O comando chmod é útil para proteger arquivos e chaves privadas SSH.

Exemplo:

`chmod 600 ~/.ssh/id_ed25519`

Esse comando restringe o acesso à chave privada SSH ao proprietário.

**Atenção:**
A chave pública não é secreta. Entretanto, a chave privada
deve ser protegida contra acesso não autorizado.

---

## 5. Riscos de executar comandos copiados da internet

Qual é o risco de executar um comando copiado da internet
sem compreendê-lo?

O risco é realizar uma operação perigosa sem perceber.

Na cibersegurança, isso está relacionado à execução de código
não confiável (Untrusted Code Execution).

### 5.1 Principais riscos

- Roubo de informações (Data Theft):
  Um comando malicioso pode procurar e enviar informações
  privadas, como chaves SSH, senhas armazenadas e tokens.

- Exclusão de arquivos (Data Loss):
  Um comando pode apagar arquivos importantes.

- Infecção por malware:
  Um comando pode instalar programas maliciosos.

- Comprometimento de contas:
  Credenciais podem ser roubadas e utilizadas por terceiros.

- Perda de controle do sistema:
  Um comando pode modificar configurações importantes.

### 5.2 Exemplo prático de comando perigoso

`rm -rf ~/storage/shared/*`

Significado:

- rm = Remove arquivos.
- -r = Remove diretórios recursivamente.
- -f = Força a remoção sem solicitar confirmação.
- ~/storage/shared/* = Todos os itens dentro do diretório
  de armazenamento compartilhado indicado.

**ATENÇÃO: NÃO EXECUTE ESSE COMANDO.**

Ele pode apagar arquivos pessoais do armazenamento
compartilhado do Android.

### 5.3 Uma regra importante

Nunca confunda um comando popular com um comando seguro.

Outro exemplo de risco:

`curl URL | bash`

Em termos gerais, esse padrão baixa conteúdo de um endereço
e o executa imediatamente pelo Bash.

O perigo está em executar o conteúdo recebido sem inspecioná-lo
previamente.

### 5.4 Desenvolvendo o hábito de segurança

Antes de executar qualquer comando:

1. Entenda o que ele faz.
2. Verifique sua origem.
3. Analise os parâmetros utilizados.
4. Identifique os arquivos e diretórios afetados.
5. Verifique se exige privilégios elevados.
6. Execute somente quando compreender os riscos.

---

## 6. Technical English

### Vocabulário técnico

| Inglês | Português |
|---|---|
| Access Control | Controle de acesso |
| File Permissions | Permissões de arquivos |
| Sensitive Information | Informação sensível |
| Authorized Testing | Teste autorizado |
| Malicious Command | Comando malicioso |
| Remote Code Execution | Execução remota de código |
| Privilege Escalation | Escalonamento de privilégios |

### Frases técnicas

**Never expose private keys or passwords in public repositories.**

Nunca exponha chaves privadas ou senhas em repositórios públicos.

**Confidentiality ensures that information is accessible only
to authorized users.**

A confidencialidade garante que as informações sejam acessíveis
somente a usuários autorizados.

**Technical vocabulary:**

- Access Control = Controle de acesso.
- File Permissions = Permissões de arquivos.
- Sensitive Information = Informação sensível.
- Authorized Testing = Teste autorizado.
- Malicious Command = Comando malicioso.
- Remote Code Execution = Execução remota de código.
- Privilege Escalation = Escalonamento de privilégios.

---

## 7. Revisão da aula

Nesta aula foram estudados:

- Os três princípios da segurança da informação (CIA).
- Confidencialidade, integridade e disponibilidade.
- Autenticação e controle de acesso.
- Criptografia e proteção de credenciais.
- Princípio do menor privilégio.
- Permissões de arquivos no Linux.
- Funcionamento do comando chmod.
- Proteção de chaves privadas SSH.
- Riscos de executar comandos desconhecidos.
- Execução de código não confiável.
- Vocabulário técnico em inglês.

**Objetivo alcançado:**

Compreender os fundamentos da segurança do ambiente Linux
e desenvolver hábitos seguros durante a utilização do Termux.
