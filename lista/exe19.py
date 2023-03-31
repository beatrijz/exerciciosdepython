"""19. Faça um programa que peça ao usuário para digitar 10 valores e some-os
e imprima o resultado."""

lista = [];
soma = 0

def lerNum (lista):
    for i in range (10):
        lista.append(float(input("Digite um número: ")));
    
lerNum (lista);


for i in lista:
    soma += i;
print("O resultado da soma é:", soma)



