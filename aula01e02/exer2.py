""" Construa um algoritmo na forma de pseudocódigo que imprima a média
aritmética dos números 8, 9 e 7. 
2. 
Modifique o algoritmo para imprimir também a média dos números 4, 5 e 6. 
3. 
Realize mais uma modificação para que o algoritmo imprima a soma das
duas médias e a média das médias. """

lista1 = [8,9,7];
lista2 = [4,5,6];

i = 0;
soma = 0;

for i in range(3):
   n = lista1[i]; 
   soma = soma + n;
   i += 1;
   
media1 = soma/3;
print ('A média da primeira lista é: {}'.format(media1));

y = 0;
soma2 = 0;

for y in range(3):
   n1 = lista2[y]; 
   soma2 = soma2 + n1;
   y += 1;
   media2 = soma2/3;
print ('A média da segunda lista é: {}'.format(media2));

media = 0;
media = (media1 + media2)/2;
print ('A média das médias é: {}'.format (media));