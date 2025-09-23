def cadastrar_comentario():
    id_comentario = input("ID comentário: ")
    id_tarefa = input("ID tarefa: ")
    id_usuario = input("ID usuário: ")
    conteudo = input("Conteúdo: ")
    data_comentario = input("Data comentário: ")
    criado_em = input("Criado em: ")
    comentario = {
        "id_comentario": id_comentario,
        "id_tarefa": id_tarefa,
        "id_usuario": id_usuario,
        "conteudo": conteudo,
        "data_comentario": data_comentario,
        "criado_em": criado_em
    }
    return comentario

def mostrar_comentario(c):
    print("Comentário:", c["id_comentario"])
    print(" Usuário:", c["id_usuario"])
    print(" Texto:", c["conteudo"])
