
"""Faça um Programa que peça dois números e imprima a soma."""

aux = 0;

def somar (num1, num2):
    soma = num1 + num2;
    return soma

def verifica(aux, repetir):
    if aux > 0 and aux != 0 and repetir == "s":
        somar(num1, num2)
    else:
        print("Programa finalizado.")

while True:
    num1 = int (input("Digite o primeiro número:"))
    num2 = int (input("Digite o segundo número:"))
    resultado = somar(num1, num2)
    print(f"A soma dos dois números é: {resultado}")
    aux += 1
    repetir = input("Deseja fazer a conta novamente? (s/n) ")
    if repetir == "n":
        break

      
verifica (aux, repetir);
