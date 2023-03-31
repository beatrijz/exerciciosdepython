""" Faça um Programa que leia 5 números inteiros, armazene-os em uma lista e imprima
essa lista na tela. """

lista = [];

def lerNum (lista):
    for i in range (5):
        lista.append(input ("Digite um número: "));
        print (lista);
    
lerNum (lista);
