"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""
num1 = int (input ("Digite o primeiro número:"));
num2 = int (input ("Digite o segundo número:"));
num3 = int (input ("Digite o terceiro número:"));
maior = num1;
menor = num3;

if (num1 > num2 and num1 > num3):
    num1 = maior;
if (num1 < num2 and num1 < num3):
    num1 = menor;


if (num2 > num1 and num2 > num3):
    num2 = maior;
if (num2 < num1 and num2 < num3):
    num2 = menor;


if (num3 > num2 and num3 > num1):
    num3 = maior;
if (num3 < num2 and num3 < num1):
    num3 = menor;


meio = num1 + num2 + num3 - maior - menor
print (menor, meio, maior)
    

