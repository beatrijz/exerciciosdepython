"""Solicite um número ao usuário. Se for divisível por 3, informe “é divisível por 3”. Se
for divisível por 4, informe “é divisível por 4”. Se for divisível por 3 e 4, informe “É
divisível tanto por 3 quanto por 4”."""
numero = int (input("Digite um número: "))
if numero % 3 == 0:
    print("O número digitado é divisível por 3")
elif numero % 4 == 0:
    print("O número digitado é divisível por 4")
elif numero % 3 == 0 and numero % 4 == 0:
    print("O número digitado é divisível por 3 e por 4")
else:
    print ("O número não é divisível por 3 e nem por 4")