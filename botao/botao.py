import RPi.GPIO as GPIO
import time

pino_LED = 18
pino_botao = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(pino_LED, GPIO.OUT)
# Configura o botão como entrada e ativa o resistor interno Pull-Up exigido
GPIO.setup(pino_botao, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(pino_LED, GPIO.LOW)

# Função de callback acionada pelos eventos do botão
def estado_led(canal):
    # Em configuração Pull-Up, o botão pressionado conecta ao GND (LOW)
    if GPIO.input(pino_botao) == GPIO.LOW:
        GPIO.output(pino_LED, GPIO.HIGH)
    else:
        GPIO.output(pino_LED, GPIO.LOW)

# Configura a detecção de eventos para borda de subida e descida (BOTH)
GPIO.add_event_detect(pino_botao, GPIO.BOTH, callback=estado_led)

# Tratamento de exceção para encerramento via teclado (CTRL+C)
try:
    print("Sistema ativo. Segure o botão para acender o LED.")
    print("Pressione CTRL+C no terminal para encerrar.")
    # Mantém o script rodando em segundo plano aguardando os eventos
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    # Captura o CTRL+C sem gerar erros vermelhos no terminal
    print("\nPrograma interrompido pelo usuário.")

finally:
    # Executa o cleanup obrigatoriamente, liberando as portas GPIO
    GPIO.cleanup()
