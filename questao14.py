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
        if self.root is not None:
            self.root = self._remover(valor, self.root)

    def _remover(self, valor, node_atual):
        if node_atual is None:
            return node_atual
        if valor < node_atual.valor:
            node_atual.left = self._remover(valor, node_atual.left)
        elif valor > node_atual.valor:
            node_atual.right = self._remover(valor, node_atual.right)
        else:
            if node_atual.left is None and node_atual.right is None:
                return None
            if node_atual.left is None:
                return node_atual.right
            if node_atual.right is None:
                return node_atual.left

            menor_valor = self._menor(node_atual.right)
            node_atual.valor = menor_valor
            node_atual.right = self._remover(menor_valor, node_atual.right)
        return node_atual

    def _menor(self, node):
        atual = node
        while atual.left is not None:
            atual = atual.left
        return atual.valor


def questao14():
    arvore = ArvoreBinaria()
    arvore.add(100)
    arvore.add(50)
    arvore.add(150)
    arvore.add(30)
    arvore.add(70)
    arvore.add(130)
    arvore.add(170)
    print("O valor 70 está na árvore:", arvore.buscar(70))
    print("Removendo 70...")
    arvore.remover(70)
    print("O valor 70 está na árvore após a remoção:", arvore.buscar(70))


questao14()
