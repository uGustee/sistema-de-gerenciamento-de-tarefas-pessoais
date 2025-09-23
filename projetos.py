def cadastrar_projeto():
    id_projeto = input("ID projeto: ")
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    data_inicio = input("Data início: ")
    data_fim = input("Data fim: ")
    id_usuario = input("ID usuário dono: ")
    status = input("Status: ")
    cor = input("Cor: ")
    criado_em = input("Criado em: ")
    projeto = {
        "id_projeto": id_projeto,
        "nome": nome,
        "descricao": descricao,
        "data_inicio": data_inicio,
        "data_fim": data_fim,
        "id_usuario": id_usuario,
        "status": status,
        "cor": cor,
        "criado_em": criado_em
    }
    return projeto

def mostrar_projeto(p):
    print("Projeto:", p["id_projeto"])
    print(" Nome:", p["nome"])
    print(" Status:", p["status"])
