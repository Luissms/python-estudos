nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade: '))
cnh = input('Você possui CNH? ').lower()
cnh = 's'

if idade >= 18 and cnh == 's':
    print('Pode dirigir.')
else:
    print('Não pode dirigir.')

