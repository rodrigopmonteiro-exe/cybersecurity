import getpass
senha = getpass.getpass("Digite sua senha: ")

while len(senha) == 0 or senha.isspace( ):
    senha = getpass.getpass("É obrigatório uma senha válida! Digite aqui: ")
    
comprimento = len(senha)

cont_maiuscula = 0
cont_minuscula = 0
cont_numero = 0
cont_simbolo = 0
cont_espaco = 0

for caractere in senha:
    if caractere.isupper():
        cont_maiuscula += 1
    elif caractere.islower():
        cont_minuscula += 1
    elif caractere.isdigit():
        cont_numero += 1
    elif caractere.isspace ():
        cont_espaco += 1
    else:
        cont_simbolo += 1

print("========== PASSWORD AUDITOR ==========")
print(f"- Comprimento: {comprimento} caracteres.")
print(f"- Letras maiúsculas: {cont_maiuscula}.")
print(f"- Letras minúsculas: {cont_minuscula}.")
print(f"- Números: {cont_numero}.")
print(f"- Símbolos: {cont_simbolo}.")
print(f"- Espaços vazios: {cont_espaco}.")
print("---------- ANÁLISE ENCERRADA ---------")
