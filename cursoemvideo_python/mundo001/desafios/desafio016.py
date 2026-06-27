"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.
"""
import math # Ou from math import trunc
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, math.trunc(num))) # Ou (num, trunc(num))

# Ou podemos fazer assim:

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, int(num)))

