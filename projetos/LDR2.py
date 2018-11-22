from gpiozero import LightSensor, LED
from signal import pause


sensor = LightSensor(23)
led = LED(15)

sensor.when_light = led.off
sensor.when_dark = led.on

pause()
