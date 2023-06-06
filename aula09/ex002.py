"""Em Matemática, o número harmônico designado por define-se como
sendo a soma da série harmónica"""

n = int (input ("Digite um número inteiro: "))
soma = 0.0
for numero in range (1, n):
    print ("1/", numero, end = "+")
    soma += 1 / numero

print("A soma da série harmônica até", n, "é:", soma)

