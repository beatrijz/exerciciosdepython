"""Defina a função recursiva div que recebe como argumentos dois números naturais m e n e
devolve o resultado da divisão inteira de m por n . Neste exercício não pode recorrer às
operações aritméticas de multiplicação, divisão e resto da divisão inteira."""

def funrecursiva (m, n, cont = 0):

    if m < n:
        return cont
    else:
        
        return funrecursiva (m - n, n, cont + 1)

resultado = funrecursiva (4,2)
print (resultado)