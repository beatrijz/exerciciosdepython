"""Faça um Programa que peça 2 números inteiros e um número real.
a) o produto do dobro do primeiro com metade do segundo
b) a soma do triplo do primeiro com o terceiro
c) o terceiro elevado ao cubo
"""
n1 = int (input ("Digite o primeiro número:"))
n2 = int (input ("Digite o segundo número:"))
n3 = float (input("Digite o terceiro número:"))

def funcao1 (n1, n2):
    produto = (n1 * 2) * (n2/2)
    return produto

def funcao2 (n1, n3):
    soma = (3*n1) + n3
    return soma
def funcao3 (n3):
    cubo = n3 ** 3
    return cubo
resultado1 = funcao1(n1, n2)
resultado2 = funcao2(n1, n3)
resultado3 = funcao3(n3)

print("Resultado do produto do dobro do primeiro com metade do segundo:", resultado1)
print("Resultado da soma do triplo do primeiro com o terceiro:", resultado2)
print("Resultado do terceiro elevado ao cubo:", resultado3)
