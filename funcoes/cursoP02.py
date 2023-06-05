#Empacotando valores

def soma (*valores):
    s = 0
    for num in valores:
        s += num
    print (f'A somando os valores {valores} temos: {s}')

soma (8,4,6)
soma (7, 6, 2)