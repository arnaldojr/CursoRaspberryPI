import RPi.GPIO as GPIO                         # Importa biblioteca RPi.GPIO
import time                                     # Importa biblioteca time
GPIO.setmode(GPIO.BCM)                          # Seta o tipo de numeração das GPIOs

TRIG = 23                                       # Associa a GPIO21 ao TRIG
ECHO = 24                                       # Associa a GPIO20 ao ECHO

print ("Medição de distância em progresso.")

GPIO.setup(TRIG, GPIO.OUT)                      # Seta pino como saída
GPIO.setup(ECHO, GPIO.IN)                       # Seta pino como entrada

while True:

    GPIO.output(TRIG, False)                    # Seta TRIG em nível baixo (LOW)
    print ("Aguardando sensor estabilizar...")
    time.sleep(2)                               # Delay de 2 segundos

    GPIO.output(TRIG, True)                     # Seta TRIG em nível alto (HIGH)
    time.sleep(0.00001)                         # Delay de 0.00001 segundos (10 micro segundos)
    GPIO.output(TRIG, False)                    # Seta TRIG em nível baixo (LOW)

    while GPIO.input(ECHO) == 0:                # Checa se o ECHO está em nível baixo (LOW)
        pulse_start = time.time()               # Armazena o último tempo em que ECHO se encontra em nível baixo (LOW)

    while GPIO.input(ECHO) == 1:                # Checa se o ECHO está em nível alto (HIGH)
        pulse_end = time.time()                 # Armazena o último tempo em que ECHO se encontra em nível alto (HIGH)

    pulse_duration = pulse_end - pulse_start    # Armazena a duração do pulso em uma variável

    distance = (pulse_duration * 34300)/2           # Multiplica a duração do pulso por 17150 para obter a distância
    distance = round(distance, 2)               # Arredonda número para duas casas decimais

    if distance > 2 and distance < 400:         # Checa se distância está dentro do alcance do sensor
        print ("Distância:", distance, "cm")    # Imprime a distância
    else:
        print ("Fora de alcance.")
