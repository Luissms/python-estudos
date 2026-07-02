# Listas são mutáveis
# Listas []
#lanche.append('') >> Estou adicionando outro elemento na lista
#lanche.insert(0, 'x') >> Estou adicionando o elemento x na posição 0.
#del lanche[3] >> Deletando o elemento da posição 3.
#lanche.pop(3) >> O pop elimina o último elemento, mas aí ele elimina o elemento 3.
#lanche.remove('x') >> elimino pelo elemento. E refaço o posicionamento.
#if 'x' in lanche:
#   lanche.remove('x') >> removo somente se o elemento estiver na lista.
"""
valores = list(range(4, 11)) >> Crio uma lista (4, 5, 6, 7, 8, 9, 10)
valores = [8, 2, 5, 4, 9, 3, 0] >> pra eu colocar em ordem basta >> valores.sort()
valores.sort(reverse=True) >> organizo em decrescente
len(valores) >> quantos elementos eu tenho na lista
"""
num = [2, 5, 9, 11]
num[2] = 3 # Vai alterar o valor de 9 para 3
print(num)
num.append(7) # vai incluir o 7 no final da lista [2, 5, 9, 11, 7]
num.sort(reverse=True) # a lista fica [7, 5, 3, 2, 1]
num.insert(2, 0) # Adicionei o 0 na posição 2. [7, 5, 0, 3, 2, 1]
num.pop() # Elimina o valor 1.
num.insert(2, 2) # Inclui o valor 2 na posição 2 >> [7, 5, 2, 3, 2, 1]
num.remove(2) # Elimina o primeiro valor 2 que estiver na lista. [7, 5, 3, 2, 1]
# num.remove(4) # Vai dar erro pois não tem o número 4 na lista.
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')

# Se eu quiser a chave e os valores:
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista.')


valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista.')

# Cuidado com isso:
a = [2, 3, 4, 7]
b = a[:] # com o [:] eu não crio uma ligação entre as listas
b[2] = 8
print(f'Lista A: {a}') # [2, 3, 8, 7]
print(f'Lista B: {b}') # [2, 3, 8, 7] vai mudar as duas listas.


