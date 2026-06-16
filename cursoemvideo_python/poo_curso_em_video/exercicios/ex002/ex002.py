# Declaração de Classe

class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
    Para criar uma nova pessoa, use
    variável = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "vazio", idade = 0): # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1
      
    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"Estado: nome = {self.nome}, idade = {self.idade}"

# Declaração de Objetos
g1 = Gafanhoto(nome="Maria", idade=17) # Instância da Classe Gafanhoto
g1.aniversario() # Chama o método para incrementar a idade
print(g1)
print(g1.__class__) # Imprime a classe do objeto g1, que é <class '__main__.Gafanhoto'>

g2 = Gafanhoto(nome="Mauro", idade=53) # Outra Instância da Classe Gafanhoto
g2.aniversario() # Chama o método para incrementar a idade
print(g2)
print(g2.__dict__) # Imprime o dicionário de atributos do objeto g2, que é {'nome': 'Mauro', 'idade': 54}
print(g2.__getstate__()) # Imprime o estado do objeto g2 usando o método __getstate__, que é "Estado: nome = Mauro, idade = 54"

print(g1.__doc__) # Imprime a documentação da classe Gafanhoto