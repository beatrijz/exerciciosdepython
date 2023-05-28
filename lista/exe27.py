"""27. Escreva um programa que leia um numero inteiro positivo “N” e em
seguida imprima “N” linhas do chamado Triângulo de Floyd. Para n = 6,
temos:"""

numero = int(input("Digite um número inteiro positivo: "));

aux = 1;

for i in range(1, numero + 1):
    for x in range(1, i+1):
        print(aux, end=" ");
        aux += 1;
    print();