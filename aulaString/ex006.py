""" Faça um programa que leia uma data de nascimento no formato
dd/mm/aaaa e imprima a data com o mês escrito por extenso. Exemplo:
Data = 20/02/1995
Resultado gerado pelo programa:
Você nasceu em 20 de fevereiro de 1995"""
dia = int (input("Digite o dia do nascimento: "))
mes = int (input("Digite o mês: "))
ano = int (input("Digite o ano: "))

def meses (mes):
    if (mes == 1):
        print("janeiro")
    elif (mes == 2):
        print ('fevereiro')
    elif (mes == 3):
        print ('março')
    elif (mes == 4):
        print ('abril')
    elif (mes == 5):
        print ('maio')
    elif (mes == 6):
        print ('junho')
    elif (mes == 7):
        print ('julho')
    elif (mes == 8):
        print ('agosto')
    elif (mes == 9):
        print ('setembro')
    elif (mes == 10):
        print ('outubro')
    elif (mes == 11):
        print ('novembro')
    elif (mes == 12):
        print ('dezembro')
print (f'Você nasceu em {dia} de {mes} de {ano}')
    
