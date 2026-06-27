import math # Ou eu posso colocar "from math import ceil, floor, sqrt"
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}.'.format(num, math.ceil(raiz))) # arredondamento para cima.
print('A raiz de {} é igual a {}.'.format(num, math.floor(raiz))) # Arredondamento para baixo
print('A raiz de {} é igual a {:.2f}.'.format(num, raiz)) # Colocando 2 casas decimais