import pygame
from gpiozero import Button

pygame.init()

btn_1 = Button(2)
btn_2 = Button(3)
btn_3 = Button(27)
btn_4 = Button(22)

som_1 = pygame.mixer.Sound("caixa-musica/samples/ambi_drone.wav")
som_2 = pygame.mixer.Sound("caixa-musica/samples/bass_dnb_f.wav")
som_3 = pygame.mixer.Sound("caixa-musica/samples/bass_thick_c.wav")
som_4 = pygame.mixer.Sound("caixa-musica/samples/drum_splash_soft.wav")


btn_1.when_pressed = som_1.play
btn_2.when_pressed = som_2.play
btn_3.when_pressed = som_3.play
btn_4.when_pressed = som_4.play
