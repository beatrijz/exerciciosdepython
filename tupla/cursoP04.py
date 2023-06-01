numeros = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Cartoze', 'Quinze', 'Dezesseis', 'Dezessete'
           , 'Dezoito', 'Dezenove', 'Vinte')
numero = int (input("Digite um número: "))
for elemento in range (0, len (numeros)):
    if (numero == elemento):
        print (numeros[elemento - 1])

