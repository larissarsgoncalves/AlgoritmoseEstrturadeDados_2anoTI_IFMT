# # Lista para armazenar os livros
# biblioteca = [
#     {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "paginas": 96, "emprestado": False},
#     {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "paginas": 256, "emprestado": False},
#     {"titulo": "1984", "autor": "George Orwell", "paginas": 328, "emprestado": False}
# ]

# # Lista para armazenar os empréstimos
# emprestimos = []

# def mostrar_livros():
#     """Exibe todos os livros e seus status na biblioteca"""
#     for livro in biblioteca:
#         status = "Emprestado" if livro["emprestado"] else "Disponível"
#         print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]}, Páginas: {livro["paginas"]}, Status: {status}')

# def emprestar_livro(titulo, nome_leitor):
#     """Realiza o empréstimo de um livro para um leitor"""
#     for livro in biblioteca:
#         if livro["titulo"].lower() == titulo.lower() and not livro["emprestado"]:
#             livro["emprestado"] = True
#             emprestimos.append({"leitor": nome_leitor, "titulo": titulo, "dias_restantes": 15})
#             print(f'O livro "{titulo}" foi emprestado para {nome_leitor}.')
#             return
#     print("Livro não disponível para empréstimo.")

# def devolver_livro(titulo, nome_leitor, dias_atraso):
#     """Registra a devolução de um livro e aplica multa, se necessário"""
#     for livro in biblioteca:
#         if livro["titulo"].lower() == titulo.lower() and livro["emprestado"]:
#             livro["emprestado"] = False
#             emprestimos.remove({"leitor": nome_leitor, "titulo": titulo, "dias_restantes": 15})
#             if dias_atraso > 0:
#                 multa = dias_atraso * 2  # R$2 por dia de atraso
#                 print(f'Devolução atrasada! {nome_leitor} deve pagar R${multa:.2f} de multa.')
#             else:
#                 print(f'O livro "{titulo}" foi devolvido por {nome_leitor} sem atraso.')
#             return
#     print("Erro na devolução do livro.")

# # Testando as funções
# mostrar_livros()
# emprestar_livro("1984", "Larissa")
# devolver_livro("1984", "Larissa", 3)
# mostrar_livros()

# Lista para armazenar os livros
biblioteca = [
    {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "paginas": 96, "emprestado": False},
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "paginas": 256, "emprestado": False},
    {"titulo": "1984", "autor": "George Orwell", "paginas": 328, "emprestado": False}
]

# Lista para armazenar os empréstimos
emprestimos = []

def mostrar_livros():
    """Exibe todos os livros e seus status na biblioteca"""
    for livro in biblioteca:
        status = "Emprestado" if livro["emprestado"] else "Disponível"
        print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]}, Páginas: {livro["paginas"]}, Status: {status}')

def emprestar_livro():
    """Solicita ao usuário os dados do empréstimo"""
    titulo = input("Digite o título do livro que deseja emprestar: ")
    nome_leitor = input("Digite o seu nome: ")

    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower() and not livro["emprestado"]:
            livro["emprestado"] = True
            emprestimos.append({"leitor": nome_leitor, "titulo": titulo, "dias_restantes": 15})
            print(f'O livro "{titulo}" foi emprestado para {nome_leitor}.')
            return
    print("Livro não disponível para empréstimo.")

def devolver_livro():
    """Solicita ao usuário os dados da devolução"""
    titulo = input("Digite o título do livro que deseja devolver: ")
    nome_leitor = input("Digite o seu nome: ")
    dias_atraso = int(input("Quantos dias de atraso na devolução? (Digite 0 se não houver atraso): "))

    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower() and livro["emprestado"]:
            livro["emprestado"] = False
            emprestimos.remove({"leitor": nome_leitor, "titulo": titulo, "dias_restantes": 15})
            if dias_atraso > 0:
                multa = dias_atraso * 2  # R$2 por dia de atraso
                print(f'Devolução atrasada! {nome_leitor} deve pagar R${multa:.2f} de multa.')
            else:
                print(f'O livro "{titulo}" foi devolvido por {nome_leitor} sem atraso.')
            return
    print("Erro na devolução do livro.")

# Testando interativamente
while True:
    print("\nEscolha uma opção:")
    print("1 - Mostrar livros disponíveis")
    print("2 - Emprestar um livro")
    print("3 - Devolver um livro")
    print("4 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        mostrar_livros()
    elif opcao == "2":
        emprestar_livro()
    elif opcao == "3":
        devolver_livro()
    elif opcao == "4":
        print("Encerrando o sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
