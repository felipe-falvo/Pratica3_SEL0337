# SEL0337 — Projetos em Sistemas Embarcados
## Prática 3: Introdução à programação de alto nível com GPIO (Checkpoint 1)

**Integrantes:**
- Felipe Assis Bernardes Falvo — Nº USP: 15004433
- Kayke Malaquias Gregorio — Nº USP: 15651561

---

Esse diretório tem a resolução do **Checkpoint 1**, envolvendo a configuração do ambiente virtual (`venv`) e o desenvolvimento de dois sistemas utilizando a biblioteca `RPi.GPIO`: um acionador de LED com botão, utilizando detecção de eventos e resistor de Pull-Up, e um temporizador regressivo.

---

## 1. Configuração do Ambiente Virtual (venv)

O projeto foi desenvolvido dentro de um ambiente virtual para evitar conflitos com os pacotes instalados no sistema operacional. O ambiente foi criado utilizando os dígitos finais do NUSP (`3361`), no qual foram instaladas as bibliotecas `gpiozero` e `RPi.GPIO`.

**Comandos utilizados:**

```bash
sudo apt install python3-venv -y
python3 -m venv 3361
source 3361/bin/activate

pip3 install gpiozero
pip3 install RPi.GPIO
```

## 2. Acionamento de LED com Botão (`botao.py`)

A ideia dessa etapa foi acender um LED ao pressionar um botão e apagá-lo ao soltar.

### Características

- **Resistor de Pull-Up Interno:** O pino de entrada (GPIO 17) foi configurado com `pull_up_down=GPIO.PUD_UP`. Isso mantém o sinal em nível alto (`HIGH`) por padrão. Ao pressionar o botão, o circuito é conectado ao GND, alterando o estado do pino para nível baixo (`LOW`).

- **Detecção de Eventos:** Foi utilizada a função `GPIO.add_event_detect` para detectar as mudanças de estado do botão. A detecção foi configurada para ambas as bordas (`GPIO.BOTH`), fazendo com que a função de *callback* `estado_led` seja acionada assim que o estado do botão mudar.

- **Tratamento de Saída (CTRL+C):** Foi utilizado `try/except KeyboardInterrupt` para permitir o encerramento do programa através do comando `CTRL+C`. Antes de finalizar a execução, a função `GPIO.cleanup()` é chamada para limpar as configurações dos pinos GPIO utilizados.

### Trecho da lógica

```python
def estado_led(canal):

    # em configuração Pull-Up, o botão pressionado é ligado ao GND
    if GPIO.input(pino_botao) == GPIO.LOW:
        GPIO.output(pino_LED, GPIO.HIGH) # liga quando botão apertado
    else:
        GPIO.output(pino_LED, GPIO.LOW) # desligado quando botão não apertado

# detecção para saber quando o botão foi ou não apertado
GPIO.add_event_detect(pino_botao, GPIO.BOTH, callback=estado_led)

# programa para quando apertar CTRL+C
try:
    print("Aperte CTRL+C para desligar")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
```

## 3. Contagem Regressiva e Acionamento de LED (`contagem_regressiva.py`)

A ideia dessa etapa foi implementar um cronômetro regressivo definido pelo usuário através do terminal. Durante a contagem, o tempo restante é atualizado na tela e, ao final, um LED conectado à protoboard é acionado.

### Características

- **Tratamento de Exceções (`try/except`):** O código verifica se o valor pode ser convertido para um número inteiro. Caso sejam inseridos caracteres ou valores que não correspondam a um número inteiro, uma mensagem de erro é mostrada e uma nova entrada é solicitada, sem interromper a execução do programa.

- **Type Casting e Validação Lógica:** A entrada recebida pelo terminal é convertida para o tipo inteiro utilizando `int()`. Em seguida, a condição `if tempo > 0` verifica se o valor fornecido é positivo, impedindo que valores negativos ou nulos sejam utilizados como tempo de contagem.

- **Formatação do Tempo (`MM:SS`):** A função `divmod()` é utilizada para separar o tempo restante em minutos e segundos. A exibição é atualizada na mesma linha do terminal utilizando `end='\r'`, evitando a impressão de uma nova linha a cada segundo.

