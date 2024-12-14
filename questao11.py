class Fila:
    def __init__(self, tamanho_maximo):
        self.inicio = 0
        self.fim = 0
        self.tamanho_max = tamanho_maximo
        self.tamanho_atual = 0
        self.itens = [None] * tamanho_maximo

    def is_empty(self):
        return self.tamanho_atual == 0

    def is_full(self):
        return self.tamanho_atual == self.tamanho_max

    def enqueue(self, item):
        if self.is_full():
            print("Erro: A fila está cheia")
            return

        self.itens[self.fim] = item
        self.fim = self.fim + 1
        self.tamanho_atual += 1
        if self.fim == self.tamanho_max:
            self.fim = 0

    def dequeue(self):
        if self.is_empty():
            print("Erro: A fila está vazia")
            return None

        primeiro_fila = self.itens[self.inicio]
        self.itens[self.inicio] = None
        self.inicio = self.inicio + 1
        self.tamanho_atual -= 1

        if self.inicio == self.tamanho_max:
            self.inicio = 0

        return primeiro_fila

    def peek(self):
        if self.is_empty():
            print("Erro: A fila está vazia")
            return None
        return self.itens[self.inicio]

    def size(self):
        return self.tamanho_atual

    def display(self):
        if self.is_empty():
            print("A fila está vazia")
        else:
            print("Fila:\n")
            for i in range(self.tamanho_atual):
                index = (self.inicio + i) % self.tamanho_max
                print(self.itens[index], end=" ")
            print()


class AtendimentoCliente:
    def __init__(self):
        self.fila = Fila(10)
        self.cliente_atual = None

    def adiciona_fila(self, cliente):
        self.cliente_atual = cliente
        self.fila.enqueue(self.cliente_atual)
        print("chegou cliente:", cliente)

    def proximo_cliente(self):
        if self.fila.is_empty():
            print("Não há clientes para atender")
        else:
            atual = self.fila.dequeue()
            print(f"\nAtendendo próximo cliente: {atual}")
            self.cliente_atual = atual


def questao_11():
    print("\nQuestao 11:  Atendimento ao Cliente")
    atendimento = AtendimentoCliente()
    atendimento.adiciona_fila("Danilo")
    atendimento.adiciona_fila("João")
    atendimento.proximo_cliente()

    atendimento.adiciona_fila("Maria")
    atendimento.proximo_cliente()
    atendimento.proximo_cliente()



questao_11()
