#!/usr/bin/env python3.8
# Código criado para demonstrar a usabilidade do uso de flags

flag = True

while flag == True:
    value = input("Entre com o código desejado: ")
    if value == 'quit':
        flag = False
        print("Saindo do programa!")
    else:
        print(value)