- **Controle do Hardware:** O LED foi conectado ao **GPIO 18**. Ao término da contagem, o pino é colocado em nível lógico alto (`GPIO.HIGH`), acionando o LED. Ao final, o comando `GPIO.cleanup()` limpa as configurações utilizados.

### Trecho da lógica aplicada

```python
# função modularizada
def contagem_LED(tempo):
    tempo_resto = tempo
    
    # While da contagem regressiva:
    while tempo_resto >= 0:
        # Separa o tempo em minuto e segundo
        minuto, segundo = divmod(tempo_resto, 60) 
        
        # formatado MM:SS e atualiza na mesma linha (end='\r')
        print('{:02d}:{:02d}'.format(minuto, segundo), end='\r')
        
        # espera de 1 segundo
        if tempo_resto > 0:
            time.sleep(1)
            
        tempo_resto = tempo_resto - 1
        
    # coloca o GPIO em nível lógico alto e acende o LED
    GPIO.output(pino_LED, GPIO.HIGH)
    print("\nContagem terminou")
    print("Led aceso\n")

# tratamento de exceções (try/except)
try:
    # Lógica para receber a entrada do usuário
    while True:
        entrada = input("Coloque o tempo (segundos) para contar: ")
        try:
            # type casting para converter a string de entrada para número inteiro
            tempo = int(entrada)
            
            # aceitar apenas números positivos
            if tempo > 0:
                contagem_LED(tempo)
                break
            else:
                print("Erro, pois numero deve ser positivo")
                
        except ValueError:
            # erro caso seja usado letras
            print("Erro, pois o valor deve ser um numero inteiro")
            
finally:
    # Apertar ENTER para poder desligar o LED
    input("Aperte enter para desligar: ")
    # limpa as configurações do hardware
    GPIO.cleanup()

```

## 4. Estrutura dos diretórios

Os arquivos utilizados durante a prática estão organizados nos diretórios correspondentes. Além dos códigos-fonte, foram registrados imagens e vídeos para documentar tanto a configuração do ambiente quanto a execução dos sistemas desenvolvidos.

### 📄 Códigos e Registros

- **`contagem_regressiva.py`**: Código responsável pela implementação do temporizador regressivo e pelo acionamento do LED ao final da contagem.
- **`botao.py`**: Código do acionamento do LED através do botão, utilizando detecção de eventos.
- **`historico_contagem_14_08.txt`**: Histórico da primeira parte da prática dos comandos utilizados no terminal durante a criação do ambiente virtual `venv 3361` e a instalação das bibliotecas necessárias.
- **`historico_completo.txt`**: Registro do histórico de comandos executados no terminal durante os dois dias da prática (14/09/26 e 21/09/26). O arquivo comprova desde a criação do ambiente virtual `venv 3361` e a execução inicial da contagem regressiva, até os comandos do segundo dia, em que o ambiente foi reativado (`source 3361/bin/activate`), a pasta foi acessada (`cd 3361/`) e o programa do botão foi testado (`python3 botao.py`).

### 📸 Imagens

- **`codigo_thonny.jpeg`**: Interface da IDE Thonny no Raspberry Pi, demonstrando o desenvolvimento dos códigos no sistema embarcado.
- **`execucao_tratamento_erros.jpeg`**: Demonstração do tratamento de entradas inválidas utilizando `try/except`.
- **`erro_pip_sistema.jpeg`**: Registro do erro `externally-managed-environment` apresentado pelo sistema ao tentar instalar pacotes Python.
- **`pip_freeze_sistema.jpeg`** e **`historico_comandos_venv.jpeg`**: Registros utilizados para comparar os pacotes disponíveis no sistema com o ambiente virtual criado especificamente para a prática.

### 🔌 Evidências Físicas de Hardware

- **`montagem_circuito_led.jpeg`**: Montagem do circuito contendo o LED e o resistor de limitação conectado ao GPIO 18.
- **`circuito.jpeg`**: Montagem do circuito, incluindo o botão conectado ao GPIO 17 e ao GND da Raspberry Pi.
- **`video_prova.mp4`**: Demonstração do acionamento do LED através da detecção de eventos do botão, acompanhando o acionamento e a liberação do botão.
- **`contagem_regressiva.mp4`**: Demonstração do funcionamento do temporizador regressivo, incluindo a atualização do tempo no terminal e o acionamento do LED ao final da contagem.
