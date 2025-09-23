from usuarios import cadastrar_usuario, mostrar_usuario
from tarefas import cadastrar_tarefa, mostrar_tarefa
from lembretes import cadastrar_lembrete, mostrar_lembrete
from categorias import cadastrar_categoria, mostrar_categoria
from projetos import cadastrar_projeto, mostrar_projeto
from comentarios import cadastrar_comentario, mostrar_comentario
from etiquetas import cadastrar_etiqueta, mostrar_etiqueta
from anexos import cadastrar_anexo, mostrar_anexo
from historico import cadastrar_historico, mostrar_historico
from notificacoes import cadastrar_notificacao, mostrar_notificacao
from configuracoes import cadastrar_config, mostrar_config
from permissoes import cadastrar_permissao, mostrar_permissao
from tags import cadastrar_tag, mostrar_tag

def main():
    print("=== Teste Usuário ===")
    u = cadastrar_usuario()
    mostrar_usuario(u)

    print("\n=== Teste Tarefa ===")
    t = cadastrar_tarefa()
    mostrar_tarefa(t)

    print("\n=== Teste Lembrete ===")
    l = cadastrar_lembrete()
    mostrar_lembrete(l)

    print("\n=== Teste Categoria ===")
    c = cadastrar_categoria()
    mostrar_categoria(c)

    print("\n=== Teste Projeto ===")
    p = cadastrar_projeto()
    mostrar_projeto(p)

    print("\n=== Teste Comentário ===")
    cm = cadastrar_comentario()
    mostrar_comentario(cm)

    print("\n=== Teste Etiqueta ===")
    e = cadastrar_etiqueta()
    mostrar_etiqueta(e)

    print("\n=== Teste Anexo ===")
    a = cadastrar_anexo()
    mostrar_anexo(a)

    print("\n=== Teste Histórico ===")
    h = cadastrar_historico()
    mostrar_historico(h)

    print("\n=== Teste Notificação ===")
    n = cadastrar_notificacao()
    mostrar_notificacao(n)

    print("\n=== Teste Configuração ===")
    cf = cadastrar_config()
    mostrar_config(cf)

    print("\n=== Teste Permissão ===")
    pm = cadastrar_permissao()
    mostrar_permissao(pm)

    print("\n=== Teste Tag ===")
    tg = cadastrar_tag()
    mostrar_tag(tg)

if __name__ == "__main__":
    main()
