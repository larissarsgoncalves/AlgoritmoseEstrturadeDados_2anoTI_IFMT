email=input("Insira seu email")
email=str.lower(email)
senha=input("insira uma senha de oito letras")
if len(senha)>=8:
    print("Login efetuado")
    l=(input("digite seu email"))
    senha2=(input("digite sua senha"))
    if l==email and senha==senha:
        print("login efetuado")
    else:
        print("login ou senha errado")

else:
    print("senha muito pequena")