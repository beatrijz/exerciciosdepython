alunos = []
i = 1
while i <= 5:
    estudante = {}
    estudante['nome'] = input('Digite o nome do estudante: ')
    notas = []
    
    j = 1
    quant_notas = int(input('Quantidade de notas que o respectivo aluno vai ter: '))
    while j <= quant_notas:
        nota = int(input(f'Digite a {j}ª nota: '))
        notas.append(nota)
        j += 1
    
    estudante['notas'] = notas
    alunos.append(estudante)
    i += 1

with open('manipulacaodeArquivos/notas_estudantes.txt', 'w') as file:
    for aluno in alunos:
        file.write(f"Nome: {aluno['nome']}\n")
        file.write(f"Notas: {', '.join(map(str, aluno['notas']))}\n")

print(alunos)