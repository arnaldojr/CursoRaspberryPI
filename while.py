SENHA_PADRAO =  "senha"

while True:
    senha = input("digite sua senha: ")
    if not senha:
        continue
    elif senha == SENHA_PADRAO:
        break

    print("Senha incorreta!")

print("Bem vindo!")
