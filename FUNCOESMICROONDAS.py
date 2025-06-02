import time

#variaveis globais
ligado = False
tempo = 0
potencia = 0

def ligar(novo_tempo, nova_potencia):
    global ligado, tempo, potencia
    if not ligado:
        ligado = True
        tempo = novo_tempo
        potencia = nova_potencia
        print(f'Microondas ligador por {tempo} segundos na potência {potencia}')
        iniciar_cronometro(tempo)
        desligar() #desligar automaticamente
    else:
        print('O microoondas já esta ligado')
        
def desligar():
    global ligado
    if ligado:
        ligado = False
        print('Microondas está desligado')
    else:
        print('Microondas já esta desligado')
        
def status():
    if ligado:
        print(f'tempo: {tempo} segundos \n potência: {potencia}')
    else:
        print(f"desligado")

def iniciar_cronometro(segundos):
    while segundos>0:
        print(f"tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos -= 1 # segundos = segundos -1
    print("\n tempo esgotado")
    
#predefinoções do microondas

def pipoca():
    ligar(30, 100)
    
#rodar a função

pipoca()