"""1. Ler três números inteiros e mostrar o maior e o menor deles."""
numeros = []

def pegarnum (num):
    for i in range(3):
        aux = int (input ("Digite um número:"))
        num.append (aux)

def maior (num): 
    num_maior = num [0]
    for numero in num:
        if (numero > num_maior):
            num_maior = numero
    return num_maior

def menor (num):
    num_menor = num [0]
    for numeros in num:
        if (numeros < num_menor):
            num_menor = numeros
    return num_menor

pegarnum (numeros)
numMaior = maior(numeros)
numMenor = menor (numeros)
print (f"O maior número digitado foi o: {numMaior}")
print (f"O menor número digitado foi o: {numMenor}")