import random

iteracoes_binaria = 0
iteracoes_linear = 0

def questao4():
    print("Questão 4")
    livros=gerar_livros(220)
    busca_linear(201,livros)
    busca_binaria(livros,15)
    print(f"na busca linear - O(n) : {iteracoes_linear} iterações")
    print(f"Busca binária: {iteracoes_binaria} iterações")

def busca_binaria(lista, isbn):
    global iteracoes_binaria
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        iteracoes_binaria += 1
        meio = (inicio + fim) // 2
        if lista[meio]['isbn'] == isbn:
            return meio
        elif lista[meio]['isbn'] < isbn:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1



def busca_linear(isbn, lista):
    global iteracoes_linear
    for item in lista:
        iteracoes_linear += 1
        if item['isbn'] == isbn:
            return item


def gerar_livros(qtd=100000):
    livros = []
    for isbn in range(qtd):
        livro = {'isbn': isbn}
        livros.append(livro)
    return livros

questao4()
