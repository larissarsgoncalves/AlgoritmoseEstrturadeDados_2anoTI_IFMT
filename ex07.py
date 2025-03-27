numero1=int(input("insira 1º numero"))
numero2=int(input("insira 2º numero"))
operacao=input("insira operação que deseja realizar")
if operacao=="adição":
    soma=numero1+numero2
    print(f"resultado é:{soma}")
elif operacao=="subtração":
    sub=numero1-numero2
    print(f"resultado é:{sub}")
elif operacao=="multiplicação":
    mult=numero1*numero2
    print(f"resultado é:{mult}")
else:
    operacao=="divisão"
    div=numero1/numero2
    print(f"resultado é:{div}")
