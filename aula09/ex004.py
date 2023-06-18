"""A série de Fibonacci é formada pela seqüência 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
55,... Faça um programa que gere a série até que o valor seja maior que 500."""
i = 1
lista = []
n1 = 0
n2 = 1
n3 = n1 + n2
print (f'{n1}, {n2}, {n3}, ', end= "")
while n3 <= 500:
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    lista.append (n3)
    i += 1
print (str (lista).strip ('[]'))

