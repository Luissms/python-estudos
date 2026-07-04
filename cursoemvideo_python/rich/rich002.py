from rich import print
from rich.panel import Panel

caixa = Panel('[white]Esse aqui é um painel de exemplo[/]:+1:', title='Mensagem', style='red', width=40, subtitle='Feito com Rich')

print(caixa)


"""
title >> título do painel
style >> coloca tudo em vermelho
width >> largura do painel 
"""