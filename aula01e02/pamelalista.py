"""1. Faça um programa que leia um número inteiro e o imprima."""

numero = int(input ("Digite um número: "));
print ("O número digitado foi: {}".format(numero));

"""2. Peça ao usuário para digitar três valores inteiros e imprima a soma deles."""

numero = int(input ("Digite o primeiro número: "));
numero2 = int(input ("Digite o segundo número: "));
numero3 = int(input ("Digite o terceiro número: "));
soma = numero + numero2 + numero3;
print ("A soma dos números é: {}".format(soma));


"""3. Desenvolva um algoritmo em python que leia um número inteiro e imprima
o seu antecessor e seu sucessor."""

numero = int(input ("Digite um número: "));
print ("O seu antecessor é: {}".format(numero - 1));
print ("O seu sucessor é: {}".format(numero + 1));


"""4. Leia uma temperatura em graus Celsius e apresente-a convertida em
graus Fahrenheit. A fórmula de conversão é: F = C*(9.0/5.0)+32.0, sendo
F a temperatura em Fahrenheit e C a temperatura em Celsius. """


temperatura = float (input("Digite a temperatura em graus Celsius: "));
conversao = temperatura * (9.0/5.0)+32.0;
print ("A temperatura em Fahrennheit é {}".format(conversao));


"""5. Leia uma velocidade em km/h (quilômetros por hora) e apresente-a
convertida em m/s (metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em km/h e M em m/s. """

velocidade = int (input("Digite a velocidade em quilômetros por hora: "));
conversao = velocidade/3.6;
print ("A velocidade em m/s é {}".format (conversao));


"""6. Leia quatro notas, calcule a média aritmética e imprima o resultado."""


notas = [];

def lerNotas (notas):
    i = 0;
    while (i < 4):
        aux = int (input('Digite a nota: '));
        notas.append(aux);
        i = i + 1;

lerNotas (notas);

def mediaNotas (notas):
 soma = sum(notas);
 divisao = soma/4;
 print ("A média das notas é: ", divisao);

mediaNotas (notas);


""" 7. Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor
correspondente em dólares. """


valor = float (input ("Digite o valor em real: "));
cotacao = valor * 5.14;
print ("O valor conertido em dólar é de: ", cotacao);



"""8. Leia o valor do raio de um círculo e calcule e imprima a área do círculo
correspondente. A área do círculo é π*r2 , considere π = 3.141592."""


raio = float (input ("Digite o valor do raio do circulo: "));
pi = 3.141592;
area = pi * (raio ** 2);
print ("O valor da área do circulo é de: {}".format (area));



"""9. A importância de R$ 780.000,00 será dividida entre três ganhadores de
um concurso. Sendo que da quantia total: - O primeiro ganhador receberá 46%; - O segundo receberá 32%; - O terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores."""



valor = 780.000;
ganhador1 = (valor * 46) / 100;
print ("O primeiro ganhador ficará com: ", ganhador1);
valor = valor - ganhador1;
ganhador2 = (valor * 32) / 100;
print ("O segundo ganhador ficará com: ", ganhador2);
valor = valor - ganhador2;
print ("O terceiro ganhador ficará com: ", valor);


"""10. Faça um programa que leia um número e, caso ele seja positivo, calcule e
mostre: - O número digitado ao quadrado
- A raiz quadrada do número digitado"""

import math
numero = int (input("Digite um número: "));
if (numero > 0):
    quadrado = numero ** 2;
    print ("O", numero, "elevado ao quadrado é igual a:", quadrado);
    raiz = math.sqrt(numero);
    print ("E a raiz do", numero, "é igual a: ", raiz);


"""11. Faça um programa que receba um número inteiro e verifique se este
número é par ou ímpar, positivo ou negativo. """


numero = int (input ("Digite um número: "));

def verifParouImpar (numero):
    if (numero % 2 == 0):
        print ("O número é par");
    else:
        print ("O número é ímpar");

