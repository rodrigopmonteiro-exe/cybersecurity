print("SISTEMA DE DESEMPENHO ACADEMICO")
nome = input("Nome do aluno: ")
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
media = (nota1 + nota2 + nota3)/3
print("===============================")
print("     RESULTADO ACADEMICO       ")
print("===============================")
print("Estudante:", nome)
print("Media:", round(media, 2))
if media >= 7.0:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")


# Etapa              Instrução executada                 nome               nota1               nota2               nota3
#  1     print("SISTEMA DE DESEMPENHO ACADEMICO")         -                  -                    -                   -
#  2     nome = input("Nome do aluno: ")             Rodrigo Monteiro        -                    -                   -
#  3     nota2 = float(input("Segunda nota: "))      Rodrigo Monteiro        8.0                  -                   -
#  4     nota3 = float(input("Terceira nota: "))     Rodrigo Monteiro        8.0                  9.0                 -
#  5     media = (/nota1 + nota2 + nota3)/3          Rodrigo Monteiro        8.0                  9.0                 10.0
#  6     print("===============================")    Rodrigo Monteiro        8.0                  9.0                 10.0
#  7     print("     RESULTADO ACADEMICO       ")    Rodrigo Monteiro        8.0                  9.0                 10.0
#  8     print("===============================")    Rodrigo Monteiro        8.0                  9.0                 10.0
#  9     print("Estudante:", nome)                   Rodrigo Monteiro        8.0                  9.0                 10.0
#  10    print("Media:", round(media, 2))            Rodrigo Monteiro        8.0                  9.0                 10.0
#  11    if media >= 7.0:                            Rodrigo Monteiro        8.0                  9.0                 10.0
#  12        print("Situação: Aprovado")             Rodrigo Monteiro        8.0                  9.0                 10.0
#  13    else:                                       Rodrigo Monteiro        8.0                  9.0                 10.0
#  14        print("Situação: Reprovado")            Rodrigo Monteiro        8.0                  9.0                 10.0
