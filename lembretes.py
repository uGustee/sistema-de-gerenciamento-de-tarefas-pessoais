def cadastrar_lembrete():
    id_lembrete = input("ID lembrete: ")
    id_tarefa = input("ID tarefa: ")
    data_lembrete = input("Data do lembrete: ")
    repetir_input = input("Repetir lembrete? (s/n): ")
    repetir = True if repetir_input.lower() == "s" else False
    enviado_input = input("Já enviado? (s/n): ")
    enviado = True if enviado_input.lower() == "s" else False
    criado_em = input("Criado em: ")

    lembrete = {
        "id_lembrete": id_lembrete,
        "id_tarefa": id_tarefa,
        "data_lembrete": data_lembrete,
        "repetir": repetir,
        "enviado": enviado,
        "criado_em": criado_em
    }
    return lembrete

def mostrar_lembrete(l):
    print("Lembrete:", l["id_lembrete"])
    print(" Tarefa:", l["id_tarefa"])
    print(" Data:", l["data_lembrete"])
    print(" Repetir?:", l["repetir"])
    print(" Enviado?:", l["enviado"])
