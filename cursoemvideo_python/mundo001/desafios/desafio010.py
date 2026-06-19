"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere: US$ 1,00 = R$ 5,25
"""
reais = float(input('Digite o valor em reais que você tem na carteira: R$ '))
dolares = reais / 5.25
print('Com R$ {:.2f} você pode comprar US$ {:.2f}.'.format(reais, dolares))
