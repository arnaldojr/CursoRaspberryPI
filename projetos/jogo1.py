from gpiozero import Button
from random import choice
from time import sleep

botao = Button(3)

while True:
    if botao.is_pressed:
        print("Faça a sua pergunta...")

        sleep(2)

        print("Estou pensando...")

        sleep(1)

        respostas = [
            "vou pensar no seu caso"
            "não sei responder"
            "Sim com certeza"

            ]
    
