"""Faça um Programa que peça as 4 notas bimestrais e mostre a média."""


notas = []
repetir = "n"


def pegarNotas (notas):
    aux = 0;
    while aux < 4:
        nota = int (input (f"Digite a nota {aux + 1}:"));
        if (nota >= 0 and nota <= 10):
            notas.append (nota)
            aux += 1
        else: 
            print ("Nota inválida, apenas aceitamos valores entre 0 e 10, digite a nota novamente:")
            continue
    

def media (notas):
    soma = 0
    media = 0
    for i in notas:
        soma = soma + i
        media = soma/4
    print (f"A média das notas é: {media}")
    repete()

def repete ():
    repetir = input("Deseja fazer a conta novamente? (s/n) ")
    if repetir == "s":
        notas = [0,0,0,0]
        pegarNotas (notas);
        media (notas)
    else:
        print ("Programa finalizado.")

pegarNotas (notas);
media(notas);



