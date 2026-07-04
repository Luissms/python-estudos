class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos.
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada para {self.titular} com saldo inicial de R${self.saldo:.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo."

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo:.2f}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saldo insuficiente para saque de R${valor:.2f}. Saldo atual: R${self.saldo:.2f}")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo:.2f}")


c1 = ContaBancaria(id=112, nome="Fernando", saldo=3000)
c1.depositar(500)
c1.sacar(2_000_000)
print(c1)