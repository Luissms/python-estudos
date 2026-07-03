"""
dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome']) # Pedro
print(dados['idade']) # 25
dados['sexo'] = 'M' # {'nome': 'Pedro', 'idade': 25, 'sexo': 'M'}
del dados['idade'] >> {'nome': 'Pedro', 'sexo': 'M'}
filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'}
print(filme.values()) >> Vai me dar somente os valores.
print(filme.keys()) >> vai me dar as chaves.
print(filme.items()) >> vai me dar chaves e valores.

for k, v in filme.items():
    print(f'O {k} é {v}.)
"""
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#print(pessoas['nome'])
#print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys()) # dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values()) # dict_values(['Gustavo', 'M', 22])
print(pessoas.items()) # dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])
for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo'] # deleto somente a chave sexo
pessoas['nome'] = 'Leandro' # substituo o Gustavo por Leandro
pessoas['peso'] = 98.5 # adicionei a chave e valor peso = 98.5