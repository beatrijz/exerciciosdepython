"""Uma empresa concederá um aumento de salário aos seus funcionários,
variável de acordo com o cargo, conforme a tabela abaixo. Faça um
programa que leia o salário e o código do cargo de um funcionário e calcule
o seu novo salário. Se o cargo do funcionário não estiver na tabela, ele
deverá, então, receber 15% de aumento. Mostre o salário antigo, o novo
salário e a diferença entre ambos."""
codigo = int (input("Digite o código do funcionário: "))
salario = float (input("Digite o salario atual: "))

def porcentagem (porcentagem, salario):
    porcento = (porcentagem / 100) * salario
    soma = porcento + salario
    return soma

def aumento (codigo, salario):
    if codigo == 310:
        return porcentagem (5.0, salario)
    elif codigo == 456:
        return porcentagem (7.5, salario)
    elif codigo == 885:
        return porcentagem (10.0, salario)
    else:
        return porcentagem (15.0, salario)
    
salarioNovo = aumento (codigo, salario)
print (f"O seu salário era de: R${salario} reais, após o aumento, ele foi para {salarioNovo} reais, aumentou R${salarioNovo - salario} reais. ")
