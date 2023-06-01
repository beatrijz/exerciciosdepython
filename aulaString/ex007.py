""" Escreva um programa que leia duas strings. Verifique se a segunda
ocorre dentro da primeira e imprima a posição de início.  1a string: AABBEFAATT
 2a string: BE
 Resultado: BE encontrado na posição 3 de AABBEFAATT"""

string1 = input ('Digite a primeira string: ')
string2 = input ('Digite a segunda string: ')


for string2 in string1:
   posicao_inicio = string1.index (string2)
   print (f'1a string: {string1}')
   print (f'2a string {string2}')
   print (f'{string2} encontrado na posição {posicao_inicio} de {string1}', end = "")
else:
    print(f"{string2} não encontrado em {string1}")