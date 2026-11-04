# SEMANA 002 — AULA 10
# DECOMPOSIÇÃO DE PROBLEMAS

---

# 1. O QUE É DECOMPOSIÇÃO?

Decomposição é o processo de dividir um problema complexo em partes menores, mais simples e fáceis de compreender, analisar e resolver.

Imagine que você precisa investigar um incidente de segurança em uma rede.

Você pode decompor essa investigação em:

- Identificação do incidente.
- Coleta de evidências.
- Análise dos registros (logs).
- Identificação da possível vulnerabilidade.
- Avaliação dos danos.
- Contenção da ameaça.
- Recuperação dos sistemas.
- Elaboração de relatórios.

Isso permite investigar problemas complexos de maneira organizada.

---

# 2. PROBLEMAS COMPLEXOS E PROBLEMAS MENORES

## 2.1. Problemas complexos

São problemas que possuem muitas partes, etapas, condições ou variáveis, tornando sua resolução difícil quando tentamos executá-los de uma só vez.

Exemplo: desenvolver um sistema de segurança para uma empresa.

Esse problema envolve:

- Identificação de usuários.
- Autenticação e controle de acesso.
- Proteção de dados.
- Monitoramento de atividades.
- Detecção de ameaças.
- Resposta a incidentes.

## 2.2. Problemas menores

São partes menores de um problema complexo, separadas para facilitar sua compreensão e resolução.

No exemplo anterior, podemos dividir o desenvolvimento do sistema em tarefas:

1. Criar um sistema de cadastro de usuários.
2. Implementar autenticação por senha.
3. Desenvolver controle de permissões.
4. Registrar tentativas de acesso.
5. Criar alertas de atividades suspeitas.
6. Implementar mecanismos de proteção de dados.

Cada tarefa pode ser desenvolvida, testada e corrigida individualmente.

---

# 3. MODULARIZAÇÃO (MODULARIZATION)

Modularização é uma técnica de desenvolvimento de software que consiste em dividir um programa ou sistema complexo em partes menores, independentes e organizadas, chamadas módulos.

Cada módulo é responsável por executar uma tarefa específica e pode ser desenvolvido, testado, corrigido e reutilizado separadamente.

A ideia central é:

Dividir para organizar, organizar para facilitar a manutenção.

## 3.1. Relação entre decomposição e reutilização de código

A decomposição permite dividir um problema complexo em partes menores, enquanto a reutilização permite aproveitar essas partes em diferentes situações, sem precisar escrever o mesmo código novamente.

Imagine que você queira desenvolver um programa de cadastro de usuários.

Em vez de construir tudo em um único bloco de código, podemos dividir o programa em tarefas:

1. Solicitar o nome do usuário.
2. Solicitar a idade.
3. Validar os dados.
4. Exibir os resultados.

Cada tarefa pode ser desenvolvida separadamente.

### Reutilização

Aproveitar o que já foi desenvolvido.

Depois de dividir o problema, podemos transformar algumas dessas tarefas em funções.

---

# 4. FUNÇÕES EM PYTHON

## 4.1. O que é uma função?

É um bloco de código criado para realizar uma tarefa específica.

Exemplos:

- Uma função pode pedir o nome de alguém.
- Outra pode calcular uma idade.
- Outra pode apresentar informações na tela.

A grande vantagem é que podemos reutilizar uma função várias vezes, sem precisar escrever todo o código novamente.

## 4.2. Como criar uma função em Python?

Exemplo:

    def cumprimento():
        print("Olá! Seja bem-vindo!")

### Explicação:

- `def`: palavra reservada em Python utilizada para criar uma função.
- `cumprimento`: nome da função que definimos.
- `()`: podem receber informações que a função utilizará.
- `:`: indica o início do bloco de código da função.
- `print()`: é a instrução que será executada quando chamarmos a função.

Importante: Quando uma função é criada, ela não é executada imediatamente.

Para executá-la, precisamos chamá-la:

    def cumprimento():
        print("Olá! Seja bem-vindo!")

    cumprimento()

### Resultado:

    Olá! Seja bem-vindo!

`cumprimento()` representa a chamada da função.

---

# 5. FUNÇÕES E ORGANIZAÇÃO DE PROGRAMAS

Podemos dividir um programa em funções para tornar o código mais fácil de entender e organizar.

Cada função tem uma responsabilidade específica e executa uma tarefa menor.

Isso também melhora a reutilização do código e facilita sua manutenção.

