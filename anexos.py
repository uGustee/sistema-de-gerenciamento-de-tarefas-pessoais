def cadastrar_anexo():
    id_anexo = input("ID anexo: ")
    id_tarefa = input("ID tarefa: ")
    nome_arquivo = input("Nome arquivo: ")
    url = input("URL: ")
    data_upload = input("Data upload: ")
    criado_em = input("Criado em: ")
    anexo = {
        "id_anexo": id_anexo,
        "id_tarefa": id_tarefa,
        "nome_arquivo": nome_arquivo,
        "url": url,
        "data_upload": data_upload,
        "criado_em": criado_em
    }
    return anexo

def mostrar_anexo(a):
    print("Anexo:", a["id_anexo"])
    print(" Arquivo:", a["nome_arquivo"])
