""" Faça um programa que leia três números, verifique (usando if e else) e
mostre o maior e o menor deles;
"""

lista1 = [];
num = [0,0,0];
def lerNumeros(lista):
    i = 0;
    while (i < 3):
        aux = int (input('Digite o número: '));
        lista.append(aux);
        i = i + 1;
    print(lista)

def verificarMaior (lista, num):
   
   for i in range(3):
        if (lista [i] > num [i]): 
            num[i].append(lista[i]);
        print (num)
   
        
          

lerNumeros(lista1);
verificarMaior (lista1, num);
