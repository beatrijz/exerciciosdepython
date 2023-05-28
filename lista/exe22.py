"""22. Faça um programa que leia um numero inteiro “N” e depois imprima os N
primeiros números naturais ímpares. """

numero = int(input("Digite um número inteiro: "));
i = 1;
aux = 0;

while aux < numero:
    if i % 2 != 0:
        print(i);
    aux += 1;
    i += 1;