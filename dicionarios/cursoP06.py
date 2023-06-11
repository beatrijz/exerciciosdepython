jogadores = []
jogador = {}
jogador['nome'] = input('Digite o nome do jogador: ')
jogador['quant_partidas'] = int(input('Digite a quantidade de partidas: '))
jogador ['quant_gol'] = 0
i = 1
while i <= jogador ['quant_partidas']:
    gol = int(input (f'Qual foi a quantidade de gol (s) na partida {i}:'))
    jogador ['quant_gol'] += gol
    i+=1

jogador['gols_campeonato'] = int(input('Quantidade de gols feitos no campeonato: '))
jogadores.append(jogador)

with open('dicionarios/jogadores06.txt', 'a') as file:
    for jog in jogadores:
        file.write(f"Nome: {jog['nome']}\n")
        file.write(f"Quantidade de partidas: {jog['quant_partidas']}\n")
        file.write(f"Foi um total de: {jog['quant_gol']} gols ;por cada partida.\n")
        file.write(f"Quantidade de gols no campeonato: {jog['gols_campeonato']}\n")
        file.write("\n")