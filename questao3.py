def buscar_contato_por_nome(nome, contatos=[{'nome': 'Lucas', 'telefone': '1234-5678'}]):
    for contato in contatos:
        if contato['nome'] == nome:
            return contato['telefone']



def questao3():
    contatos = [{'nome': 'Lucas', 'telefone': '1234-5678'},
                {'nome': 'João', 'telefone': '8765-4321'},
                {'nome': 'Maria', 'telefone': '9999-9999'}]
    contato=buscar_contato_por_nome('Lucas', contatos)
    print(f"O telefone do Lucas é: {contato}")

questao3()
