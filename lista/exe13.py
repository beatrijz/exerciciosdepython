""" 13. Faça um programa que receba a altura e o sexo de uma pessoa e calcule
e mostre seu peso ideal, utilizando as seguintes fórmulas (onde h
corresponde à altura): - Homens: (72.7 * h) − 58
- Mulheres: (62, 1 * h) − 44, 7 """
altura = float (input ("Digite a altura: "));
sexo = input ("Indique o sexo com a letra 'F' (Feminino) ou a letra 'M' (Masculino): ");

if (sexo == "F"):
    calculo = (62.1 * altura) - 44.7;
    print ("O peso ideal para o sexo feminino e na seguinte altura, é de:", calculo);
else:
    calculo = (72.7 * altura) - 58;
    print ("O peso ideal para o sexo masculino e na seguinte altura, é de:", calculo);
