def solicitar_numero ( ):
  return float(input("Digite um número: "))
def dobrar_numero(numero):
  return 2*numero
numero = solicitar_numero( )
resultado = dobrar_numero(numero)
print(f"O dobro de {numero} é {resultado:.1f}.")
