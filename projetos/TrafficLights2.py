from gpiozero import TrafficLights
from time import sleep

semaforo1 = TrafficLights(2, 3, 4) #red, yellow, green
semaforo2 = TrafficLights(17, 27, 22)

def cond1(): #semaro1=verde; s2=vml
    semaforo1.green.on()
    semaforo1.amber.off()
    semaforo1.red.off()

    semaforo2.green.off()
    semaforo2.amber.off()
    semaforo2.red.on()

def cond2(): #semaro1 amarelo; s2=vml
    semaforo1.green.off()
    semaforo1.amber.on()
    semaforo1.red.off()

    semaforo2.green.off()
    semaforo2.amber.off()
    semaforo2.red.on()
    
def cond3(): #semaro1 vermelho; s2=verde
    semaforo1.green.off()
    semaforo1.amber.off()
    semaforo1.red.on()

    semaforo2.green.on()
    semaforo2.amber.off()
    semaforo2.red.off()

def cond4(): #semaro1 vermelho; s2=aml
    semaforo1.green.off()
    semaforo1.amber.off()
    semaforo1.red.on()

    semaforo2.green.off()
    semaforo2.amber.on()
    semaforo2.red.off()


while True:
    cond1()
    sleep(10)
    cond2()
    sleep(1)
    cond3()
    sleep(10)
    cond4()
    sleep(1)