## 5.1. Exemplo: sistema de cadastro

    def solicitar_nome():
        return input("Digite seu nome: ")

    def solicitar_idade():
        return int(input("Digite sua idade: "))

    def apresentar_resultado(nome, idade):
        print("\nCADASTRO")
        print("Nome:", nome)
        print("Idade:", idade)

    nome = solicitar_nome()
    idade = solicitar_idade()

    apresentar_resultado(nome, idade)

## 5.2. Entendendo o funcionamento

1. `solicitar_nome()` solicita o nome e devolve o valor digitado.
2. `solicitar_idade()` solicita a idade e converte o texto recebido em número inteiro.
3. `apresentar_resultado()` recebe o nome e a idade e apresenta os dados.
4. As variáveis `nome` e `idade` armazenam os valores retornados pelas funções.
5. A última linha chama a função responsável pela apresentação do cadastro.

---

# 6. DECOMPOSIÇÃO DO DESENVOLVIMENTO DE UMA CALCULADORA

Primeiro, dividimos o problema principal em problemas menores.

1. Definir funcionalidades: determinar o que a calculadora fará.
2. Identificar entradas: definir quais dados serão recebidos.
3. Identificar saídas: definir quais resultados serão apresentados.
4. Planejar operações: definir os cálculos disponíveis.
5. Criar a estrutura: organizar o código.
6. Implementar operações: programar os cálculos.
7. Criar o menu: permitir escolher uma operação.
8. Integrar os módulos: conectar todas as funcionalidades.
9. Tratar erros: evitar falhas durante a execução.
10. Testar: verificar se tudo funciona corretamente.

---

# 7. O QUE ACONTECE QUANDO TODAS AS RESPONSABILIDADES FICAM EM UMA ÚNICA PARTE DO PROGRAMA?

Isso pode causar cinco problemas:

1. Dificuldade de manutenção: qualquer alteração pode afetar várias partes do programa.
2. Dificuldade de identificação de erros: fica mais complicado descobrir exatamente onde ocorreu um problema.
3. Baixa reutilização: fica difícil aproveitar uma parte específica do código em outro programa.
4. Dificuldade de compreensão: o código fica extenso e complexo.
5. Maior risco de falhas: uma mudança em uma responsabilidade pode comprometer outras funcionalidades.

---

# 8. CONCEITO FUNDAMENTAL: SEPARAÇÃO DE RESPONSABILIDADES

Esse princípio está relacionado à separação de responsabilidades (Separation of Concerns).

Cada parte do programa deve ter uma responsabilidade bem definida, evitando que uma única parte precise cuidar de tudo.

---

# 9. EXERCÍCIOS E RESPOSTAS

## Questão 1 — Qual a relação entre decomposição e reutilização de código?

A decomposição permite dividir um problema complexo em partes menores, enquanto a reutilização permite aproveitar essas partes em diferentes situações, sem precisar escrever o mesmo código novamente.

## Questão 2 — Divida o desenvolvimento de um programa de cadastro de usuários em etapas.

1. Solicitar o nome do usuário.
2. Solicitar a idade.
3. Validar os dados.
4. Exibir os resultados.

Cada tarefa pode ser desenvolvida separadamente.

## Questão 3 — Explique o que aconteceria se todas as responsabilidades estivessem concentradas em uma única parte do programa.

Isso pode causar cinco problemas:

1. Dificuldade de manutenção: qualquer alteração pode afetar várias partes do programa.
2. Dificuldade de identificação de erros: fica mais complicado descobrir exatamente onde ocorreu um problema.
3. Baixa reutilização: fica difícil aproveitar uma parte específica do código em outro programa.
4. Dificuldade de compreensão: o código fica extenso e complexo.
5. Maior risco de falhas: uma mudança em uma responsabilidade pode comprometer outras funcionalidades.

---

# 10. TECHNICAL ENGLISH

## Vocabulário técnico

| Inglês | Português |
|---|---|
| Decomposition | Decomposição |
| Function | Função |
| Module | Módulo |
| Task | Tarefa |
| Responsibility | Responsabilidade |
| Reusability | Reutilização |

## Traduções e expressões

- Dividing a program into functions makes the code easier to understand and organize.

  Dividir um programa em funções torna o código mais fácil de entender e organizar.

- Each function has a specific responsibility and performs a smaller task.

  Cada função tem uma responsabilidade específica e executa uma tarefa menor.

