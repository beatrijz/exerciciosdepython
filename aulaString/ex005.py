"""Faça uma função que recebe uma string que representa uma cadeia de DNA
e gera a cadeia complementar. A entrada e saída de dados deve ser feita
pelo programa principal."""
dna = (input ("Digite a cadeia de DNA: ")).upper()
complementar = dna.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c')
complementar = complementar.upper()
print (complementar)