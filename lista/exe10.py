"""10. Faça um programa que leia um número e, caso ele seja positivo, calcule e
mostre: - O número digitado ao quadrado
- A raiz quadrada do número digitado"""

import math
numero = int (input("Digite um número: "));
if (numero > 0):
    quadrado = numero ** 2;
    print ("O", numero, "elevado ao quadrado é igual a:", quadrado);
    raiz = math.sqrt(numero);
    print ("E a raiz do", numero, "é igual a: ", raiz);