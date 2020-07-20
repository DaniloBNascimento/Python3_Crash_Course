#!/usr/bin/env python3.8

# Exercicio do capitulo de laços de repetição com o while

msg = "Informe o ingrediente da pizza que deseja adicionar: "
ingredientes = []
while True:
    ingrediente = input(msg)
    if ingrediente == 'quit':
        print("Saindo do programa")
        break
    else:
        print(" ")
        print("Adicionando ingrediente " + ingrediente + " a lista")
        ingredientes.append(ingrediente)
        print(" ")
        print("Sua lista atual de ingredientes:")
        for list_ingrediente in ingredientes:
            print(list_ingrediente)
        print(" ")

