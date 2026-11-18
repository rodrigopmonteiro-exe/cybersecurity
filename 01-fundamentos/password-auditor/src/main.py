import getpass
senha = getpass.getpass("Digite sua senha: ")

while len(senha) == 0:
    senha = getpass.getpass("É obrigatório uma senha! Digite aqui: ")
    
comprimento = len(senha)

cont_maiuscula = 0
cont_minuscula = 0
cont_numero = 0
cont_simbolo = 0

for caractere in senha:
    if caractere.isupper():
        cont_maiuscula += 1
    if caractere.islower():
        cont_minuscula += 1
    if caractere.isdigit():
        cont_numero += 1
    if not caractere.isalnum():
        cont_simbolo += 1

print("========== PASSWORD AUDITOR ==========")
print(f"- Comprimento: {comprimento} caracteres.")
print(f"- Letras maiúsculas: {cont_maiuscula}.")
print(f"- Letras minúsculas: {cont_minuscula}.")
print(f"- Números: {cont_numero}.")
print(f"- Símbolos: {cont_simbolo}.")
print("---------- ANÁLISE ENCERRADA ---------")