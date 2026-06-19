"""
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""
n = int(input('Digite um número inteiro: '))
antecessor = n - 1
sucessor = n + 1
print('O número digitado foi {}. O seu antecessor é {} e o seu sucessor é {}.'.format(n, antecessor, sucessor))