def cadastrar_usuario():
    id_usuario = input("Digite o ID do usuário: ")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    foto_url = input("URL da foto: ")
    data_cadastro = input("Data de cadastro: ")
    ultimo_login = input("Último login: ")
    ativo_input = input("Usuário ativo? (s/n): ")
    if ativo_input.lower() == "s":
        ativo = True
    else:
        ativo = False

    usuario = {
        "id_usuario": id_usuario,
        "nome": nome,
        "email": email,
        "senha": senha,
        "foto_url": foto_url,
        "data_cadastro": data_cadastro,
        "ultimo_login": ultimo_login,
        "ativo": ativo
    }
    return usuario

def mostrar_usuario(u):
    status = "Ativo" if u["ativo"] else "Inativo"
    print("Usuário:", u["id_usuario"])
    print(" Nome:", u["nome"])
    print(" Email:", u["email"])
    print(" Status:", status)
