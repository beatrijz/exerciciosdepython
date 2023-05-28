"""Escreva um programa para calcular o fatorial de um número fornecido
pelo usuário."""
numero = int(input("Digite um número: "))
lista = []
j = 0
fatorial = 1
cont = numero

if numero == 0:
    print(f"O fatorial de {numero}! = 1")

while cont > 0 and j < 10:
    lista.append(cont)
    cont -= 1
    j += 1

string = ' '.join(str(numero) for numero in lista)

for i in range(1, numero + 1):
    fatorial *= i

nova_string = string.replace (' ', 'x')

print(f"O fatorial de {numero}! = {nova_string} = {fatorial}")