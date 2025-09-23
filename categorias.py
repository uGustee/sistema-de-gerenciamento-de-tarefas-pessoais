def cadastrar_categoria():
    id_categoria = input("ID categoria: ")
    nome = input("Nome da categoria: ")
    descricao = input("Descrição: ")
    cor = input("Cor: ")
    criada_em = input("Criada em: ")
    categoria = {
        "id_categoria": id_categoria,
        "nome": nome,
        "descricao": descricao,
        "cor": cor,
        "criada_em": criada_em
    }
    return categoria

def mostrar_categoria(c):
