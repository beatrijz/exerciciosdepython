"""Conta espaços e vogais. Dado uma string com uma frase informada
pelo usuário (incluindo espaços em branco), conte: quantos espaços
em branco existem na frase. quantas vezes aparecem as vogais a, e, i,
o, u. """
string = input ('Digite uma frase: ')
espaco_branco = string.count(' ')
vogais = 'aeiou'
contador_vogais = 0
letra = ""
if letra in string:
     if letra.lower() in vogais:
        contador_vogais += 1

print(f'Espaços em branco: {espaco_branco}')
print(f'Vogais (a, e, i, o, u): {contador_vogais}')