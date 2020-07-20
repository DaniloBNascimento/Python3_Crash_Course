#!/usr/bin/env python3.8

# Código python para treinamento de escrita de classes
# O código instância usuários e exibe uma saudação aos mesmos

class User():
    def __init__(self, name, lastname, endereco, telefone):
        self.name = name
        self.name = lastname
        self.endereco = endereco
        self.telefone = telefone
    def describe_user(self):
        print("Olá usuário " + self.name + " seja bem vindo!")
        print("O endereço cadastrado para você é o: " + self.endereco)
        print("Esse é o número de telefone: " + self.telefone)

usuario_one = User('Danilo', 'Bastos', 'Rua 160', '79999522415')
usuario_two = User('Rosy', 'Nascimento', 'Rua 161', '79991046230')

usuario_one.describe_user()
print("")
usuario_two.describe_user()

