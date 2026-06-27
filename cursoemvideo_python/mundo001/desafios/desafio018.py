"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(an, tangente))
