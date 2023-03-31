"""8. Leia o valor do raio de um círculo e calcule e imprima a área do círculo
correspondente. A área do círculo é π*r2 , considere π = 3.141592."""


raio = float (input ("Digite o valor do raio do circulo: "));
pi = 3.141592;
area = pi * (raio ** 2);
print ("O valor da área do circulo é de: {}".format (area));