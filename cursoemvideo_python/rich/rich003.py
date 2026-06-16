from rich import print
from rich.table import Table

tabela = Table(title='Tabela de Preços')

tabela.add_column('Produto', justify='center', style='cyan', no_wrap=True)
tabela.add_column('Preço', justify='center', style='magenta')

tabela.add_row('Lápis', 'R$ 5,00')
tabela.add_row('Caneta', '[green]R$ 2,00[/]')

print(tabela)
