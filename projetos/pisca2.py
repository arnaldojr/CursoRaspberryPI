from gpiozero import LED
from time import sleep
from signal import pause


vermelho = LED(24)

vermelho.blink(1, 1)
pause()
