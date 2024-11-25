#codigo feito com auxilio
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

mostrar_lista_carros(carros)

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
        pass

    elif op == 1:
        pass

    elif op == 2:
        pass

    print("")
    print("="*40)
    print("0 - CONTINUAR | 1 - SAIR")
    if int(input()) == 1:
        break