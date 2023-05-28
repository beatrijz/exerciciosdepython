"""4. Ler um número inteiro e mostrar uma mensagem indicando se este número é
par ou ímpar, e se é positivo ou negativo.
"""
numero = int (input ("Digite um número: "))

def verificarImparePar (num):
    if (num % 2 == 0):
        return "par"
    else:
        return "ímpar"
    
def verificarPositivoNegativo (num):
    if (num > 0):
        return "positivo"
    else:
        return "negativo"
    
par_impar = verificarImparePar(numero)
neg_pos = verificarPositivoNegativo(numero)
print (f'O número é {par_impar} e é {neg_pos}.')
