class TabelaHash:
    def __init__(self):
        self.tabela = {}

    def inseri(self, chave, valor):
        self.tabela[chave] = valor

    def remover(self, chave):
        if chave in self.tabela:
            del self.tabela[chave]
            return True
        return False

    def buscar(self, chave):
        return self.tabela.get(chave)

    def __str__(self):
        resultado = []
        for chave, valor in self.tabela.items():
            resultado.append(f"{chave}: {valor}")
        return "{ " + ", ".join(resultado) + " }"


def tem_valor_duplicado_o_linear(numeros):
    lidos = TabelaHash()

    for i in range(len(numeros)):
        ja_foi_lido = lidos.buscar(numeros[i])
        if ja_foi_lido:
            return True, numeros[i]
        lidos.inseri(numeros[i], True)
    return False, None


def questao7():
    print('\nQuestao 7: buscar duplicado - O(n):\n ')
    lista = [31, 54, 12, 22, 32, 11, 22]
    duplicado, numero = tem_valor_duplicado_o_linear(lista)
    if duplicado:
        print(f'\nNumero {numero} duplicado')
    else:
        print('\nNão tem duplicado')


questao7()
