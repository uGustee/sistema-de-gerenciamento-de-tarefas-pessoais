def formatar_telefone(telefone):
    return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"

def formatar_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

id_usuario = input("Digite o ID do usuário: ")
nome = input("Digite o nome: ")
email = input("Digite o email: ")
senha = input("Digite a senha: ")
cpf = input("Digite o CPF (somente números, ex: 12345678900): ")
telefone = input("Digite o telefone (somente números com DDD, ex: 41999999999): ")

print("\n--- Dados do Usuário ---")
print("ID:", id_usuario)
print("Nome:", nome)
print("Email:", email)
print("CPF:", formatar_cpf(cpf))
print("Telefone:", formatar_telefone(telefone))
