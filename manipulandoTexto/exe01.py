frase = 'Curso em Video Python'
print (frase[::3])
print (frase.count ('o'))
print (frase.upper().count ('c'))
print (len(frase))
frase = '   Curso em Video Python  '
print (len(frase))
frase1 = frase.strip()
print (frase1)
print (frase.replace('Python', 'Linda'))
print (frase1.find('Video'))
frase2 = frase.split()
print (frase2 [0][2])  #pega a posição 0 e mostre a letra 2
frase2_formatada = '-'.join (frase2)
print (frase2_formatada)