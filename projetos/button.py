from gpiozero import Button
from signal import pause


botao = Button(14)

botao.wait_for_press()
print("botao ativado")
pause()
