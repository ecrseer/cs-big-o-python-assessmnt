class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None


class ArvoreBinaria:
    def __init__(self):
        self.root = None

    def add(self, valor):
        if self.root is None:
            self.root = Node(valor)
        else:
            self._add_no_node(valor, self.root)

    def _add_no_node(self, valor, node):
        if valor < node.valor:
            if node.left is None:
                node.left = Node(valor)
            else:
                self._add_no_node(valor, node.left)
        else:
            if node.right is None:
                node.right = Node(valor)
            else:
                self._add_no_node(valor, node.right)

    def buscar(self, valor):
        if self.root is None:
            return False
        else:
            return self._buscar_no_node(self.root, valor)

    def _buscar_no_node(self, node_atual, valor):
        if node_atual is None:
            return False
        if valor == node_atual.valor:
            return True
        if valor < node_atual.valor:
            return self._buscar_no_node(node_atual.left, valor)
        return self._buscar_no_node(node_atual.right, valor)

    def remover(self, valor):
        self.root = self._remover_no(self.root, valor)

    def _remover_no(self, node, valor):
        if node is None:
            return node

        if valor < node.valor:
            node.left = self._remover_no(node.left, valor)
        elif valor > node.valor:
            node.right = self._remover_no(node.right, valor)
        else:
            if node.left is None and node.right is None:
                return None

            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            menor_valor_direita = self.busca_min(node.right)
            node.valor = menor_valor_direita
            node.right = self._remover_no(node.right, menor_valor_direita)

        return node

    def busca_min(self, node):
        atual = node
        while atual.left is not None:
            atual = atual.left
        return atual.valor

    def ordena(self):
        resultado = []
        self._ordena_a_partir(self.root, resultado)
        return resultado

    def _ordena_a_partir(self, node, resultado):
        if node is not None:
            self._ordena_a_partir(node.left, resultado)
            resultado.append(node.valor)
            self._ordena_a_partir(node.right, resultado)


def questao16():
    arvore = ArvoreBinaria()
    codigos = [45, 25, 65, 20, 30, 60, 70]
    for codigo in codigos:
        arvore.add(codigo)

    print("Árvore em ordem crescente (inicial):", arvore.ordena())

    arvore.remover(20)
    print("Após remover 20 (nó folha):", arvore.ordena())

    arvore.remover(25)
    print("Após remover 25 (nó com um filho):", arvore.ordena())

    arvore.remover(45)
    print("Após remover 45 (nó com dois filhos):", arvore.ordena())


questao16()
