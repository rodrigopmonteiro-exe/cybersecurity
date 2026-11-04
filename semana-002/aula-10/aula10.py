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
