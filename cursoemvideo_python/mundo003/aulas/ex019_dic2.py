brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1) # {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(estado2) # {'uf': 'São Paulo', 'sigla': 'SP'}
print(brasil) # [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
print(brasil[0]) # {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(brasil[1]) # {'uf': 'São Paulo', 'sigla': 'SP'}
print(brasil[0]['uf']) # Rio de Janeiro
print(brasil[1]['sigla']) # SP



estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # Usar o copy no lugar do [:]
print(brasil) # [{'uf': 'Minas', 'sigla': 'MG'}, {'uf': 'Acre', 'sigla': 'AC'}, {'uf': 'Goias', 'sigla': 'GO'}]


for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')


for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print() 