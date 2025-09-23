from usuarios import cadastrar_usuario, mostrar_usuario
from tarefas import cadastrar_tarefa, mostrar_tarefa
from lembretes import cadastrar_lembrete, mostrar_lembrete

def main():
    print("=== Cadastro Usuário ===")
    u = cadastrar_usuario()
    print("\nDados cadastrados do usuário:")
    mostrar_usuario(u)

    print("\n=== Cadastro Tarefa ===")
    t = cadastrar_tarefa()
    print("\nDados da tarefa:")
    mostrar_tarefa(t)

    print("\n=== Cadastro Lembrete ===")
    l = cadastrar_lembrete()
    print("\nDados do lembrete:")
    mostrar_lembrete(l)

if __name__ == "__main__":
    main()
