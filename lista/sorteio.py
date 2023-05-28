"""Aluna: Pâmela Beatriz Ferreira de Moura"""
"""1 ADS 2023.1 """
import random

with open('alunos.txt', 'r') as file:
    alunos = [line.strip() for line in file]


random.shuffle(alunos)

equipes = []
for i in range(len(alunos)//5):
    equipe = alunos[i*5:(i+1)*5]
    equipes.append(equipe)

sobras = alunos[len(equipes)*5:]

for i, aluno in enumerate(sobras):
    index = i % len(equipes)
    if len(equipes[index]) < 6:
        equipes[index].append(aluno)


print("Lista de alunos antes da formação das equipes:", alunos)

# Imprimir equipes formadas
print("\nEquipes formadas:")
for i, equipe in enumerate(equipes):
    print(f"Equipe {i+1}: {', '.join(equipe)}")

with open("lista_de_equipes.txt", "w") as file:
    for equipe in equipes:
        file.write(','.join(equipe) + '\n')
