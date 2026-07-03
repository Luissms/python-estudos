# docstring
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    i: início da contagem
    f: fim da contagem
    p: passo da contagem
    return: sem retorno
    
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM')

contador(2, 10, 2)
help(contador)


# Parâmetros opcionais
def somar(a=0, b=0, c=0): #Os parâmetros opcionais são os "=0"
    s = a + b + c
    print(f'A soma vale {s}.')
somar(3, 2, 5)
somar(8, 4)
somar()

# ESCOPO DE VARIÁVEIS
def teste():
    x = 8 # x tem escopo local
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}.')

# Programa principal
n = 2 # Escopo global
print(f'Na função teste, n vale {n}.')
teste()
print(f'Na função teste, x vale {x}.') # X tem escopo local, por isso não vai funcionar.


def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}.') # N1 dentro vale 4.

n1 = 2
funcao()
print(f'N1 fora vale {n1}.') # N1 fora vale 2.


# RETORNO DE VALORES
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}.') # Os resultados foram 10, 4 e 6.