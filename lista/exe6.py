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
