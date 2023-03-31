"""4. Leia uma temperatura em graus Celsius e apresente-a convertida em
graus Fahrenheit. A fórmula de conversão é: F = C*(9.0/5.0)+32.0, sendo
F a temperatura em Fahrenheit e C a temperatura em Celsius. """


temperatura = float (input("Digite a temperatura em graus Celsius: "));
conversao = temperatura * (9.0/5.0)+32.0;
print ("A temperatura em Fahrennheit é {}".format(conversao));