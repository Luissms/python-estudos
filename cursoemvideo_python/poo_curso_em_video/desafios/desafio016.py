"""
Crie a classe Funcionario, onde podemos cadastrar nome,
setor e cargo. Crie também um método que permita ao funcionário
se apresentar.

"""
class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f"Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa Curso em Vídeo."
    
c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentar())

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentar())
