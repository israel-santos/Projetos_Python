import os
os.system('cls' if os.name == 'nt' else 'clear')
print("Bem vindo a calculadora")
print("0 : Soma")
print("1 : Subtração")
print("2 : Multiplicação")
print("3 : Divisão")
print("4 : Exponenciação")
print("\n")


while True:
    operacao = int(input("Escolha a operação que deseja realizar: "))
    print("\n")
    
    if operacao == 0:
        print("Operação escolhida Soma ")
        N1 = float(input("Qual o primeiro valor? "))
        N2 = float(input("Qual o segundo valor? "))
        soma = N1 + N2
        print("\n")
        print("{} + {} = {}".format(N1, N2, soma))
    elif operacao == 1:
        print("Operação escolhida Subtração ")
        N1 = float(input("Qual o primeiro valor? "))
        N2 = float(input("Qual o segundo valor? "))
        sub = N1 - N2
        print("\n")
        print("{} - {} = {}".format(N1, N2, sub))
    elif operacao == 2:
        print("Operação escolhida Multiplicação ")
        N1 = float(input("Qual o primeiro valor? "))
        N2 = float(input("Qual o segundo valor? "))
        multi = N1 * N2
        print("\n")
        print("{} * {} = {}".format(N1, N2, multi))
    elif operacao == 3:
        print("Operação escolhida Divisão")
        N1 = float(input("Qual o primeiro valor? "))
        N2 = float(input("Qual o segundo valor? "))
        div = N1 / N2
        print("\n")
        print("{} / {} = {}".format(N1, N2, div))
    elif operacao == 4:
        print("Operação escolhida Exponenciação")
        N1 = float(input("Qual o primeiro valor? "))
        N2 = float(input("Qual o segundo valor? "))
        expo = N1 ** N2
        print("\n")
        print("{} ^ {} = {}".format(N1, N2, expo))
    
    else:
        print("Digite uma operação válida!")
    print("\n")
    continuar = int(input('DESEJA FAZER OUTRA OPERAÇÃO? 0 - SIM, 1 - NÃO: '))
    if continuar == 1:
        break
