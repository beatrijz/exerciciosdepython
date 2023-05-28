"""Tipos primitivos: int, float, bool, str
int: 7, -4, 0, 9875;
float: 7.0, 4.5, 0.076;
bool: True or False (boleano);
str: 'Olá', '7.5';
"""
"""digite_num = int (input("Digite um número positivo: "));
digite_num2 = int (input("Digite um número positivo: "));
print ('A soma vale', digite_num);
print ("A soma vale {} e {}".format (digite_num, digite_num2));"""

n = input ("Digite algo:");
print ("O tipo primitivo desse valor é: ", type (n));
print("Só tem espaços?", n.isspace());
print ("É um número?", n.isnumeric());
print ("é alfabético", n.isalpha());
print ("é alfanumérico?", n.isalnum());
print ("Está em maiúsculas?", n.isupper());
print ("Está em minúsculas", n.islower());
print ("Está capitalizada", n.istitle());

