lanche = ('Hámburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#tuplas são imutáveis

"""print (lanche[-2])
print (lanche [1:3])
print (lanche [:2])"""
"""for comida in lanche:
    print (f'eu vou comer {comida}')"""
for cont in range (0, len(lanche)):
    print (f'Eu vou comer {lanche[cont]} na posição {cont}')