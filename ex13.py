nome = input("coloque o nome do aluno") #aqui a variavel nome esta recebendo o input que é o valor que o usuario vai digitar
idade = int(input("coloque sua idade")) #se o input que é o valor que o usuario vai digitar não for texto precisa declarar o tipo da variavel nesse caso é um numero inteiro
turma = input("qual turma pertence")

if idade>=6: #esse linha significa: se a idade for maior ou igual a 6 anos
              print(f"Aluno cadastrado com sucesso {nome}, {idade} anos, turma {turma}") #esse f que aparece antes das aspas é para juntar texto e variavel, o texto fica escrito em rosa e a variavel esta entre colchetes
else: #isso significa senão, ele não pode ter condição na frente se precisar incluir uma condição usar o comando elif
              print("A criança ainda não tem idade suficiente para estudar conosco")