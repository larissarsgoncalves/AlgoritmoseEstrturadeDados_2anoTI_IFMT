compras = []

while True:
    print("\n Escolha uma opção abaixo")
    print("\n 1 - Adicionar itens")
    print("\n 2 - Remover itens")
    print("\n 3 - Encerrar")
    
    opcao = input("Qual opção desejada?")
    if opcao =="1":
        item=input("Digite o item a ser adicionado")
        compras.append(item)
        print(f"lista de compras atual: \n {compras}")
    elif opcao =="2":
        item_a_remover=input("Digite o item a ser removido")
        if item_a_remover in compras:
            compras.remove(item_a_remover)
            print(f"lista de compras atual: \n {compras}")
        else:
            print("item não encontrado na lista")
        