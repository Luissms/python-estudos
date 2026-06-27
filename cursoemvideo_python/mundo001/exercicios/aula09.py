frase = 'Curso em Vídeo Python'
print(frase[3]) # s
print(frase[3:13]) # so em Víde
print(frase[:13]) # Curso em Víde
print(frase[13:]) # o Python
print(frase[1:15]) # urso em Vídeo
print(frase[1:15:2]) # us mVdo
print(frase[1::2]) # us mVdoPto
print(frase[::2]) # Croe íe yhn
print(frase.count('o')) # 3 - Conta a quantidade de vezes que aparece a letra "o"
print(frase.upper().count('O')) # 3 - Se tiverem letras maiúsculas eu transformo tudo em maíusculo e conto.
print(len(frase)) # 21 - Quantidade de caracteres que tem a frase, contando os espaços.
print(len(frase.strip())) # 21 - Ele tira os espaços de antes e de depois e conta.
print(frase.replace('Python', 'Android')) # Troca o Python por Android.
print(frase[0]) # C se eu fizer frase[0] = 'J' vai dar erro pois é imutável.
print('Curso' in frase) # True
print(frase.find('Vídeo')) # 9
print(frase.lower().find('vídeo')) # com a letra minúscula não vai achar, mas se eu colocar tudo em minúsculo vai achar.
print(frase.split()) # ['Curso', 'em', 'Vídeo', 'Python'] se eu quiser eu posso colocar dentro de uma variável e depois print na variável com [0] vai aparecer somente Curso. O join junta tudo de novo.