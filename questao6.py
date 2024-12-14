import time


def bubble_sort_ordena_nota(lista, index_fim):
    tudo_ordenado = True
    iteracoes = 0
    for i in range(index_fim):
        iteracoes += 1
        if lista[i] > lista[i + 1]:
            iteracoes += 1
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            tudo_ordenado = False
    return lista, tudo_ordenado, iteracoes


def bubble_sort_completo(lista):
    index_fim = len(lista) - 1
    tudo_ordenado = False
    iteracoes = 0

    while not tudo_ordenado:
        tudo_ordenado = True
        lista, tudo_ordenado, iterou = bubble_sort_ordena_nota(lista, index_fim)
        iteracoes += iterou
        index_fim -= 1
    return lista, iteracoes


def questao6():
    mil_precos = [preco for preco in range(1000, 0, -1)]
    dezmil_precos = [preco for preco in range(10000, 0, -1)]

    print(f"""Mil precos de produtos:
    {mil_precos[0:10]}...
    
    Dezmil precos de produtos:
    {dezmil_precos[0:20]}
    ----
    iniciando ordenacao....
    """)

    inicio = time.time()
    ordenado_mil, iterado_mil = bubble_sort_completo(mil_precos)
    fim = time.time()

    print(f"""Ordenacao: Mil precos de produtos - Iterações: {iterado_mil}
    Lista ordenada: {ordenado_mil}""")
    print(f"Tempo de execução: {fim - inicio} segundos")

    inicio = time.time()
    ordenado, iterado_dezmil = bubble_sort_completo(dezmil_precos)
    fim = time.time()

    print(f"""Ordenacao: Dezmil precos de produtos - Iterações: {iterado_dezmil}
    Lista ordenada: {ordenado}""")
    print(f"Tempo de execução: {fim - inicio} segundos")

questao6()
