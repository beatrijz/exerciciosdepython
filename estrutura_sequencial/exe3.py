
"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""
sexo = input ("Digite o seu sexo (f/m): ");
altura = float(input ("Digite a sua altura:"));

if (sexo == 'f'):
    formula = (62.1*altura) - 44.7;
    print ("O seu peso ideal é {:.2f} ".format (formula));
else:
     formula = (72.7*altura) - 58
     print ("O seu peso ideal é {:.2f} ".format (formula));

