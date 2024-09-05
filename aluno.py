

def aprovados(lista: list) -> list:
    """ retorna uma lista com os nomes da lista que tem nota maior igual a 7 """
    nomes = []
    for tupla in lista:
        if tupla[2] >= 7:
            nomes.append(tupla[0])
    return nomes



lista = []
while True:
    nome = input('Insira o nome do aluno: ')
    if nome == '':
        break
    idade = int(input('insira a idade do aluno'))
    nota = float(input("Insira a nota do aluno"))
    tupla = (nome,idade,nota)
    lista.append(tupla)
print(lista)

print(aprovados(lista))
