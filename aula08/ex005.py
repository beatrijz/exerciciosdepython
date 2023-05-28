"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de
qualquer número inteiro entre 1 a 10. O usuário deve informar de qual
numero ele deseja ver a tabuada. A saída deve ser conforme o
exemplo abaixo:"""
numero = int (input("Digite o número: "))
print (f"Tabuada de {numero}")
i = 1
for i in range (11):
    multiplicacao = numero * i
    print (f"{numero} X {i} = {multiplicacao}")

