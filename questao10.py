class Pilha:
    def __init__(self, tamanho_maximo=10):
        self.topo = -1
        self.itens = [None] * tamanho_maximo
        self.tamanho_maximo = tamanho_maximo

    def is_full(self):
        return self.topo == self.tamanho_maximo - 1

    def is_empty(self):
        return self.topo == -1

    def push(self, item):
        if self.is_full():
            print("Pilha cheia")
            return
        self.topo += 1
        self.itens[self.topo] = item

    def pop(self):
        if self.is_empty():
            print("Pilha vazia")
            return
        item = self.itens[self.topo]
        self.itens[self.topo] = None
        self.topo -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Pilha vazia ")
            return
        return self.itens[self.topo]

    def size(self):
        return self.topo + 1

    def display(self):
        if self.is_empty():
            print("Pilha vazia")
        else:
            print("Pilha: ")
            for i in range(self.topo + 1):
                print(self.itens[i])
            print()


class NavegadorWeb:
    def __init__(self):
        self.pilha = Pilha()
        self.pagina_atual = None

    def acessar_pagina(self, pagina):
        self.pilha.push(self.pagina_atual)
        print("Acessando pagina...")
        self.pagina_atual = pagina

    def voltar_pagina(self):
        if self.pilha.is_empty():
            print("Não há páginas para voltar")
            return
        print("Voltando página...")
        self.pagina_atual = self.pilha.pop()

    def avancar_pagina(self):
        if self.pagina_atual is None:
            print("Não há páginas para avançar")
            return
        self.pilha.push(self.pagina_atual)
        self.pagina_atual = None

    def exibir_pagina_atual(self):
        if self.pagina_atual is None:
            print("Não há página atual")
        else:
            print(f"Página atual: {self.pagina_atual}")


def questao10():
    web = NavegadorWeb()
    web.acessar_pagina("www.google.com")
    web.exibir_pagina_atual()

    web.acessar_pagina("www.facebook.com")
    web.exibir_pagina_atual()

    web.voltar_pagina()
    web.exibir_pagina_atual()


questao10()
