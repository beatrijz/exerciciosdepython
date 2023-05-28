"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16"""

num = int (input ("Digite um número: "));
n = str (num);
i = len(n);

if (i == 1):
    print (n [0], "unidade(s)");
if (i == 2):
    print (n [0], "dezena(s)");
    print (n [1], "unidade(s)");
elif i == 3:
    print(n[0], "centena(s)")
    if n[1] == "1":
        print(n[1]+n[2], "unidade(s)")
else:
    print(n[1], "dezena(s)")
    print(n[2], "unidade(s)")
   

