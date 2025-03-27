Saldo=input("Insira o saldo")
conta=True
if Saldo==0:
    conta=False
    print("Conta desativada")
elif Saldo<0:
    print("Negociar divida")
else:
    conta=True
    print("Tem um bom saldo")