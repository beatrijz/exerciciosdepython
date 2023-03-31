""" 3. Faça um programa que armazene as idades e as alturas de 4 alunos. Seu programa
deve exibir quantos alunos com mais de 13 anos possuem uma altura inferior à
altura média dentre todos os alunos. """
nomes = [];
idades = [];
alturas = [];

def armazenamento (nomes, idades, alturas):
    i = 0;
    while( i <= 2):
        nomes.append(input ("Digite o nome: "));
        idades.append (int(input ("Digite a idade: ")));
        alturas.append (float(input ("Digite a altura: ")));
    i=+1;print ('O total da lista é: {}'.format(nomes));


armazenamento (nomes, idades, alturas);