verifParouImpar(numero);

def positivoNegativo (numero):
    if (numero >= 1):
        print ("e também um número positivo");
    else:
        print ("e também um número negativo");

positivoNegativo(numero);


"""12. Faça um programa que leia 2 notas de um aluno, verifique se as notas são
válidas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua
um valor válido, este fato deve ser informado ao usuário e o programa
termina. """


nota1 = float (input ("Digite a primeira nota do aluno: "));
nota2 = float (input ("Digite a segunda nota do aluno: "));

def notaValida (nota1, nota2):
    if (nota1 >= 0.0 and nota1 <= 10.0 and nota2 >= 0.0 and nota2 <= 10.0):
        print ("As notas são válidas");
    else:
        print ("As notas não são válidas");
        

notaValida (nota1, nota2);


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


""" 14. A nota final de um estudante é calculada a partir de três notas atribuídas
entre o intervalo de 0 até 10, respectivamente, a um trabalho de
laboratório, a uma avaliação semestral e a um exame final. A média das
três notas mencionadas anteriormente obedece aos pesos: Trabalho de
Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o
resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as
verificações necessárias. """

nota1 = float (input("Digite a nota do trabalho de laboratório: "));
nota2 = float (input("Digite a nota da avaliação semestral: "));
nota3 = float (input("Digite a nota do exame final: "));

def notaValida (nota1, nota2, nota3):
    if (nota1 >= 0.0 and nota1 <= 10.0 and nota2 >= 0.0 and nota2 <= 10.0 and nota3 >= 0.0 and nota3 <= 10.0):
        print ("As notas são válidas");
    else:
        print ("As notas não são válidas");
        

notaValida (nota1, nota2, nota3);

def media (nota1, nota2, nota3):
 media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10;
 if (media >= 0 and media <= 2.9):
    print ("O aluno está reprovado, pois a média foi de:", media);
 elif (media >= 3 and media <= 4.9):
    print ("O aluno ficou em recuperação, pois a média foi de:", media);
 else:
    print ("O aluno foi aprovado, pois a média foi de:", media);

media (nota1, nota2, nota3);



""" 15. Faça um programa que faça 5 perguntas para uma pessoa sobre um
crime."""

perg1 = input ("Telefonou para a vítima? Responda com 'S' (Sim) ou 'N' (Não): ");
perg2 = input ("Esteve no local do crime? Responda com 'S' (Sim) ou 'N' (Não): ");
perg3 = input ("Mora perto da vítima? Responda com 'S' (Sim) ou 'N' (Não): ");
perg4 = input ("Devia para vítima? Responda com 'S' (Sim) ou 'N' (Não): ");
perg5 = input ("Já trabalhou com a vítima? Responda com 'S' (Sim) ou 'N' (Não): ");
aux = 0
if (perg1 == "S"):
    aux = aux + 1;
if (perg2 == "S"):
    aux = aux + 1;
if (perg3 == "S"):
    aux = aux + 1;
if (perg4 == "S"):
    aux = aux + 1;
if (perg5 == "S"):
    aux = aux + 1;

if(aux == 2):
    print ("Suspeito!");
if(aux == 3 or aux == 4):
    print ("Cúmplice!");
if (aux == 5):
    print("Assassino!");



""" 16. Leia a idade e o tempo de serviço de um trabalhador e escreva se ele
pode ou não se aposentar. As condições para aposentadoria são: - Ter pelo menos 65 anos,
 - Ou ter trabalhado pelo menos 30 anos, - Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos. """

idade = int (input("Digite a sua idade: "));
tempoServico = int (input("Digite o tempo de serviço: "));
if (idade == 65 or tempoServico == 30 or idade == 60 and tempoServico == 25):
    print ("Pode se aposentar.")
