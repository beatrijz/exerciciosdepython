"""20. Faça um programa que leia 10 inteiros e imprima sua media."""

lista = [];
soma = 0

def lerNum (lista):
    for i in range (2):
        lista.append(int(input("Digite um número: ")));
    
lerNum (lista);


for i in lista:
    soma += i;
    media = soma/2;
print("A média dos números digitados é:", media)
