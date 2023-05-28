"""A prefeitura de uma cidade deseja fazer uma pesquisa entre seus
habitantes. Faça um algoritmo para coletar e armazenar dados sobre
o salário e número de filhos de cada habitante e após as leituras,
escrever:"""

habitantes = []  # lista para armazenar os dados dos habitantes

quantidade_habitantes = int(input("Digite a quantidade de habitantes: "))

for i in range(quantidade_habitantes):
    salario = float(input("Digite o salário do habitante: "))
    numero_filhos = int(input("Digite o número de filhos do habitante: "))

    habitante = {"salario": salario, "filhos": numero_filhos}
    habitantes.append(habitante)

# Após as leituras, realizar os cálculos e exibir as informações desejadas
total_salarios = 0
total_filhos = 0

for habitante in habitantes:
    total_salarios += habitante["salario"]
    total_filhos += habitante["filhos"]

media_salarios = total_salarios / quantidade_habitantes
media_filhos = total_filhos / quantidade_habitantes

print("Resultados:")
print("Média de salários: ", media_salarios)
print("Média de filhos: ", media_filhos)
