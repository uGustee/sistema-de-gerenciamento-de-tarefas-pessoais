def cadastrar_permissao():
    id_perm = input("ID permissão: ")
    id_usuario = input("ID usuário: ")
    nivel = input("Nível de acesso: ")
    criado_em = input("Criado em: ")
    perm = {
        "id_perm": id_perm,
        "id_usuario": id_usuario,
        "nivel": nivel,
        "criado_em": criado_em
    }
    return perm

def mostrar_permissao(p):
    print("Permissão:", p["id_perm"])
    print(" Usuário:", p["id_usuario"])
    print(" Nível:", p["nivel"])
