"""2. Implemente uma função recursiva que, dados dois números inteiros x e n, calcula o valor de xn. """
def expoente (x, n):
    if n == 0:
        return 1
    else:
       return (x * expoente (x, n-1))
    
ex =expoente (3, 4)
print (ex)