def cadastrar_etiqueta():
    id_etiqueta = input("ID etiqueta: ")
    nome = input("Nome: ")
    cor = input("Cor: ")
    criada_em = input("Criada em: ")
    etiqueta = {
        "id_etiqueta": id_etiqueta,
        "nome": nome,
        "cor": cor,
        "criada_em": criada_em
    }
    return etiqueta

def mostrar_etiqueta(e):
    print("Etiqueta:", e["id_etiqueta"])
    print(" Nome:", e["nome"])
