listapessoas = []

def cadastrar_pessoas ():
    pessoas = {}
    pessoas ['nome'] = str (input('Digite o nome da pessoa: '))
    pessoas ['sexo'] = str (input ('Digite o sexo da pessoa [F/M]: '))
    pessoas ['idade'] = int (input ('Digite a idade da pessoa: '))

    listapessoas.append (pessoas)
    with open('dicionarios/pessoas.txt', '+a') as arquivo:
        for i in listapessoas:
            arquivo.write (f'Nome: {i["nome"]}\n')
            arquivo.write (f'Sexo: {i["sexo"]}\n')
            arquivo.write (f'Idade: {i["idade"]}\n')
            arquivo.write ("\n")  

def media_idade ():
    soma = 0
    media = 0
    cont = 0
    with open ('dicionarios/pessoas.txt', 'r') as arquivo:
        linhas = arquivo.readlines ()
        for i in range (2, len (linhas), 4):
            idades = int(linhas[i].split(':')[1].strip())
            soma += i
            cont += 1
        media = soma / cont 
        escreva (f'A média de idade do grupo é: {media}')
        
def lista ():
    with open ('dicionarios/pessoas.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        for i in range (0, len(linhas), 4):
            nome = linhas[i].split(':')[1].strip()
        for j in range (1, len (linhas), 4):
            sexo = linhas [j].split (':')[1].strip()
            if sexo == 'F':
                nomes = linhas[j - 1].split(':')[1].strip()
                print (nomes)

def escreva (txt):
    print ('     ' + '-' * len (txt) + '     ')
    print ('    ',txt, '    ')



def exibir_menu():
    escreva ('MENU')
    escreva ('1 - CADASTRAR PESSOAS' )
    escreva ('2 - DELETAR PESSOAS')
    escreva ('3 - CALCULAR A MÉDIA DAS IDADES')
    escreva ('4 - LISTA COM TODAS AS MULHERES')
    escreva ('3 - SAIR')

def escolha (opcao):
    if opcao == 1:
        cadastrar_pessoas ()
    if opcao == 3:
        media_idade()
    if opcao == 4:
        lista ()


while True:
    exibir_menu()
    esc = int (input('Escolha uma opção: '))
    escolha (esc)
    
    

    if esc == 7:
        break


