"""O IMC (índice de massa corpórea) indica o grau de obesidade de uma pessoa. Este
índice é obtido pelo peso (em kg) dividido pelo quadrado da altura (em metros). A
tabela a seguir apresenta as faixas deste índice:"""
peso = float (input("Digite o seu peso: "))
altura = float (input("Digite a sua altura: "))


def IMC (peso, altura):
    calculo = peso / altura**2
    if calculo < 20:
        return "Peso abaixo do normal"
    elif calculo >= 20 and calculo < 25:
        return "Peso normal"
    elif calculo >= 25 and calculo < 30:
        return "Sobrepeso"
    elif calculo >= 30 and calculo < 35:
        return "Obesidade leve"
    elif calculo >= 35 and calculo < 40:
        return "Obesidade morderada"
    else:
        return "Obesidade mórbida"
    
imc = IMC(peso, altura)
print (imc)