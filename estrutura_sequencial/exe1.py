"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""

num1 = int (input ("Digite um número inteiro: "));
num2 = float (input("Digite um número real: "));
dobro = (num1 * 2) * (num2/2);
print ("O resultado do dobro é: {:.2f}".format (dobro));
soma = (num1 * 3) + dobro;
print ("O resultado da soma é: {:.2f}".format(soma));
cubo = dobro ** 3;
print ("O terceiro elevado ao cubo: {:.2f}".format(cubo));

