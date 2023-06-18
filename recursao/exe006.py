"""Crie uma função recursiva que imprima o enésimo termo da sequencia de Fibonacci. 
Ex: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584. 2584 é o 18o número da
sequencia. """
def fibonacci (n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 18
resultado = fibonacci(n)
print(f"O {n}º número da sequência de Fibonacci é: {resultado}")