else:
    print ("Não pode se aposentar.")




    """17. Leia a distância em Km e a quantidade de litros de gasolina consumidos
por um carro em um percurso, calcule o consumo em Km/l e escreva uma
mensagem de acordo com a tabela abaixo:"""
distancia = int (input("Digite a distância em km: "));
quantLitros = float (input("Digite quantos litros foram consumidos: "));
if (distancia <= 8 and quantLitros < 8):
    print ("Venda o carro");
if (distancia >= 8 and distancia <= 12 and quantLitros <= 8 and quantLitros <= 12):
    print ("Econômico!");
if (distancia >= 12 and quantLitros <= 12):
    print ("Super econômico!");


"""18. Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 2
vezes. A primeira vez deve usar a estrutura de repetição “for”, a segunda
vez a estrutura “while”."""

lista = [];
lista2 = [];

for i in range (100):
    lista.append(i + 1);
    i = i + 1;
print (lista);
i = 1;

while (i <= 100):
    lista2.append (i)
    i = i + 1;
print(lista2);



"""19. Faça um programa que peça ao usuário para digitar 10 valores e some-os
e imprima o resultado."""

lista = [];
soma = 0

def lerNum (lista):
    for i in range (10):
        lista.append(float(input("Digite um número: ")));
    
lerNum (lista);


for i in lista:
    soma += i;
print("O resultado da soma é:", soma)


"""20. Faça um programa que leia 10 inteiros e imprima sua media."""

lista = [];
soma = 0

def lerNum (lista):
    for i in range (2):
        lista.append(int(input("Digite um número: ")));
    
lerNum (lista);


for i in lista:
    soma += i;
    media = soma/2;
print("A média dos números digitados é:", media)


"""21. Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima a sua média"""
lista = [];
soma = 0;

i = 1;
while i < 10:
    aux = int(input("Digite um número inteiro positivo: "));
    if aux > 0:
        lista.append(aux);
        soma += aux;
        i += 1;

media = soma / len(lista);
print("A média dos números positivos digitados é:", media);




"""22. Faça um programa que leia um numero inteiro “N” e depois imprima os N
primeiros números naturais ímpares. """

numero = int(input("Digite um número inteiro: "));
i = 1;
aux = 0;

while aux < numero:
    if i % 2 != 0:
        print(i);
    aux += 1;
    i += 1;

"""23. Faça um programa que leia um numero inteiro positivo “N” e imprima
todos os números naturais de 0 até “N” em ordem crescente."""
numero = int(input("Digite um número inteiro positivo: "));

if numero < 0:
    print("O número digitado não é positivo.");
else:
    for i in range(numero+1):
        print(i);



"""24. Faça um programa que leia um numero inteiro positivo “N” e imprima
todos os números naturais de 0 até N em ordem decrescente."""
numero = int(input("Digite um número inteiro positivo: "));

if numero < 0:
    print("O número digitado não é positivo.");
else:
    for i in range(numero, -1, -1):
        print(i);



"""25. Faça um programa que receba dois números. Calcule e mostre: - a soma dos números pares desse intervalo de números, incluindo os
números digitados; - a multiplicação dos números ímpares desse intervalo, incluindo os
digitados"""
num1 = int(input("Digite o primeiro número: "));
num2 = int(input("Digite o segundo número: "));

soma_pares = 0;
mult_impares = 1;

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        soma_pares += i;
    else:
        mult_impares *= i;

print("A soma dos números pares é:", soma_pares);
print("A multiplicação dos números ímpares é:", mult_impares);



"""26. Faça um programa que imprima a tabuada de multiplicação de 1 a 9;"""

for i in range(1, 10):
    print(f"Tabuada do {i}");
    for x in range(1, 11):
        print(f"{i} x {x} = {i*x}");
    print();


"""27. Escreva um programa que leia um numero inteiro positivo “N” e em
seguida imprima “N” linhas do chamado Triângulo de Floyd. Para n = 6,
temos:"""

numero = int(input("Digite um número inteiro positivo: "));

aux = 1;

for i in range(1, numero + 1):
    for x in range(1, i+1):
        print(aux, end=" ");
        aux += 1;
    print();








