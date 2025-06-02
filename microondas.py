import time

# Variáveis globais
ligado = False
tempo = 0
potencia = 0

def ligar(novo_tempo, nova_potencia):
    global ligado, tempo, potencia
    if not ligado:
        ligado = True
        tempo = novo_tempo
        potencia = nova_potencia
        print(f"Micro-ondas ligado por {tempo} segundos na potência {potencia}.")
        iniciar_cronometro(tempo)
        desligar()  # Desliga automaticamente ao fim do tempo
    else:
        print("O micro-ondas já está ligado!")

def desligar():
    global ligado
    if ligado:
        ligado = False
        print("Micro-ondas desligado.")
    else:
        print("O micro-ondas já está desligado.")

def status():
    if ligado:
        print(f"Micro-ondas está ligado: {tempo} segundos restantes na potência {potencia}.")
    else:
        print("Micro-ondas está desligado.")

def iniciar_cronometro(segundos):
    while segundos > 0:
        print(f"Tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos -= 1
    print("\nTempo esgotado!")

# Modos predefinidos
def pipoca():
    ligar(20, 8)

def descongelar():
    ligar(30, 4)

def arroz():
    ligar(6, 7)

# Testando
pipoca()
descongelar()
arroz()