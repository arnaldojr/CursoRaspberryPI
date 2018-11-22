from gpiozero import LED, Button


botao = Button(14, bounce_time =0.09)
vermelho = LED(15)

while True:
    if botao.is_pressed:
        vermelho.toggle()
    if vermelho.is_lit:
        print("ativo")
    else:
        print("apagado")

