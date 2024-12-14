def selection_sort(lista):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        menor = i

        for j in range(i + 1, tamanho_lista):
            if lista[j]['pontos'] < lista[menor]['pontos']:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista


def questao8():
    jogadores =[{'nome': 'Lucas', 'pontos': 100},
                {'nome': 'João', 'pontos': 50},
                {'nome': 'Maria', 'pontos': 150},
                {'nome': 'Pedro', 'pontos': 200},
                {'nome': 'Paulo', 'pontos': 20}]

    print("Questão 8")
    print("Antes do sort")
    print(jogadores)
    print("Depois do sort")
    print(selection_sort(jogadores))


questao8()

