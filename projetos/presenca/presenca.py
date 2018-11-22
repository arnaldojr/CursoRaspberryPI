from picamera import PiCamera
from time import sleep
from gpiozero import MotionSensor
import datetime
from signal import pause

pir = MotionSensor(4)
camera = PiCamera()

def capture():
    camera.start_preview()
    sleep(3)
    camera.capture("/home/pi/Desktop/meu espaço programas/projetos/presenca/fotos/" + datetime.datetime.now().strftime("%Y_%m_%d_H:%M:%S")+".jpg")
    camera.stop_preview()

pir.when_motion = capture

pause()


