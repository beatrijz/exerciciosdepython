pessoas = {'nome': 'Beatriz', 'sexo': 'F', 'idade': 22 }
#print (pessoas['nome'])
#print (f'O {pessoas["nome"]} tem {pessoas ["idade"]}')
#print (pessoas.keys())
#print (pessoas.values())
#print (pessoas.items())
"""for k in pessoas.keys ():
    print (k)"""
pessoas ['nome'] = 'Pâmela'
pessoas ['peso'] = '60kg'
for k, v in pessoas.items ():
    print (f'{k} = {v}')