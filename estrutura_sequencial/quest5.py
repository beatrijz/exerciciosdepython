"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, 
isto é, considere latas cheias."""
import math
area_pintada = float (input ("Digite o tamanho da área a ser pintada: "));

def calculo_lata18 (area):
    litros = area/6;
    calculo = litros/18;
    resultado = math.ceil (calculo)
    valor = resultado * 80;
    print ("-Será necessário comprar apenas {} latas de 18 litros.\n Dando o valor de R$ {:.2f} reais.".format (resultado, valor));

calculo_lata18 (area_pintada)

def calculo_lata2 (area):
    litros = area/6;
    calculo = litros/3.6;
    resultado = math.ceil (calculo)
    valor = resultado * 25;
    print ("-Ou comprar {} latas de 3.6 litros.\n Dando o valor de R$ {:.2f} reais.".format (resultado, valor));

calculo_lata2 (area_pintada)

def misto_lata (area):
    litros = area/6;
    calculo1 = litros/18;
    calculo2 = calculo1 * 1.1
    resultado = math.ceil (calculo2)
    resto = resultado - calculo2 
    resto2 = math.ceil (resto);
    valor = (resultado * 80) + (resto2 * 25)
   
    print ("-Ou comprar {} latas de 18 listros e {} lata (s) de 3.6 litros. \n Dando o valor de R${:.2f}reais.".format (resultado, resto2, valor));

misto_lata (area_pintada)