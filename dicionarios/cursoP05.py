pessoa = {}
def verifica_dados (dados):
    dados ['nome'] = str (input ('Digite o seu nome: '))
    dados ['sexo'] = str (input ('Digite o seu sexo feminino (f) ou masculino (m): '))
    dados ['ano_nascimento'] = int (input('Digite o ano de nascimento: '))
    dados ['ctps'] = int (input('Digite o número da carteira de trabalho: '))
    if dados ['ctps'] > 0:
        dados ['ano_contratacao'] = int (input('Digite o ano de contratação: ')) 
        dados ['salario'] = float (input('Digite o valor do seu salário: '))
        dados ['idade'] = 2023 - dados['ano_nascimento']
    for k, v in dados.items ():
        print (f'{k} = {v}')

def anos_aposentadoria (dados):
    verifica_dados (pessoa)
    ano = 2023
    aposentadoria = dados['ano_contratacao'] + 35;
    if dados ['sexo'] == 'f':
        if aposentadoria >= ano and dados ['idade'] >= 62:
            print ('Esse ano você se aposenta!')
        if aposentadoria <= ano and dados ['idade'] >= 62:
            diferenca = ano - aposentadoria
            if diferenca == 1:
                print (f'Falta {diferenca} ano para você já pode se aposentar ')
            else:
                print (f'Falta {diferenca} anos para você se aposentar ')
    else:
        if aposentadoria >= dados['ano_contratacao'] and dados ['idade'] >= 65:
            print ('Esse ano você se aposenta!')
        if aposentadoria <= dados ['ano_contratacao'] and dados ['idade'] >= 65:
            diferenca = aposentadoria - dados ['ano_contratacao']
            print (f'Falta {diferenca} anos para você se aposentar ')
anos_aposentadoria (pessoa)

    
