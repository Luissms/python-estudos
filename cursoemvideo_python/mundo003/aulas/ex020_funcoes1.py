"""
def lin():
    print('-' * 30)

lin()
print('CURSO EM VIDEO')
lin()

def mensagem(msg):
    print('-----')
    print(msg)
    print('-----')

mensagem('SISTEMA DE ALUNOS')
"""
def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

# Programa principal
título('CURSO EM VÍDEO')
título('PYTHON É MUITO BOM!')

def soma(a, b):
    print(f'A = {a} e B = {b}.')
    s = a + b
    print(f'A soma A + B = {s}.')


# Programa principal
soma(a=4, b=5)
soma(8, 9)
soma(2, 1)


def contador(* núm):
    print(núm)

contador(2, 1, 7) # (2, 1, 7)
contador(8, 0) # (8, 0)

def contador(* núm):
    for valor in núm:
        print(f'{valor} ', end='')
print('FIM')

contador(2, 1, 7) # 2 1 7 FIM
contador(8, 0) # 8 0 FIM


def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números.')

contador(2, 1, 7) # Recebi os valores (2, 1, 7) e são ao todo 3 números. 
contador(8, 0) # Recebi os valores (8, 0) e são ao todo 2 números.

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

# Desempacotamento
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')

soma(5, 2) # Somando os valores (5, 2) temos 7.
soma(2, 9, 4) # somando os valores (2, 9, 4) temos 15.