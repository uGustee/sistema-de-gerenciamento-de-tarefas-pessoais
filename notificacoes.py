def cadastrar_notificacao():
    id_notif = input("ID notificação: ")
    id_usuario = input("ID usuário: ")
    mensagem = input("Mensagem: ")
    data_envio = input("Data envio: ")
    lida = input("Lida? (s/n): ")
    criado_em = input("Criado em: ")
    notif = {
        "id_notif": id_notif,
        "id_usuario": id_usuario,
        "mensagem": mensagem,
        "data_envio": data_envio,
        "lida": lida,
        "criado_em": criado_em
    }
    return notif

def mostrar_notificacao(n):
    print("Notificação:", n["id_notif"])
    print(" Usuário:", n["id_usuario"])
    print(" Mensagem:", n["mensagem"])
