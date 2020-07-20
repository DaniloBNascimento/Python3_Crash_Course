#!/usr/bin/env python3.8

# Código de exemplo para demonstar uma instrução break em um laço while

msg = "Entre com o código desejado: "
while True:
    code = input(msg)
    if code == 'quit':
        break
    else:
        print("O código digitado foi: "+str(code))


