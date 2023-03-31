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



