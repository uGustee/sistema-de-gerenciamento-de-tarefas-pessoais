nome = input("Digite o nome do usuário: ")

cpf = input("Digite o CPF do usuário (apenas números): ")
cpf = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]

telefone = input("Digite o telefone do usuário (apenas números): ")
telefone = "(" + telefone[:2] + ")" + telefone[2:7] + "-" + telefone[7:]

email = input("Digite o e-mail do usuário: ")

rua = input("Digite a rua: ")
numero = input("Digite o número: ")
bairro = input("Digite o bairro: ")
cidade = input("Digite a cidade: ")
estado = input("Digite o estado (sigla, ex: PR): ")

cep = input("Digite o CEP (apenas números): ")
cep = cep[:5] + "-" + cep[5:]
