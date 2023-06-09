familias = dict ()


def insercao_familia ():
    quant_individuos = int (input('Há quantas indivíduos na sua família? '))
    individuo = {}
    salarios = 0
    i = 1
    individuo ['CPF'] = str (input ('Digite o CPF do chefe da família: '))
    while i <= quant_individuos:
        salario = float (input(f'Digite a renda mensal do indivíduo {i} da família: '))
        salarios += salario
        i += 1
    individuo ['salarios'] = salarios
    print (individuo)
    familias [i] = individuo
        
insercao_familia ()