- It also improves code reusability and makes debugging and maintenance easier.

  Isso também melhora a reutilização do código e facilita a identificação de erros e a manutenção.

---

# 11. PRÁTICA — LABORATÓRIO PYTHON

## 11.1. Criação do arquivo

    nano aula10.py

## 11.2. Código desenvolvido

    def solicitar_nome():
        return input("Digite seu nome: ")

    def solicitar_idade():
        return int(input("Digite sua idade: "))

    def apresentar_resultado(nome, idade):
        print("\nCADASTRO")
        print("Nome:", nome)
        print("Idade:", idade)

    nome = solicitar_nome()
    idade = solicitar_idade()

    apresentar_resultado(nome, idade)

## 11.3. Execução no Termux

    python aula10.py

## 11.4. Resultado obtido

    Digite seu nome: Rodrigo Monteiro
    Digite sua idade: 44

    CADASTRO
    Nome: Rodrigo Monteiro
    Idade: 44

## 11.5. Evidência prática

O programa foi executado com sucesso no Termux.

Resultados observados:

- O programa solicitou o nome.
- O programa solicitou a idade.
- A idade foi convertida para inteiro utilizando `int()`.
- Os dados foram armazenados nas variáveis correspondentes.
- A função `apresentar_resultado()` recebeu os valores.
- O cadastro foi apresentado corretamente na tela.

Status: EXECUÇÃO CONCLUÍDA COM ÊXITO.

---

# 12. OBSERVAÇÕES TÉCNICAS

## 12.1. Diferença entre criar e chamar uma função

Criar uma função significa definir o que ela fará.

Chamar uma função significa solicitar que ela execute sua tarefa.

## 12.2. Diferença entre parâmetro e argumento

Parâmetro é a variável definida na declaração da função.

Argumento é o valor enviado durante a chamada da função.

Exemplo:

    def apresentar_resultado(nome, idade):
        print(nome, idade)

Nesse exemplo, `nome` e `idade` são parâmetros.

Na chamada:

    apresentar_resultado("Rodrigo", 44)

Os argumentos são `"Rodrigo"` e `44`.

## 12.3. Entendendo o return

O `return` devolve um resultado produzido pela função para quem a chamou.

Exemplo:

    def dobrar_numero(numero):
        return 2 * numero

    resultado = dobrar_numero(10)

    print(resultado)

Resultado:

    20

Nesse exemplo, o valor devolvido por `return` é armazenado na variável `resultado`.

## 12.4. Separação de responsabilidades

Uma função deve executar uma tarefa bem definida.

Isso torna o código:

- Mais organizado.
- Mais fácil de compreender.
- Mais fácil de testar.
- Mais fácil de corrigir.
- Mais fácil de reutilizar.

## 12.5. Aplicação em cibersegurança

A decomposição de problemas é importante na cibersegurança porque permite dividir atividades complexas em etapas menores.

Exemplo: investigação de um incidente de segurança.

- Identificar o incidente.
- Coletar evidências.
- Analisar logs.
- Identificar a origem do problema.
- Avaliar os impactos.
- Conter a ameaça.
- Recuperar os sistemas.
- Elaborar o relatório técnico.

Cada etapa pode ser tratada como uma responsabilidade específica dentro de um processo maior.

---

# 13. ENTREGA DA AULA 10

- [x] Estudo sobre decomposição de problemas.
- [x] Identificação de problemas complexos e problemas menores.
- [x] Estudo sobre modularização.
- [x] Estudo sobre reutilização de código.
- [x] Estudo sobre funções em Python.
- [x] Compreensão de parâmetros e argumentos.
- [x] Compreensão do funcionamento do return.
- [x] Resolução dos exercícios.
- [x] Desenvolvimento do programa de cadastro.
- [x] Execução do arquivo aula10.py.
- [x] Verificação do resultado no Termux.
- [x] Registro das evidências práticas.
- [x] Estudo do vocabulário técnico em inglês.

---

# 14. CONCLUSÃO

A Aula 10 apresentou um conceito fundamental da programação: decompor problemas complexos em partes menores e organizadas.

Aprendemos que as funções permitem separar responsabilidades, reutilizar código e facilitar a manutenção dos programas.

Também aplicamos esses conceitos na criação e execução de um programa de cadastro de usuários utilizando Python no Termux.

A decomposição de problemas é uma habilidade essencial para o desenvolvimento de software e para a construção de ferramentas utilizadas em cibersegurança.

**Status da prática: CONCLUÍDA COM ÊXITO.**
