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