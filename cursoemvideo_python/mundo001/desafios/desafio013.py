"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salario = float(input('Digite o salário do funcionário: R$ '))
aumento = salario * 0.15
novo_salario = salario + aumento
print('O salário original do funcionário é R$ {:.2f}. Com o aumento de 15%, o novo salário é R$ {:.2f}.'.format(salario, novo_salario))
