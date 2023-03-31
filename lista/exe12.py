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