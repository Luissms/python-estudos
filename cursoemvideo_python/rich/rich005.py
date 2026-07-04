from rich.traceback import install # Todo e qualquer erro será monitorado pela biblioteca do rich e ficará apresentado de forma mais clara.
install()

def divisao(x, y):
    return x / y

print(divisao(10, 0))
