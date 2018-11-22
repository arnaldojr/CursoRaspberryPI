from gpiozero import LED
from time import sleep

vermelho = LED(24)

while True:
    vermelho.on()
    sleep(1)
    print("led aceso")
    vermelho.off()
    sleep(1)
    print("led apagado")
