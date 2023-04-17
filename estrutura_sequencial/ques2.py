"""Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário."""
lado = int (input ("Digite o valor do lado quadrado:"));
area = lado * lado;
dobro = area * 2;
print ("A área do quadrado é: {}".format(area));
print ("O dobro da área do quadrado é: {}".format(dobro));