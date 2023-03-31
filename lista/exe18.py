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
