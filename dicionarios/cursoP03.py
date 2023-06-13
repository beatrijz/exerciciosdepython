alunos = []

def cadastrarAluno():
    aluno = {}
    aluno ['nome'] = str (input ('Digite o nome do aluno(a): '))
    aluno ['media'] = float (input('Digite a média do aluno(a): '))
    aluno ['situacao'] = ''
    if aluno['media'] >= 7:
        aluno ['situacao'] = 'Aprovado'
    else:
        aluno ['situacao'] = 'Reprovado'
    alunos.append (aluno)

    with open ('dicionarios/alunos.txt', '+a') as arquivo:
        for i in alunos:
            arquivo.write (f'Nome: {i ["nome"]}\n')
            arquivo.write (f'Média: {i["media"]}\n')
            arquivo.write (f'Situação: {i["situacao"]}\n')
            arquivo.write ('\n')


        
def listarAlunos():
    with open ('dicionarios/alunos.txt', 'r') as arquivo:
        linhas = arquivo.readlines ()
        for  i in range (len (linhas)):
            fam = linhas[i].strip().split(':')[0:]
            dados_formatados = ' = '.join(fam)
            escreva (dados_formatados)
"""            nome = alunos[v]['nome']
            media = alunos[v]['media']
            situacao = alunos[v]['situacao']
            print (f'Nome: {nome}')
            print (f'Media: {media}')
            print (f'Situação: {situacao}\n')"""

def escreva (txt):
    print ( '-' * len(txt))
    print (' ', txt, '  ')
    print ('-' * len(txt))


def menu():
    escreva ('Menu')
    escreva ('1 - CADASTRAR ALUNO')
    escreva ('2 - LISTAR OS ALUNOS')
    escreva ('3 - Sair')

def escolher (opca):
    if opca == 1:
        cadastrarAluno()
    elif opca == 2:
        listarAlunos()
    elif opca == 3:
        print ()
    else:
        print ('Opcão inválida')


while True:
    menu ()
    esc = int (input ('Digite a ação que você deseja fazer: '))
    if esc == 3:
        break
    else:
        escolher (esc)


