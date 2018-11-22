def hello():
    print("hello world")

def imprime_nome(nome):
    if not nome:
        print("vazio, por favor digite um nome.")
    else:
        print("olá "+nome)

def media(numero1, numero2):
    media = numero1+numero2
    media /=2
    print("média "+ str(media))

hello()
imprime_nome("")
imprime_nome("Arnaldo")
media(15, 20)
