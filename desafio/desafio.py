familias = []
def insercao_familia ():
    quant_individuos = int (input('Há quantos indivíduos na sua família? '))
    individuos = {}
    salarios = 0
    i = 1
    individuos ['CPF'] = str (input ('Digite o CPF do chefe da família: '))
    while i <= quant_individuos:
        salario = float (input(f'Digite a renda mensal do indivíduo {i} da família: '))
        salarios += salario
        i += 1
    individuos ['Renda total da família'] = salarios
    individuos ['Número de indivíduos'] = quant_individuos
    individuos ['Média da renda familiar'] = salarios / quant_individuos
    familias.append (individuos)
    with open('desafio/dados_familia.txt', '+a') as file:
        for fam in familias:
            file.write(f"CPF: {fam['CPF']}\n")
            file.write(f"Renda total da família: {fam['Renda total da família']}\n")
            file.write(f"Número de indivíduos: {fam['Número de indivíduos']}\n")
            file.write(f"Média da renda familiar: {fam['Média da renda familiar']}\n")
            file.write("\n")

def buscarCPF(cpf):
    with open('desafio/dados_familia.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        encontrado = False
        for i in range(len(linhas)):
            if cpf in linhas[i]:
                escreva(linhas[i])
                escreva(linhas[i+1])
                escreva(linhas[i+2])
                escreva(linhas[i+3])
                encontrado = True
                break
        if not encontrado:
            print('CPF inválido')



def listagem_de_cpf ():
    j = 1
    with open('desafio/dados_familia.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        for i in range (0, len (linhas), 5):
            cpf = linhas[i].split(':')[0]
            num = linhas[i].split(':')[1]
            escreva (f'{j} - {cpf}: {num}')
            j +=1
            

def listagem_dos_dados ():
        with open('desafio/dados_familia.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for i in range (0, len (linhas)):
                fam = linhas[i].strip().split(':')[0:]
                dados_formatados = ' = '.join(fam)
                escreva (dados_formatados)



def listagem_de_dados_consolidados ():
        for fam in familias:
            print (fam)

def escreva (txt):
    print ('     ' + '-' * len (txt) + '     ')
    print ('    ',txt, '    ')


def exibir_menu():
    escreva ('MENU')
    escreva ('1 - CADASTRAR FAMÍLIA')
    escreva ('2 - BUSCAR POR CPF')
    escreva ('3 - LISTAGEM DE CPFs CADASTRADOS')
    escreva ('4 - LISTAGEM DOS DADOS DAS FAMÍLIAS')
    escreva ('5 - LISTAGEM DE DADOS CONSOLIDADOS')
    escreva ('6 - SAIR')

def escolha(escolha):
    if escolha == 1:
        insercao_familia()
    elif escolha == 2:
        cpf = str (input('digite o CPF que voce deseja buscar: '))
        buscarCPF(cpf)
    elif escolha == 3:
        listagem_de_cpf ()
    elif escolha == 4:
        listagem_dos_dados ()
    elif escolha == 5:
        listagem_de_dados_consolidados ()
    else:
        print("Escolha inválida")

while True:
    exibir_menu()
    opcao = int(input("ESCOLHA A OPÇÃO DESEJADA: "))
    escolha(opcao)
    
    if escolha == 5:
        break