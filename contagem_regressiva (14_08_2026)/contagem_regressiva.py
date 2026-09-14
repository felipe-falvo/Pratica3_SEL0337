import RPi.GPIO as GPIO
import time

pino_LED = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pino_LED, GPIO.OUT)
GPIO.output(pino_LED, GPIO.LOW) # LED começa apagado

# função modularizada
def contagem_LED(tempo):
    tempo_resto = tempo
    
    # contagem:
    while tempo_resto >= 0:
        minuto, segundo = divmod(tempo_resto, 60) # Separa o tempo em minuto e segundo
        # formatado MM:SS e atualiza na mesma linha (end='\r')
        print('{:02d}:{:02d}'.format(minuto, segundo), end='\r')
        
        # espera de 1 segundo
        if tempo_resto > 0:
            time.sleep(1)
            
        tempo_resto = tempo_resto - 1
        
    # acende o LED
    GPIO.output(pino_LED, GPIO.HIGH)
    print("\nContagem terminou")
    print("Led aceso\n")

# tratamento de exceções (Try/Except)
try:
    while True:
        entrada = input("Coloque o tempo (segundos) para contar: ")
        try:
            # type casting para inteiro
            tempo = int(entrada)
            
            # aceitar apenas números positivos
            if tempo > 0:
                contagem_LED(tempo)
                break
            else:
                print("Erro, pois numero deve ser positivo")
                
        except ValueError:
            # erro caso seja usado letras ou símbolos
            print("Erro, pois o valor deve ser um numero inteiro")
            
finally:
    input("Aperte enter para desligar: ")
    GPIO.cleanup()
