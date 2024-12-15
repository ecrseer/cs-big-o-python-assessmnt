def permutar_maximo_valor(capacidade_mochila, pesos, valores, qtd, memo):

    if qtd == 0 or capacidade_mochila == 0:
        return 0

    if (qtd, capacidade_mochila) in memo:
        return memo[(qtd, capacidade_mochila)]


    if pesos[qtd - 1] > capacidade_mochila:
        resultado = permutar_maximo_valor(
            capacidade_mochila, pesos, valores, qtd - 1, memo
        )
    else:
        proximos_itens=permutar_maximo_valor(
            capacidade_mochila - pesos[qtd - 1],
            pesos,
            valores,
            qtd - 1,
            memo,
            )
        valor_com_item = (
                valores[qtd - 1]
                + proximos_itens
        )
        valor_sem_item = permutar_maximo_valor(
            capacidade_mochila, pesos, valores, qtd - 1, memo
        )
        resultado = max(valor_com_item, valor_sem_item)


    memo[(qtd, capacidade_mochila)] = resultado
    return resultado



def questao13():
    valores_dos_itens = [6, 5, 40]
    pesos_dos_itens = [10, 20, 40]
    capacidade_total = 50
    quantidade_de_itens = len(valores_dos_itens)


    memoizacao = {}


    valor_maximo = permutar_maximo_valor(
        capacidade_total, pesos_dos_itens, valores_dos_itens, quantidade_de_itens, memoizacao
    )

    print(f"O valor máximo que pode ser carregado na mochila é: {valor_maximo}")

questao13()
