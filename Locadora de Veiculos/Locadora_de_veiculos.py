#codigo feito com auxilio. NÃO FIZ SÓ!!! :)
import os

carros = [
    ("Chevrolet Tracker", 120),
    ("Chevrolet Onix", 90),
    ("Hyundai HB20", 85),
    ("Hyundai Tucson", 120),
    ("Fiat Uno", 60),
    ("Fiat Mobi", 70),
    ("Fiat Pulse", 130)
        ]

alugados = []

def mostrar_lista_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} / dia.".format(i, car[0], car[1]))



while  True:
    os.system("cls")
    print("-"*40)
    print("Bem vindo à Locadora de carros!")
    print("-"*40)
    print("O que deseja fazer?\n")
    print("0 - Mostrar Portifólio | 1 - Alugar um Carro | 2 - Devolver um carro")
    op = int(input())

    os.system("cls")
    if op == 0:
        mostrar_lista_carros(carros)

    elif op == 1:
        mostrar_lista_carros(carros)
        print("-"*40)
        print("Escolha o código do carro:")
        cod_car = int(input())
        print("Por quantos dias você deseja alugar este carro?")
        dias = int(input())
        os.system("cls")

        print("Você escolheu {} por {} dias.".format(carros[cod_car] [0], dias))
        print("")
        print("O aluguel está com o seguinte valor R$ {}. Deseja finalizar?".format(dias * carros[cod_car][1]))

        print("0 - SIM | 1 - NÃO")
        conf = int(input())
        os.system("cls")
        if conf == 0:
            print("Parabéns você alugou o {} por {} dias.".format(carros[cod_car][0], dias))
            alugados.append(carros.pop(cod_car))



    elif op == 2:
        if len(alugados) == 0:
            print("Não há carros para devolver")
        else:
            print("Segue a lista de carros alugados. Qual você deseja devolver?")
            mostrar_lista_carros(alugados)
            print("")
            print("Escolha o código do carro que deseja devolver")
            cod = int(input())
            if conf == 0:
                print("Obrigado por devolver o carro {}.".format(alugados[cod][0]))
                carros.append(alugados.pop(cod))

    print("")
    print("="*40)
    print("0 - CONTINUAR | 1 - SAIR")
    if int(input()) == 1:
        break