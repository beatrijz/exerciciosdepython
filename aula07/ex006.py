"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a
quantidade de centenas, dezenas e unidades do mesmo. """
numero = int(input("Digite um número inteiro menor que 1000: "))

if numero < 1000:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = (numero % 100) % 10

    # Verifica a quantidade de centenas
    if centenas == 1:
        centenas_texto = "1 centena"
    else:
        centenas_texto = f"{centenas} centenas"

    # Verifica a quantidade de dezenas
    if dezenas == 1:
        dezenas_texto = "1 dezena"
    else:
        dezenas_texto = f"{dezenas} dezenas"

    # Verifica a quantidade de unidades
    if unidades == 1:
        unidades_texto = "1 unidade"
    else:
        unidades_texto = f"{unidades} unidades"

    # Imprime o resultado
    print(f"O número {numero} possui {centenas_texto}, {dezenas_texto} e {unidades_texto}.")
else:
    print("Número inválido. O número deve ser menor que 1000.")