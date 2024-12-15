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

    def busca_min(self):
        if self.root is None:
            return None
        atual = self.root
        while atual.left is not None:
            atual = atual.left
        return atual.valor

    def busca_max(self):
        if self.root is None:
            return None
        atual = self.root
        while atual.right is not None:
            atual = atual.right
        return atual.valor


def questao15():
    arvore = ArvoreBinaria()
    notas = [8, 2, 6, 7, 10]
    for nota in notas:
        arvore.add(nota)

    nota_minima = arvore.busca_min()
    nota_maxima = arvore.busca_max()

    print("Nota mínima na turma:", nota_minima)
    print("Nota máxima na turma:", nota_maxima)


questao15()
