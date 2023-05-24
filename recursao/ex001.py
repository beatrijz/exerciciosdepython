"""Defina a função recursiva div que recebe como argumentos dois números naturais m e n e
devolve o resultado da divisão inteira de m por n . Neste exercício não pode recorrer às
operações aritméticas de multiplicação, divisão e resto da divisão inteira."""

def divisao (m, n):
    cont = 0
    if (m > n):
        div = m - n
        cont += 1
    return cont

divisao (10,2)
    
