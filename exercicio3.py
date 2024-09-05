def calcular(estoque: dict) -> float:
    """ retorna o valor total em estoque"""
    total = 0
    for valor in estoque.values():
        total += valor[0] * valor[1]
    return total



estoque = {}
while True:
    nome = input("Insira o nome do produto: ")
    if nome == "":
        break
    preço = float(input('Insira o preçõ: '))
    quantidade = int(input('Insira a quantidade: '))
    estoque[nome] = (preço,quantidade)
print(estoque)

print(estoque)
print(f'Total em estoque: {calcular(estoque)}')
