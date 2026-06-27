"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
import math # from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an)) # sin(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(an, seno))
cosseno = math.cos(math.radians(an)) # cos(radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(an, cosseno))
tangente = math.tan(math.radians(an)) # tan(radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(an, tangente))
