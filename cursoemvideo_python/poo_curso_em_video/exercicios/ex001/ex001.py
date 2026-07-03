"""
Classe é um molde, um projeto de algo que queremos construir. O objeto é uma instância de uma classe. Ela é um modelo para criar objetos. Atributos são as características do objeto,
e métodos são as ações que o objeto pode realizar. Instância é um objeto criado a partir 
de uma classe, ou seja, é uma ocorrência específica da classe. Coisa material ou abstrata que é feita a partir de um modelo e pode ser descrita por meio de suas características, comportamentos e estado atual.

"""
# Declaração de Classe

class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    

# Declaração de Objetos
g1 = Gafanhoto() # Instância da Classe Gafanhoto
g1.nome = "Maria" 
g1.idade = 17
g1.aniversario() # Chama o método para incrementar a idade
print(g1.mensagem())

g2 = Gafanhoto() # Outra Instância da Classe Gafanhoto
g2.nome = "Mauro"
g2.idade = 53
g2.aniversario() # Chama o método para incrementar a idade
print(g2.mensagem())