"""23. Faça um programa que leia um numero inteiro positivo “N” e imprima
todos os números naturais de 0 até “N” em ordem crescente."""
numero = int(input("Digite um número inteiro positivo: "));

if numero < 0:
    print("O número digitado não é positivo.");
else:
    for i in range(numero+1):
        print(i);