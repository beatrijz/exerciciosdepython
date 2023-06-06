alunos = {}
quant_alunos = int (input ('Digite a quantidade de alunos: '))
i = 1
while i <= quant_alunos:
    aluno = dict ()
    aluno ['nome'] = str (input ('Digite o nome do aluno(a): '))
    aluno ['media'] = float (input('Digite a média do aluno(a): '))
    aluno ['situacão'] = str (input('Qual a situação do aluno? '))
    i += 1
    alunos [i] = aluno

for k, v in alunos.items ():
    print (f'{k} = {v}')