ferramentas =["Termux", "Python", "Git"]
print("Inventário do laboratório de Cibersegurança")
print("===========================================")
for ferramenta in ferramentas:
    print("-", ferramenta)
if ferramentas:
   print("O inventário contém ferramentas.")
else:
   print("O inventário está vazio.")
print("Total de ferramentas:", len(ferramentas))
