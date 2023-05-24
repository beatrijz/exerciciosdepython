"""Crie um programa em Python que que solicite ao usuário e receba o valor
do raio para calcular a área, perímetro e diâmetro de um círculo;"""
raio = int (input ("Digite o raio da círculo: "))
pi = 3.14
def area (raio):
    area = pi * (raio ** 2)
    print (f"A área do círuclo é: {area}") 

def diametro (raio):
    diametro = raio * 2
    print (f"O diâmetro do círculo é: {diametro}")

def perimetro (raio):
    perimetro = 2 * raio * pi
    print (f"O périmetro do círculo é igual a: {perimetro}")

area (raio)
diametro (raio)
perimetro (raio)