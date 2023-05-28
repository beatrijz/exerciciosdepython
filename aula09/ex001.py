"""Escreva um programa que leia um número inteiro e calcule a soma de todos
os divisores desse número, com exceção dele próprio. Ex: a soma dos
divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78"""

numero = int (input("Digite um número: "))
lista = [] 
soma = 0

for divisor in range (1, numero):
    if numero % divisor == 0:
      lista.append(divisor)

string = ' '.join(str(numero) for numero in lista)

for somatorio in lista:
   soma += somatorio

nova_string = string.replace (' ', '+')


print (f'A soma dos divisores do número {numero} é {nova_string} = {soma}')