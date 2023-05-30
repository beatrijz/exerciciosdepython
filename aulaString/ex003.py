"""Faça um programa que solicite uma string ao usuário e
em seguida a imprima em formato de escada."""
nome = input ("Digite o seu nome:")
for i in range (len(nome)):
    print (nome [:i+1])

for j in range (len(nome)):
    print (nome [j:])