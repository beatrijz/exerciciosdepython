
def recursao (i):
    print ('imprimindo a Recursão ')
    i += 1
    if (i <= 5):
        return recursao(i)
    else:
        return
recursao (0)