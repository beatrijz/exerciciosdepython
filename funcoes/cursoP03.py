def area (largura, comprimento):
    area = largura * comprimento
    return area

print ('CONTROLE DE TERRENOS')
print ('-' * 30)
largura = float (input ('LARGURA (m):'))
comprimento = float (input ('COMPRIMENTO (m):'))
print (f'A área do terreno retângular {largura} X {comprimento} é: {area (largura, comprimento)} m')