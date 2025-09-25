nome = input("Digite o nome do usuário: ")

cpf = input("Digite o CPF do usuário (apenas números): ")
cpf = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]

telefone = input("Digite o telefone do usuário (apenas números): ")
telefone = "(" + telefone[:2] + ")" + telefone[2:7] + "-" + telefone[7:]

email = input("Digite o e-mail do usuário: ")
