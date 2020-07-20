#!/usr/bin/env python3.8

# Código criado para modelar um cachorro através de uma classe

class Dog():
    """ Classe para modelar um cachorro """
    def __init__(self, name, age):
        """ Inicializa os métodos name e age """
        self.name = name
        self.age = age
    def sit(self):
        """ Simula um cachoro sentando em resposta a um comando """
        print(" O cachorro "+self.name.title() +" está sentando.")
    def roll_over(self):
        """ Simula um cachorro rolando em resposta a um comando """
        print(self.name.title() + " rolando!")

my_dog = Dog('Danilo', 25)

print ("Meu cachorro se chama " + my_dog.name + " e tem uma idade de " + str(my_dog.age))
print(" ")
acao = input("O que deseja que o cachorro faça? (sentar ou rolar)")

if acao == 'sentar':
    my_dog.sit()
elif acao == 'rolar':
    my_dog.roll_over()
else:
    print("Opção inválida!")

