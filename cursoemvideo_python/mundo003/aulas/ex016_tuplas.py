lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas são imutáveis
print(lanche)
print(lanche[1])
print(len(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi pra caramba.')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')

print(sorted(lanche)) # coloca em ordem

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(len(c))
print(c.count(5)) # 2 - Quantos tem?
print(c.index(8)) # Em que posição está?
print(c.index(5, 1)) # Em que posição está começando a contar da posição 1.

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) # Ele apaga a tupla inteira. Mas eu não posso apager somente um elemento. 
print(pessoa) # Em outras linguagens não pode ter dados de diferentes tipos, no Python sim.