from gpiozero import Button, LED, Buzzer
from signal import pause

def BuzzerOn():
    buzzer.beep(1,1)
    led.on()

def BuzzerOff():
    buzzer.off()
    led.off()

buzzer = Buzzer(18)
botao = Button(14)
led = LED(15)

botao.when_pressed = BuzzerOn
botao.when_released = BuzzerOff

pause()
