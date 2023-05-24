"""2. Dados três valores distintos, fazer um programa que, após a leitura destes
dados, coloque-os em ordem crescente."""
numeros = []

def pegarnum (num):
    for i in range(3):
        aux = int (input ("Digite um número:"))
        num.append (aux)

def ordemCrescente (num):
    numero_maior = num [0]
    numero_menor = num [0]
    meio = 0
    ordem = []
    for i in num:
        if (i > numero_maior):
            numero_maior = i
        if (i < numero_menor):
            numero_menor = i
        if (numero_maior > i and i > numero_menor ):
            meio = i

    ordem = [numero_maior,meio, numero_menor]
    print (ordem)

pegarnum(numeros)
ordemCrescente(numeros)
    
    
    

