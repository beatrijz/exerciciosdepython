"""Escreva um programa para contar a quantidade de números pares
entre dois números quaisquer fornecidos pelo usuário?"""
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
cont = 0

for i in range(n1, n2 + 1):
    if i % 2 == 0:
        cont += 1

print(f"A quantidade de números pares entre {n1} e {n2} é: {cont}")
