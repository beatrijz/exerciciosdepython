lista = [9, 5, 6]

def cubo(lista):
    listas = []
    for elemento in lista:
        cubo = elemento ** 3
        tupla = (elemento, cubo)
        listas.append(tupla)
    print(listas)

cubo(lista)