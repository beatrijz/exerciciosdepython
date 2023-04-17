"""Faça um Programa que pergunte quanto você ganha por hora e o número 
de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

horas = float (input("Digite quantas horas foram trabalhadas nesse mês:"));
valor_hora = float (input("Digite o valor que você ganha por hora:"));
total_salario = horas * valor_hora;
print ("O valor do seu sálario nesse mês foi de R${}".format (total_salario));