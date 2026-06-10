# Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome: "nome da pessoa", idade: idade da pessoa)"""
    
    def __init__(self, nome = "vaziio", idade = 0): # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

        # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self): # Dunder Method
        return f"Nome: {self.nome} é Gafanhhoto (a) e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"Estado: nome: {self.nome} e idade: {self.idade}"
    
# Declaração de Objetos
g1 = Gafanhoto(nome: "Maria", idade: 17)
g1.aniversario()
#print(g1) # Quando eu coloco o nome do objeto, ele chama o método __str__() para mostrar a representação do objeto.
print(g1.__dict__()) # Attribute
print(g1.__getstate__()) # Method mostra o estado do objeto, ou seja, os valores dos atributos do objeto. Estado: nome: Maria e idade: 18
print(g1.__class__) # Attribute mostra a classe do objeto, ou seja, a classe Gafanhoto
print(g1.__doc__) # Attribute mostra a documentação da classe, ou seja, a string de documentação da classe Gafanhoto

g2 = Gafanhoto(nome: "Mauro", idade: 54)
print(g2)
print(g2.__getstate__()) # Method
    
