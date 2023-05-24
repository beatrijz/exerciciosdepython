
def pegarN():
    num = []
    aux = 0
    while aux < 3:
        numeros = int(input("Digite um número:"))
        num.append(numeros)
        aux += 1
    return num

lista = pegarN()
tupla = tuple(lista)

def tuplaF(tupla1):
    for i in range(len(tupla1)):
       tupla = (tupla1 [i], tupla1[i]**3)
       print (tupla)

tuplaF(tupla)






