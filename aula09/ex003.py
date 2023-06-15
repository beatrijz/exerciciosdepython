"""A série de Fibonacci é formada pela seqüência 1, 1, 2, 3, 5, 8, 13, 21, 34,
55, ... Faça um programa capaz de gerar a série até o nésimo termo."""
numero = int (input("Digite o valor de n: "))
lista = []
def sequencia (n):
    n1 = 1
    n2 = 1
    n3 = n1 + n2
    i = 1        
    print (f'{n1}, {n2}, {n3}, ', end = "")
    while i <= n:
        n1 = n2
        n2 = n3
        n3 = n1 + n2
        lista.append (n3)
        i +=1
    
    string = str (lista).strip('[]')
    print (string)
        

sequencia (numero)