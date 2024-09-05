dicionario = {}
texto = input('Insira seu texto aqui :')
x = texto.split()
for char in x:
    if char in dicionario:
        dicionario[char] += 1
    else:
        dicionario[char] = 1
print(dicionario)