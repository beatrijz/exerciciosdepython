"""
2. Faça um programa para a leitura de duas notas parciais de um aluno. 
3. A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;

4. A mensagem “Aprovado com Distinção”, se a média for igual a dez;
5. A mensagem “Reprovado” se a média for menor de do que sete; """
nota1 = float (input("Digite a primeira nota: "));
nota2 = float (input("Digite a segunda nota: "));

media = (nota1 + nota2)/2;

if (media == 10):
   print ('Aprovado com distinção: {}' .format (media));
elif (media >= 7):
   print ('Você foi aprovado: {}' .format (media));
elif (media < 7):
   print ('Você foi reprovado: {}' .format (media));