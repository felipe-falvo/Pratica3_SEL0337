# SEL0337 — Projetos em Sistemas Embarcados
## Prática 3: Introdução à programação de alto nível com GPIO (Checkpoint 1)

**Integrantes:**
- Felipe Assis Bernardes Falvo — Nº USP: 15004433
- Kayke Malaquias Gregorio — Nº USP: 15651561
- 
**Local:** EESC-USP, São Carlos - SP  

Esse repositório documenta a Prática 3 da disciplina SEL0337. O roteiro dessa prática é dividido em três Checkpoints.

Nessa primeira parte, o grupo começou configurando o ambiente virtual e desenvolvendo o sistema de temporizador regressivo com acionamento de LED. Na próxima semana, o repositório será atualizado e completado com a primeira etapa do roteiro (acionamento de LED por botão com detecção de eventos e Pull-Up).

---
## 1. Configuração do Ambiente Virtual (venv)
O projeto foi desenvolvido dentro de um ambiente virtual. O ambiente foi criado utilizando os dígitos finais do NUSP (`3361`), permitindo a instalação das bibliotecas `gpiozero` e `RPi.GPIO` para o controle de hardware.

**Comandos utilizados na configuração:**
```
# Instalação, criação e ativação do ambiente virtual
sudo apt install python3-venv -y
python3 -m venv 3361
source 3361/bin/activate

# Instalação das bibliotecas isoladas
pip3 install gpiozero
pip3 install RPi.GPIO
```
---

## 2. Contagem Regressiva e Acionamento de LED (`contagem_regressiva.py`)
O script desenvolvido usa um cronômetro regressivo definido pelo usuário, que faz acionar um LED montado na protoboard. 

**Características:**
*   **Tratamento de Exceções (Try/Except):** O código valida a entrada do usuário, garantindo que o valor digitado seja numérico (`ValueError`). Se forem inseridos letras (ex: "abcde"), o sistema mostra a mensagem de erro e pede a entrada novamente.
*   **Type Casting e Validação Lógica:** A entrada é convertida utilizando `int()`, e uma estrutura condicional `if tempo > 0` impede a entrada de números negativos ou nulos.
*   **Formatação de Tempo (MM:SS):** A conversão do tempo para o formato de minutos e segundos foi feita utilizando a função `divmod`. A atualização ocorre na mesma linha do terminal utilizando o parâmetro `end='\r'`, fazendo com que a contagem fique sendo na mesma linha.
*   **Controle de Hardware:** Utilizou-se a biblioteca `RPi.GPIO` configurada no BCM (pino 18). Ao término da contagem, a porta é ativada (`GPIO.HIGH`) e o código é encerrado e limpando as configurações anteriores através do comando `GPIO.cleanup()` no bloco `finally`.

---

## 3. Estrutura de Diretórios e Fotos

Todos os arquivos gerados nessa primeira sessão colocado na pasta `contagem_regressiva (14_08_2026)`. Abaixo está a descrição de cada arquivo e imagem que comprovam a execução da prática:

### 📄 Códigos e Registros
*   **`contagem_regressiva.py`**: código do temporizador e modularizado
*   **`historico_contagem_14_08.txt`**: Registro em texto dos comandos executados no terminal Linux durante a aula, documentando a criação do ambiente e a execução do código.

### 📸 Imagens de Desenvolvimento e Execução
*   **`codigo_thonny.jpeg`**: Registro do desenvolvimento do script na IDE Thonny no Raspberry Pi.
*   **`execucao_tratamento_erros.jpeg`**: Prova do funcionamento do bloco `Try/Except`. Demonstra o sistema rejeitando uma entrada negativa (`-8`) e uma entrada em formato de texto (`abcde`), para então aceitar o valor correto (`5`).
*   **`inicio_limpando_historico.jpeg`**: Demonstra o ambiente de terminal no momento inicial da prática.

### 📸 Imagens de Configuração do Ambiente (venv)
*   **`erro_pip_sistema.jpeg`**: Documenta o erro `externally-managed-environment`, indicando a necessidade de usar um ambiente virtual.
*   **`pip_freeze_sistema.jpeg`**: Mostra a lista de pacotes instalados no SO, servindo de comparação com o ambiente criado.
*   **`historico_comandos_venv.jpeg`**: Prova a sequência de criação do ambiente virtual (`venv 3361`), ativação e instalação das bibliotecas `gpiozero` e `RPi.GPIO` com o `pip3`.

### 🔌 Hardware
*   **`montagem_circuito_led.jpeg`**: Montagem na protoboard, mostrando a conexão do LED e do resistor aos pinos GPIO da Raspberry Pi.
*   **`contagem_regressiva.mp4`**: Vídeo demonstrando a execução do sistema interagindo em tempo real, sendo desde a digitação do tempo no terminal, a contagem decrescente na mesma linha e o acendimento do LED no momento em que a contagem chega a zero.
