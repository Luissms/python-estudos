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

