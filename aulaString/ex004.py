"""Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita
da direita para esquerda ou vice-versa. Por exemplo: OSSO e OVO são
palíndromos. Em textos mais complexos os espaços e pontuação são
ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma
onde os espaços foram ignorados. Faça um programa que leia uma
seqüência de caracteres, mostre-a e diga se é um palíndromo ou não."""
frase = input ("Digite uma frase:").lower().replace (" ", "")
palindromo = ""
for i in range (len(frase)):
    palindromo += frase [-i-1]

if (frase == palindromo):
    print ("A frase é um palíndromo")
else:
    print ("A frase não é um palíndromo")

