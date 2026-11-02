# Aula 6 — Laboratório integrado

**Data:** 31/10/2026
**Duração:** 2 horas e 30 minutos  
**Módulo:** Semana 01 — Fundamentos e preparação do ambiente

## Objetivo

Combinar terminal, Python, organização de arquivos e documentação em um único projeto pequeno.

---

## Parte A — Preparar o laboratório (20 min)

Crie a pasta da aula:

```bash
mkdir -p ~/cybersecurity/semana-01/aula-06
cd ~/cybersecurity/semana-01/aula-06
```

### Registre o ambiente

Execute:

```bash
{
    echo "Data: 28/10/2026"
    echo "Python:"
    python --version
    echo "Git:"
    git --version
    echo "Diretório:"
    pwd
} > ambiente.txt
```

### Confira

```bash
cat ambiente.txt
```

---

## Parte B — Construir o programa (40 min)

Crie `inventario.py`:

```python
ferramentas = ["Termux", "Python", "Git"]

print("Inventário do laboratório")
print("=========================")

for ferramenta in ferramentas:
    print("-", ferramenta)

print("Total de ferramentas:", len(ferramentas))
```

### Execute

```bash
python inventario.py
```

Observe como a lista, o laço `for` e a função `len()` funcionam.

Se algum conceito for novo, registre a dúvida em vez de tentar memorizar sem compreender.

---

## Parte C — Modificar e testar (35 min)

Faça três modificações:

1. Adicione uma quarta ferramenta à lista, mas somente se ela estiver realmente disponível no seu ambiente.
2. Altere o título exibido.
3. Modifique o programa para mostrar uma mensagem diferente quando a lista estiver vazia.

### Exemplo para a terceira tarefa

```python
if ferramentas:
    print("O inventário contém ferramentas.")
else:
    print("O inventário está vazio.")
```

Teste as duas condições, removendo temporariamente os itens da lista e depois restaurando-os.

---

## Parte D — Documentação e integridade (30 min)

Crie `README.md` com:

- Objetivo do laboratório.
- Requisitos.
- Como executar o programa.
- Saída esperada.
- Testes realizados.
- Limitações conhecidas.

### Calcule um resumo criptográfico do código

```bash
sha256sum inventario.py
```

O SHA-256 gera um hash que pode ajudar a verificar se o conteúdo mudou.

**Atenção:** o hash não prova, sozinho, que o código é seguro ou confiável.

---

## Parte E — Technical English (25 min)

Escreva cinco frases em inglês sobre o laboratório, utilizando:

- `tool` — ferramenta.
- `script` — script.
- `execute` — executar.
- `output` — saída.
- `verify` — verificar.

### Exemplo

*I execute the Python script and verify its output.*

### Evidências

Registre e preserve:

- [ ] Arquivo `inventario.py`.
- [ ] Arquivo `ambiente.txt`.
- [ ] Arquivo `README.md`.
- [ ] Saída do programa.
- [ ] Hash SHA-256 registrado nas notas.

---

## Critérios de conclusão

- [ ] Ambiente registrado corretamente.
- [ ] Programa Python criado e executado.
- [ ] Lista e laço `for` compreendidos.
- [ ] Função `len()` compreendida.
- [ ] Três modificações realizadas e testadas.
- [ ] Documentação criada.
- [ ] Hash SHA-256 calculado.
- [ ] Cinco frases em inglês produzidas.
- [ ] Evidências preservadas.
