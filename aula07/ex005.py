"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados
formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. """
n1 = int (input("Digite o valor do primeiro lado: "))
n2 = int (input("Digite o valor do segundo lado: "))
n3 = int (input("Digite o valor do terceiro lado: "))

if (n1 + n2 > n3):
    print ("É um triângulo")
    if (n1 == n2 and n1 == n3 and n2 == n3):
        print("equilátero")
    elif (n1 == n2 or n1 == n2 or n2 == n3):
        print ("isósceles")
    elif (n1 != n2 and n1 != n2 and n2 != n3):
        print ("escaleno")
else:
    print ("Não é um triângulo")
