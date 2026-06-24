"""
Crie a classe Churrasco, onde seja possível informar quantas
pessoas vão participar e mostre quanto de carne deve ser
comprado, o custo total do churrasco e o preço por pessoa.
"""
from rich import print
from rich.panel import Panel

class Churrasco:
    # Atributos de Classe
    consumo_padrao:float = 0.400 # Cada pessoa come em média 400g de carne
    preco_kg:float = 82.40 # Cada kg de carne custa R$82.40

    def __init__(self, titulo, quant):
        # Atributos de Instância
        self.titulo = titulo
        self.participantes = quant

    def __str__(self):
        return f"Esse é {self.titulo} com {self.participantes} pessoas participando."
    
    def calcular_qtd_carne(self) -> float:
        return self.participantes * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * self.__class__.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes
    
    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.participantes} convidados[/]"
        conteudo += f"\nCada participante comerá {Churrasco.consumo_padrao} kg e cada kg custa R${Churrasco.preco_kg:,.2f}"
        conteudo += f"\nRecomendo [blue]comprar {self.calcular_qtd_carne():.3f}Kg[/] de carne"
        conteudo += f"\n O custo total será de [green]R${self.calcular_custo_total():,.2f}[/]"
        conteudo += f"\nCada pessoa pagará [yellow]R${self.calcular_custo_individual():.2f}[/] para participar."
        painel = Panel(conteudo, title=self.titulo)
        print(painel)

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()

c2 = Churrasco("Festa do fim de ano", 80)
c2.analisar()
# CONSIDERE:
# Consumo padrão: 400g por pessoa
# Preço: R$82,40/Kg

