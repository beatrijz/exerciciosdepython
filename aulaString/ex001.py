"""Faça um programa que leia 2 strings e informe o conteúdo delas
seguido do seu comprimento. Informe também se as duas strings
possuem o mesmo comprimento e são iguais ou diferentes no
conteúdo."""
string1 = input ("Digite o valor da primeira String: ")
string2 = input ("Digite o valor da segunda String: ")


if len(string1) == len (string2):
    print (f'A primeira String {string1} tem o o seu comprimento igual da segunda String {string2}, de {len(string1)}')
if len(string1) != len(string2):
    print ('São diferentes no comprimento')
if string1 == string2:
    print("São iguais no conteúdo também")
if string1 != string2:
    print ("e também no conteúdo")


