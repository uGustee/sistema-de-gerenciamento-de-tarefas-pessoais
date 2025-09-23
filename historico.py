def cadastrar_historico():
    id_hist = input("ID histórico: ")
    id_tarefa = input("ID tarefa: ")
    acao = input("Ação: ")
    data_acao = input("Data da ação: ")
    id_usuario = input("ID usuário: ")
    criado_em = input("Criado em: ")
    historico = {
        "id_hist": id_hist,
        "id_tarefa": id_tarefa,
        "acao": acao,
        "data_acao": data_acao,
        "id_usuario": id_usuario,
        "criado_em": criado_em
    }
    return historico

def mostrar_historico(h):
    print("Histórico:", h["id_hist"])
    print(" Ação:", h["acao"])
    print(" Usuário:", h["id_usuario"])
