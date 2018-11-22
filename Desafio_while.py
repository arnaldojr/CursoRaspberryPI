from random import randrange

NUMERO_SORTE =  randrange(10)

while True:
    numero = int(input("digite um numero: "))
    if not numero:
        continue
    elif numero == NUMERO_SORTE:
        break
    elif numero > NUMERO_SORTE:
        print("Menos")
    else:
        print("Mais")

print("Parabens")
