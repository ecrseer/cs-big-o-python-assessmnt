import os

def navegar_diretorios(caminho):
    try:
        with os.scandir(caminho) as entradas:
            for entrada in entradas:
                print(f"Lendo... {entrada.path}")

                if entrada.is_dir(follow_symlinks=False):
                    navegar_diretorios(entrada.path)
    except PermissionError:
        print(f"Sem permissão p acessar {caminho}")



    def questao12():
        navegar_diretorios("./atq12")

    questao12()

