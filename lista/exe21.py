"""21. Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima a sua média"""
lista = [];
soma = 0;

i = 1;
while i < 10:
    aux = int(input("Digite um número inteiro positivo: "));
    if aux > 0:
        lista.append(aux);
        soma += aux;
        i += 1;

media = soma / len(lista);
print("A média dos números positivos digitados é:", media);