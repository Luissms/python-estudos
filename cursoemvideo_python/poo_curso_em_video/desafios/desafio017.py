"""
Crie a classe Produto, onde podemos cadastrar nome e preço. Crie também um método
que mostre uma etiqueta de preço do produto.

"""
from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta_preco(self):
        return f"{self.nome} custa R${self.preco:.2f}."
    
p1 = Produto("iPhone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8_500.99)
print(p1.etiqueta_preco())