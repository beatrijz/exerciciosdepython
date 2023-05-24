"Faça um Programa que leia três números e mostre o maior deles."
numeros = []

def verificar (lista):
    
    i = 0
    while i<=2:
        numero = int (input ("Digite um número: "))
        lista.append(numero)
        i += 1


def maior (lista):
    maior = []
    aux = lista [0]
    if (aux > lista [1]):
        maior.append (aux)
    else:
        maior.append (lista[1])
    if (aux > lista [2]):
        maior.append (aux)
    if (lista [2] > lista [1]):
        maior.append (lista [2])
    else:
        maior.append (lista[1])
    if (maior [0] < maior [1]):
        maior [0] = maior [1]
    print ("O maior entre os números digitados é:", maior[0])



verificar (numeros)
maior (numeros)

        
