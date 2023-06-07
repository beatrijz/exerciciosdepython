import random

jogadores = dict ()
i = 1
while i <= 4:
    jogador = {}
    jogador ['nome'] = str (input ('Digite o nome do jogador: '))
    jogador ['numero_sorteado'] = random.randint(0, 20)
    i += 1
    jogadores [i] = jogador

maior_numero = -1
jogador_sorteado = ""
for jogador in jogadores.values():
    numero_sorteado = jogador['numero_sorteado']
    if numero_sorteado > maior_numero:
        maior_numero = numero_sorteado
        jogador_sorteado = jogador['nome']

print(f'O jogador sorteado foi: {jogador_sorteado} com o número {maior_numero}')