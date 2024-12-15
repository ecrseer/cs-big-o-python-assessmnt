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
        if valor == node_atual.valor:
            return True
        if valor < node_atual.valor and node_atual.left is not None:
            return self._buscar_no_node(valor, node_atual.left)
        if valor > node_atual.valor and node_atual.right is not None:
            return self._buscar_no_node(valor, node_atual.right)
        return False

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

            node_atual.valor = self._menor(node_atual.right)
            node_atual.right = self._remover(node_atual.valor, node_atual.right)
        return node_atual

    def _menor(self, node):
        if node.left is not None:
            node= node.left
        else:
            return self

