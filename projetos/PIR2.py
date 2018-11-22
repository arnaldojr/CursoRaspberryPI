from gpiozero import MotionSensor, LED
from signal import pause
from time import sleep


pir = MotionSensor(4)
led = LED(15)

led.off()

while True:
    print("lendo sensor...")
    pir.wait_for_motion()
    if pir.motion_detected:
        print("Detectado Movimento!")
        led.on()
    sleep(3)
    led.off()



