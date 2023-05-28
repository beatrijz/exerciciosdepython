"""Elabore um algoritmo que calcule o que deve ser pago por um produto,
considerando o preço normal de etiqueta e a escolha da condição de
pagamento. Utilize os códigos a seguir para ler qual acondição de
pagamento escolhida e efetuar o cálculo adequado:"""
valor = float (input("Digite o valor contido na etiqueta:"))

def aumento (porcentagem, valor):
    porcento = (porcentagem / 100) * valor
    soma = porcento + valor
    return soma

def desconto (porcentagem, valor):
    porcento = (porcentagem / 100) * valor
    subtracao = valor - porcento
    return subtracao


def exibir_menu():
    print("Menu:")
    print("À vista em dinheiro ou cheque [1]")
    print("À vista no cartão de crédito [2]")
    print("Em duas vezes no cartão [3]")
    print("Em três vezes no cartão [4]")
    print("Em seis vezes no cartão [5]")
    print("0. Sair")

opcao = -1

while opcao != 0:
    exibir_menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Executando a Opção 1")
        print ("Total da compra já com desconto: R$", desconto(10,valor))

    
    elif opcao == 2:
        print("Executando a Opção 2")
        print ("Total da compra já com desconto: R$", desconto(15,valor))
       

    elif opcao == 3: 
        print("Executando a Opção 3")
        print ("Total da compra: R$", valor)
        
    elif opcao == 4:
        print("Executando a Opção 4")
        print ("Total da compra já com juros: R$", aumento(10,valor))

    elif opcao == 5:
        print("Executando a Opção 5")
        print ("Total da compra já com juros: R$", aumento(20,valor))
       

    elif opcao == 0:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")