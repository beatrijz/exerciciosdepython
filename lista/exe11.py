"""11. Faça um programa que receba um número inteiro e verifique se este
número é par ou ímpar, positivo ou negativo. """


numero = int (input ("Digite um número: "));

def verifParouImpar (numero):
    if (numero % 2 == 0):
        print ("O número é par");
    else:
        print ("O número é ímpar");

verifParouImpar(numero);

def positivoNegativo (numero):
    if (numero >= 1):
        print ("e também um número positivo");
    else:
        print ("e também um número negativo");

positivoNegativo(numero);