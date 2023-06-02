"""Defina a função recursiva div que recebe como argumentos dois números naturais m e n e
devolve o resultado da divisão inteira de m por n . Neste exercício não pode recorrer às
operações aritméticas de multiplicação, divisão e resto da divisão inteira."""
def divisao(m, n):
    cont = 0
    while m >= n:
        m -= n
        cont += 1
    return cont

dividindo = divisao (10, 2)
print (dividindo)
