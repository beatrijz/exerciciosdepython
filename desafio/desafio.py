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

insercao_familia ()


cpf = str (input('digite o CPF que voce deseja buscar: '))

def busca_dados (cpf):
    with open('desafio/dados_familia.txt', 'r') as arquivo:
        arquivos = arquivo.readlines()
        encontrado = False
        for i in range (0, len (arquivos), 3):
            if arquivos[i].strip() == f"CPF: {cpf}":
                print(arquivos[i].strip())
                print(arquivos[i+1].strip())
                print(arquivos[i+2].strip())
                print(arquivos[i+3].strip())
                print()
                encontrado = True
                break
        if not encontrado:
            print('CPF não encontrado')
busca_dados(cpf)


def listagem_de_cpf ():
    lista_cpf = []
    for fam in familias:
        lista_cpf.append(fam ['CPF'])

    print (lista_cpf)
           
#listagem_de_cpf ()

def listagem_dos_dados ():
    for fam in familias:
        print (fam)

#listagem_dos_dados ()

#def listagem_de_dados_consolidados ()