
"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área 
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""
import math
areaPintada = float (input ("Digite quantos metros quadrados a ser pintada: "));

litros = areaPintada/3;
latas = litros/18;
print ("litros {:.2f}". format (litros));
resultado = math.ceil (latas);
print (resultado * 80)

