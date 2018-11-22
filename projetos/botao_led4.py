from gpiozero import LED, Button
from time import sleep

def pisca():
    print("botao segurado por 2 segundos")
    vermelho.toggle()

    
botao = Button(14, bounce_time = 0.09, hold_time = 2)
vermelho = LED(15)

botao.when_held = pisca


    
