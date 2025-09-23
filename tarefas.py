def cadastrar_tarefa():
    id_tarefa = input("ID tarefa: ")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    data_criacao = input("Data de criação: ")
    vencimento = input("Data de vencimento: ")
    prioridade = input("Prioridade (número): ")
    categoria = input("Categoria: ")
    id_usuario = input("ID do usuário dono: ")
    id_projeto = input("ID do projeto: ")
    cor = input("Cor (hexadecimal ou nome): ")
    criado_em = input("Criado em: ")

    tarefa = {
        "id_tarefa": id_tarefa,
        "titulo": titulo,
        "descricao": descricao,
        "data_criacao": data_criacao,
        "vencimento": vencimento,
        "prioridade": prioridade,
        "categoria": categoria,
        "id_usuario": id_usuario,
        "id_projeto": id_projeto,
        "cor": cor,
        "criado_em": criado_em
    }
    return tarefa

def mostrar_tarefa(t):
    print("Tarefa:", t["id_tarefa"])
    print(" Título:", t["titulo"])
    print(" Descrição:", t["descricao"])
    print(" Vencimento:", t["vencimento"])
    print(" Prioridade:", t["prioridade"])
    print(" Categoria:", t["categoria"])
    print(" Usuário:", t["id_usuario"])
    print(" Projeto:", t["id_projeto"])
    print(" Cor:", t["cor"])
