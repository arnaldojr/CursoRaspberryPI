from gpiozero import LED, Button
from signal import pause


botao = Button(14)
vermelho = LED(15)

botao.when_pressed = vermelho.toggle
#botao.when_released = vermelho.off


pause()
