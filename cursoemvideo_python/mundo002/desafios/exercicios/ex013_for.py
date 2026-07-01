for c in range(0, 6):
    print('Oi')
print('Fim')


for c in range(0, 6):
    print(c)
print('Fim')

for c in range(6, 0, -1): #Pra eu contar de forma decrescente, eu preciso colocar o passo negativo
    print(c)
print('Fim')

for c in range(0, 7, 2): # Contando de 2 em 2, ou seja, pulando de 2 em 2
    print(c)
print('Fim')


n = int(input('Digite um número: '))
for c in range(0, n): #Se eu quiser contar o número digitado, basta eu colocar n+1
    print(c)
print('Fim')


i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')


for c in range(0, 3):
    n = int(input('Digite um valor: ')) # Vai pedir para digitar valores 3 vezes.
print('Fim')


s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n # A cada vez que o laço for executado, ele vai somar o valor digitado com o valor anterior.
print('O somatório de todos os valores foi {}.'.format(s))

