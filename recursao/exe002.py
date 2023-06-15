def somar(n):
    if n == 0:
        return 0
    else:
        return n + somar(n - 1)

resultado = somar(5)
print(resultado)
