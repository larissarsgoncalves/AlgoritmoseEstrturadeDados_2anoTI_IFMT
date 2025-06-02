# a= 25
# # b=2**3
# # print(type(a))
# # a=float(a)
# # print(type(a))
# idade=input("escreva um numero")
# if idade> 17:
#     print("voce tem mais de 18 anos")
# else:
#     print("voce tem menos de 18 anos")

# login=(input("escreva login"))
# senha=int(input("escreva senha"))
# if login=="adm"and senha==123:
#     print("acesso liberado")
# # elif login!="adm" and senha!=123:
# #     print("acesso negado")
# # else:
# #     print("senha e login invalido")
    
# # Solicita ao usuário um número inteiro
# numero = int(input("Digite qual tabuada você deseja saber: "))

# # Cria uma lista para armazenar os resultados da tabuada
# tabuada = []

# # Preenche a lista com os resultados usando um laço for
# for i in range(1, 11):
#     tabuada.append(numero * i)

# # Exibe os valores armazenados na lista
# print(f"Tabuada do {numero}:")
# for i, resultado in enumerate(tabuada, start=1):
#     print(f"{numero} x {i} = {resultado}")

# # Solicita ao usuário um número inteiro
# numero = int(input("Digite um número inteiro: "))

# # Cria uma lista para armazenar os resultados da tabuada
# tabuada = []

# # Preenche a lista com os resultados usando um laço for
# for i in range(1, 11):
#     tabuada.append(numero * i)

# # Exibe os valores armazenados na lista sem enumerate
# print(f"Tabuada do {numero}:")
# i = 1  # Inicializa o contador manual
# for resultado in tabuada:
#     print(f"{numero} x {i} = {resultado}")
#     i += 1  # Incrementa o contador manual
    
    
numero = int(input("Digite um número inteiro: "))
tabuada = []

for i in range(1, 11):
    tabuada.append(numero * i)

print(f"Tabuada do {numero}:")
i = 1 
for resultado in tabuada:
    print(f"{numero} x {i} = {resultado}")
    i += 1  
