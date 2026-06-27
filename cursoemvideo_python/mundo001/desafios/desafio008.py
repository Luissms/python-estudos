"""
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""
m = float(input('Digite um valor em metros: '))
cm = m * 100
mm = m * 1000
print('O valor de {}m corresponde a {}cm e {}mm.'.format(m, cm, mm))
