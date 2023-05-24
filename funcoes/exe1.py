numeros = []

def recebeNum (lista):
    i = 0
    while i <= 2:
        num = int (input ("Digite um número: "))
        lista.append(num)
        i += 1
recebeNum (numeros)

def soma (lista):
    
    variavel = lista [0] + lista [1] + lista [2]
    print (variavel)
    

soma (numeros)

