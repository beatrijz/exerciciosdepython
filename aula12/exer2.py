""" 2. Faça um programa que leia 10 números inteiros. Cada numero par deve ser
armazenado em uma lista de pares e cada impar tem que ser armazenado em uma
lista de impares. """

lista = [];
par = [];
impar = [];

def lerNum (lista):
    i = 0;
    while( i <= 9):
        lista.append(int (input ("Digite um número: ")));
        i= i+1;
    print ('O total da lista é: {}'.format(lista));
    
def verificar (numero, par, impar):
    i = 0;
    for i in range (len(numero)):
        if(numero [i]%2 == 0):
            par.append(numero[i]);
            i += 1;
        else:
            impar.append(numero[i]);
                
    print ('O total da lista dos números pares é: {}'.format(par));
    print ('O total da lista dos números Impares é: {}'.format(impar));

lerNum (lista);
verificar (lista, par, impar);




