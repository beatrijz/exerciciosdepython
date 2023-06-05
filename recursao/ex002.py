"""2. Implemente uma função recursiva que, dados dois números inteiros x e n, calcula o valor de
xn."""

def exponencial(x, n):
    if n < 0:
        return 1 / exponencial(x, -n)
    elif n == 0:
        return 1
    else:
        return x * exponencial(x, n - 1)
    
expoente = exponencial (5,2)
print (expoente)
