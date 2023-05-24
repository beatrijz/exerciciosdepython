
tupla1 = (1, 3, 5, 2, 3, 5, 1, 1, 3)
tupla2 = ()
for i in tupla1:
    if i not in tupla2:
        tupla2 = (i,) + tupla2
print(tupla2, end='')
