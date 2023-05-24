"""Escreva uma função que receba um número de parâmetros indefinido.
Imprima a quantidade de parâmetros recebidos de cada tipo de dado. A função também deve imprimir o maior e o menor valor numérico
recebido. """

def recebe (*numeros):
    print (f"A quantidade total de parâmetros é: {len(numeros)}")
    print (f"O maior número recebido foi: {max(numeros)}")
    print(f"O menor número recebido foi: {min (numeros)}")


recebe (5,4,7,4,2,6,4,5.5, 5.8, 9.8,5,1,10)
