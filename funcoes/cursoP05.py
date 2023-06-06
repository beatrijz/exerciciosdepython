def escreva (txt):
    print ('  ' + '-' * len (txt) + '  ')
    print (' ',txt, '  ')
    print ('  ' + '-' * len (txt) + '  ')


def contador (inicio, fim, passo):
    list = []
    if passo > 0:
        for num in range (inicio, fim, passo):
            list.append (num)
        escreva (list)
    else:
        for num in range (inicio, fim, -passo):
            list.append (num)
        print (list)

            

contador (1, 10, 1)
contador (10, 0, 2)
