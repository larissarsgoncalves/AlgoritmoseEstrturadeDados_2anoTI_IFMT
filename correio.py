# Tupla contendo os pacotes e seus respectivos status
pacotes = (
    ("ABC123", "Enviado"),
    ("XYZ789", "Recebido"),
    ("DEF456", "Em Trânsito"),
    ("JKL321", "Enviado"),
    ("MNO654", "Recebido"),
    ("PQR987", "Em Trânsito"),
    ("STU741", "Enviado"),
)

# 1. Contar quantos pacotes existem em cada status
status_contagem = {"Enviado": 0, "Recebido": 0, "Em Trânsito": 0}

for codigo, status in pacotes:
    status_contagem[status] += 1

print("Contagem de pacotes por status:")
print("Enviado:", status_contagem["Enviado"])
print("Recebido:", status_contagem["Recebido"])
print("Em Trânsito:", status_contagem["Em Trânsito"])

# 2. Listar apenas os códigos dos pacotes com status "Em Trânsito"
pacotes_transito = tuple(codigo for codigo, status in pacotes if status == "Em Trânsito")

print("\nPacotes em trânsito:", pacotes_transito)

# 3. Função para buscar o status de um pacote pelo código de rastreamento
def buscar_status(codigo_rastreamento, pacotes):
    for codigo, status in pacotes:
        if codigo == codigo_rastreamento:
            return f"O pacote {codigo_rastreamento} está '{status}'."
    return "Pacote não cadastrado."

# Teste da função
print("\nStatus do pacote 'DEF456':", buscar_status("DEF456", pacotes))
print("Status do pacote 'XYZ123':", buscar_status("XYZ123", pacotes))  # Código inexistente

# 4. Ordenar os pacotes pelo código de rastreamento
pacotes_ordenados = tuple(sorted(pacotes, key=lambda x: x[0]))

print("\nPacotes ordenados pelo código:")
for pacote in pacotes_ordenados:
    print(pacote)