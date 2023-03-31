"""25. Faça um programa que receba dois números. Calcule e mostre: - a soma dos números pares desse intervalo de números, incluindo os
números digitados; - a multiplicação dos números ímpares desse intervalo, incluindo os
digitados"""
num1 = int(input("Digite o primeiro número: "));
num2 = int(input("Digite o segundo número: "));

soma_pares = 0;
mult_impares = 1;

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        soma_pares += i;
    else:
        mult_impares *= i;

print("A soma dos números pares é:", soma_pares);
print("A multiplicação dos números ímpares é:", mult_impares);