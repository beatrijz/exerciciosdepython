pessoas = []
dictprin = {}
def escreva (txt):
    print ('  ', '-' * len(txt), '  ')
    print ('  ', txt, '  ')
    print ('  ', '-' * len(txt), '  ')


def cadastroPessoas ():
    pessoa = {}
    pessoa ['nome'] = input ('Digite o nome: ')
    pessoa ['apelido'] = str (input ('Digite o apelido: '))
    if pessoa ['apelido'] == '':
        pessoa ['apelido'] = 'n/a'
    pessoa ['idade'] = int(input('Digite a idade: ')) 
    pessoa ['cpf'] = input('Digite o CPF: ')

    dictprin['pessoas'] = pessoas 
    pessoas.append (pessoa)
    

    with open ('dadospessoas.txt', '+a') as arquivo:
        for pes in pessoas:
            arquivo.write (f"Nome: {pes ['nome']}\n")
            arquivo.write (f"Apelido: {pes ['apelido']}\n")
            arquivo.write (f"Idade: {pes ['idade']}\n")
            arquivo.write (f"CPF: {pes ['cpf']}\n")


def backup():
    with open('dadospessoas.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        dados_fam = []
        for linha in linhas:
            dados_fam.append(linha.strip())

    with open('backup_dadospessoas.txt', 'w') as arquivo_backup:
        for dados in dados_fam:
            arquivo_backup.write(f"{dados}\n")

for i in range(2): 
    cadastroPessoas()
    print (len(dictprin['pessoas']))
    if len(dictprin['pessoas']) == 2:
        backup ()




