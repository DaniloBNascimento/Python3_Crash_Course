#!/usr/bin/env python3.8

# Código python criado para modelar uma classe de obejtos referente a um restaurante

class Restaurante():
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def description(self):
        print("Esse restaurante tem a cozinha do tipo: " + self.type.title())
    def open(self):
        print("O restaurante " + self.name + " está aberto!")

restaurant1 = Restaurante('cantina', 'italiano')
restaurant1.description()
restaurant1.open()

restaurant2 = Restaurante('bahia', 'brasileiro')
restaurant2.description()
restaurant2.open()