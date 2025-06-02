def calculate_imc(pessoa):
    imc = pessoa["peso"] / (pessoa["altura"] * pessoa["altura"])
    resultado = f"O IMC de {pessoa['nome']} é {imc:.2f}"
    saudavel = 18.5 < imc < 25  # Condição para um IMC saudável

    return {
        "nome": pessoa["nome"],
        "imc": imc,
        "resultado": resultado,
        "saudavel": saudavel
    }

# Definição do objeto pessoa como um dicionário
pessoa1 = {
    "nome": "João",
    "peso": 70,
    "altura": 1.75
}

# Chamando a função e imprimindo o resultado
print(calculate_imc(pessoa1))