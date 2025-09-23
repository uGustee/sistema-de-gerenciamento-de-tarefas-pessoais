def cadastrar_config():
    id_config = input("ID configuração: ")
    id_usuario = input("ID usuário: ")
    tema = input("Tema: ")
    notificacoes = input("Notificações ligadas? (s/n): ")
    idioma = input("Idioma: ")
    criado_em = input("Criado em: ")
    config = {
        "id_config": id_config,
        "id_usuario": id_usuario,
        "tema": tema,
        "notificacoes": notificacoes,
        "idioma": idioma,
        "criado_em": criado_em
    }
    return config

def mostrar_config(c):
    print("Configuração:", c["id_config"])
    print(" Usuário:", c["id_usuario"])
    print(" Tema:", c["tema"])
