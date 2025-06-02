def cifra_de_cesar_tradicional(texto, deslocamento):  
    # Define a função que recebe um texto e um número de deslocamento para cifrar a mensagem.
    
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Criamos uma string contendo todas as letras do alfabeto (maiúsculas e minúsculas).
    
    resultado = ""  
    # Inicializamos uma variável para armazenar o texto cifrado.

    for char in texto:  
        # Percorremos cada caractere na string fornecida.

        if char in alfabeto:  
            # Verificamos se o caractere atual está dentro do alfabeto definido.

            indice_atual = alfabeto.index(char)  
            # Encontramos a posição do caractere dentro da string alfabeto.

            novo_indice = (indice_atual + deslocamento) % len(alfabeto)  
            # Calculamos a nova posição aplicando o deslocamento e usamos o operador "%" 
            # para garantir que o índice não ultrapasse o tamanho do alfabeto.

            resultado += alfabeto[novo_indice]  
            # Adicionamos o caractere cifrado ao resultado.

        else:  
            resultado += char  
            # Se o caractere não estiver no alfabeto (como números ou símbolos), ele é mantido inalterado.

    return resultado  
    # Retornamos a string final contendo o texto cifrado.


def decifra_de_cesar_tradicional(texto_cifrado, deslocamento):  
    # Função para decifrar um texto cifrado aplicando o deslocamento inverso.
    
    return cifra_de_cesar_tradicional(texto_cifrado, -deslocamento)  
    # Chamamos a função de cifragem, mas com deslocamento negativo para inverter o efeito da cifra.


# Testando a função
mensagem = "Programacao web eh top"  
# Definimos um texto de exemplo para ser cifrado.

deslocamento = 6
# Definimos um deslocamento de 3 posições.

mensagem_cifrada = cifra_de_cesar_tradicional(mensagem, deslocamento)  
# Chamamos a função para cifrar a mensagem.

print("Cifrada:", mensagem_cifrada)  
# Exibimos o resultado da cifra.

mensagem_decifrada = decifra_de_cesar_tradicional(mensagem_cifrada, deslocamento)  
# Chamamos a função para decifrar a mensagem cifrada.

print("Decifrada:", mensagem_decifrada)  
# Exibimos o resultado da decifração.