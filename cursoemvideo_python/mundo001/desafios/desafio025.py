"""
Crie um programa que leia um nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower())) # ou 'SILVA' in nome.upper()