#!/usr/bin/env python3.8

# Utilizando vários ifs no laço while

msg = "Informe a idade para que possamos informar o preço: "
while True:
    value = input(msg)
    value = int(value)
    if value < 3:
        print("Você não paga a entrada! :)")
    elif value <= 12:
        print(" O ingresso custa 10 dólares!")
    else:
        print("O ingresso custa 15 doláres!")
