# Tuplas separadas com códigos de rastreamento e status dos pacotes
codigos = ("ABC123", "XYZ789", "DEF456", "JKL321", "MNO654", "PQR987", "STU741")
status = ("Enviado", "Recebido", "Em Trânsito", "Enviado", "Recebido", "Em Trânsito", "Enviado")

# 1. Contar quantos pacotes existem em cada status
print("Enviado:", status.count("Enviado"))
print("Recebido:", status.count("Recebido"))
print("Em Trânsito:", status.count("Em Trânsito"))

# 2. Listar apenas os códigos dos pacotes com status "Em Trânsito"
pacotes_transito = tuple(codigos[i] for i in range(len(status)) if status[i] == "Em Trânsito")
print("\nPacotes em trânsito:", pacotes_transito)

# 3. Função para buscar o status de um pacote pelo código de rastreamento
def buscar_status(codigo_rastreamento):
    if codigo_rastreamento in codigos:
        indice = codigos.index(codigo_rastreamento)
        return f"O pacote {codigo_rastreamento} está '{status[indice]}'."
    return "Pacote não cadastrado."

# Teste da função
print("\nStatus do pacote 'DEF456':", buscar_status("DEF456"))
print("Status do pacote 'XYZ123':", buscar_status("XYZ123"))  # Código inexistente

# 4. Ordenar os códigos de rastreamento e reorganizar os status de acordo
pacotes_ordenados = sorted(zip(codigos, status))  # Ordenando pares código-status
codigos_ordenados, status_ordenados = zip(*pacotes_ordenados)  # Convertendo de volta para tuplas separadas

print("\nCódigos ordenados:", codigos_ordenados)
print("Status ordenados:", status_ordenados)