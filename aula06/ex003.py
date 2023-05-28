"""3. Elaborar um algoritmo que, dada a idade de um nadador, classificá-lo nas
categorias: infantil A (5 - 7 anos), infantil B (8 -10 anos), juvenil A (11 - 13
anos), juvenil B (14 -17 anos) e adulto (maiores que 18 anos)."""
nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))

def categorias(idade):
    if idade >= 18:
        return "adulto"
    elif idade >= 14:
        return "juvenil B"
    elif idade >= 11:
        return "juvenil A"
    elif idade >= 8:
        return "infantil B"
    elif idade >= 5:
        return "infantil A"
    else:
        return "idade inválida"

nadador = categorias(idade)
print(f"O nadador(a) {nome} está na categoria: {nadador}")



