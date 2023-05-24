lista = []

def pegarNum (numeros):
    aux = 0
    while aux < 4:
        i = int (input (f"Digite o {aux + 1} elemento da lista: "))
        numeros.append (i)
        aux +=1

pegarNum (lista)

def verificacao (numeros):
    auxMaior = []
    auxMenor = []
    num = 0
    num2 = 1
    for i in numeros:
        if (i > num or i > numeros[num2]):
            auxMaior.append(i)
            num = i
        if (i < num or i < numeros [num2]):
            auxMenor.append(i)
    num2 +=1
    if (auxMenor[0]> auxMenor [1]):
        print (f"O segundo número menor é:{auxMenor[0]}")
    else:
        print (f"O segundo número menor é:{auxMenor[1]}")

    if (auxMaior[0] > auxMaior [1]):
        print (f"O segundo maior número é:{auxMaior[0]}")
    else:
        print (f"O segundo maior número é:{auxMaior[1]}")
        

verificacao (lista);



            






