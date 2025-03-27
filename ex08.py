login=(input("escreva login"))
senha=int(input("escreva senha"))
if login=="adm"and senha==123:
    print("acesso liberado")
elif login!="adm" and senha!=123:
    print("acesso negado")
else:
    print("senha e login invaldo")
