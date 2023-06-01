times = ('Botafogo', 'Palmeiras', 'São Paulo', 'Atlético-MG', 'Grêmio',
          'Cruzeiro', 'Flamengo', 'Fortaleza')
tupla_ordenada = tuple (sorted(times))
for pos in range (0, len (times)):
    if "Flamengo" == times [pos]:
        print ("A posição do time do Flamengo, é: ", pos + 1)
print ("Os cinco primeiros colocados são: ", times [:5])
print ("Os últimos quatro colocados: ", times [4:])
print ("A tupla em ordem", tupla_ordenada)
