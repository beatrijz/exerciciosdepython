alunos = []
i = 1
while i <= 5:
    estudante = {}
    quant_notas = int (input ('Quantidade de notas que o respectivo aluno vai ter: '))
    estudante ['nome'] = input ('Digite o nome do estudante: ')
    j = 1
    while j <= quant_notas:
        estudante ['nota'] = int(input(f'Digite a {j} nota: '))
        j += 1
    i += 1
    alunos.append (estudante)
    
    with open('manipulacaodeArquivos/notas_estudantes.txt', 'a') as file:
        for i in alunos:
            file.write(f"Nome: {i['nome']}\n")
            file.write (f"Notas': {i['nota']}\n")

print (alunos)
    