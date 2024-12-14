from questao7 import TabelaHash


class RedeSocial:
    def __init__(self):
        self.usuarios = TabelaHash()
        self.usuarios.inseri('maria', {'nome': 'Maria', 'idade': 30})
        self.usuarios.inseri('ana', {'nome': 'Ana', 'idade': 45})
        self.usuarios.inseri('lucas', {'nome': 'Lucas', 'idade': 40})
        self.usuarios.inseri('joao', {'nome': 'João', 'idade': 25})

    def buscar_perfil(self, nome):
        return self.usuarios.buscar(nome)

    def adiciona_perfil(self, nome, idade):
        self.usuarios.inseri(nome, {'nome': nome, 'idade': idade})
        return self.usuarios


def questao9():
    rede_social = RedeSocial()
    rede_social.adiciona_perfil('pedro', 35)
    print("Perfil do pedro adicionado!")

    buscado = rede_social.buscar_perfil('pedro')
    print(f"Perfil do pedro: {buscado}")


questao9()
