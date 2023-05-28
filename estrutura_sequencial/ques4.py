"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)."""

temperatura = float (input ("Digite a temperatudo em Fahrenheit:"));
formula = 5 * ((temperatura-32) / 9);
print ("O valor da temperatura em graus Celsius é {:.2f}".format(formula))