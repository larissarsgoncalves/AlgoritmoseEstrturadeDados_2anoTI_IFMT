lista = []
sair = "nao"

while sair == "nao":
    print("deseja adicionar um item na lita?")
    resposta1 = input("sim ou nao")
    if resposta1 == "sim":
        item = input("digite o nome do item a ser adionado")
        lista.append(item)
        print("lista atual:", lista)
    else:
        print("deseja excluir um item da lista?")
        resposta2 = input("sim ou nao:")
        if resposta2 == "sim":
            item = input("digite o nome do item a ser removido:")
            if item in lista:
                lista.remove(item)
                print("lista atual:", lista)
            else:
                print("item não encontrado")
        else:
            print("deseja finalizar?")
            sair = input("sim ou nao:")
print("programa finalizado. lista final:", lista)
            
    