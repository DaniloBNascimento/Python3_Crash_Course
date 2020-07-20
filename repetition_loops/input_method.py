#!/usr/bin/env python3.8

# Código de exemplo para entrada de dados
prompt = "\nPersonalize suas entradas de dados em python"
prompt += "\nQual o seu nome?"
name = input(prompt)

# Exemplo de um simples laço while
count = 1
while count <= 5:
    print(count)
    count += 1

# Exemplo de um laço while esperando por uma interação do usuário
prompt = "Programa escrito em python 3.8"
prompt += "\nEnter 'quit' para sair do programa"
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
print("Fim do programa!")