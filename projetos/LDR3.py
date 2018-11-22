from gpiozero import LightSensor, PWMLED
from signal import pause

sensor = LightSensor(23)
led = PWMLED(15)


led.source = sensor.values


pause()
