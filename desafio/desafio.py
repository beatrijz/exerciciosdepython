import datetime
familias = []

def escreva (txt):
    print ('     ' + '-' * len (txt) + '     ')
    print ('    ',txt, '    ')


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
    with open('desafio/dados_familia.txt', 'w') as file:
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



def listagem_de_dados_consolidados():
    with open('desafio/dados_familia.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        cont_fam = 0
        renda_cidade = 0
        individuos = 0
        num_individuos = 0
        cont_renda = 0
        cont_renda_maior = 0

        for i in range(0, len(linhas), 5):
            cpf = linhas[i].split(':')[1].strip()
            cont_fam += 1

            renda = float(linhas[i + 1].split(':')[1].strip())
            renda_cidade += renda
            media_cidade = renda_cidade / cont_fam

            num_individuos = float(linhas[i + 2].split(':')[1].strip())
            individuos += num_individuos
            media_individuos = round(individuos / cont_fam)

            renda_media_fam = float(linhas[i + 3].split(':')[1].strip())
            if renda_media_fam < 1320:
                cont_renda += 1
            elif renda_media_fam > 13200:
                cont_renda_maior += 1

        percentual = round((cont_renda / cont_fam) * 100)

        escreva(f'A média da renda familiar da cidade é: R${media_cidade:.2f}')
        escreva (f'Média de indivíduos por família: {media_individuos}')
        escreva(f'O percentual de famílias que recebem renda familiar média inferior a 1 salário mínimo é: {percentual}%')
        escreva(f'Quantidade de famílias com renda familiar média superior a 10 salários mínimos: {cont_renda_maior}')

ver = 0
def backup_de_dados():
    global ver
    ver += 1
    data_hora_atual = datetime.datetime.now()
    data_formatada = data_hora_atual.strftime("%d/%m/%Y")
    hora_formatada = data_hora_atual.strftime("%H:%M:%S")
    
    with open('desafio/dados_familia.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        dados_fam = []
        for linha in linhas:
            dados_fam.append(linha.strip().split(':'))
    
    with open('desafio/backup.txt', 'w') as arquivo:
            arquivo.write(f"{data_formatada} ")
            arquivo.write(f"{hora_formatada}hs ")
            arquivo.write (f"{len(linhas)} ")
            arquivo.write (f"v{ver}\n")
            for dados in dados_fam:
                dados_formatados = ' = '.join(dados)
                arquivo.write(f"{dados_formatados}\n")

            
def exibir_menu():
    escreva ('MENU')
    escreva ('1 - CADASTRAR FAMÍLIA')
    escreva ('2 - BUSCAR POR CPF')
    escreva ('3 - LISTAGEM DE CPFs CADASTRADOS')
    escreva ('4 - LISTAGEM DOS DADOS DAS FAMÍLIAS')
    escreva ('5 - LISTAGEM DE DADOS CONSOLIDADOS')
    escreva ('6 - BACKUP DE DADOS')
    escreva ('7 - SAIR')


def realizar_escolha(opcao):
    if opcao == 1:
        insercao_familia()
    elif opcao == 2:
        cpf = str(input('Digite o CPF que você deseja buscar: '))
        buscarCPF(cpf)
    elif opcao == 3:
        listagem_de_cpf()
    elif opcao == 4:
        listagem_dos_dados()
    elif opcao == 5:
        listagem_de_dados_consolidados()
    elif opcao == 6:
        backup_de_dados()
    elif opcao == 7:
        print()
    else:
        print("ESCOLHA INVÁLIDA")

i = 0
while True:
    esc = False

    if i == 0:
        exibir_menu()
        opcao = int(input("ESCOLHA A OPÇÃO DESEJADA: "))
        realizar_escolha(opcao)
        if opcao == 7:
            break

    elif opcao != 7:
        acao = str(input('DESEJA REALIZAR OUTRA AÇÃO? (S) OU (N): '))
        if acao == 'S':
            esc = True
            exibir_menu()
            opcao = int(input("ESCOLHA A OPÇÃO DESEJADA: "))
            realizar_escolha(opcao)
            if opcao == 7:
                break
        else:
            break

    i += 1