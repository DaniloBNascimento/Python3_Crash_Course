#!/usr/bin/env python3.8
# Código python criado para demonstar a remoção de instancias em uma lista

# lista:
animais = ['cachorro', 'cachorro', 'gato', 'urso', 'cachorro', 'leão']

# Mostrando a lista original
print(animais)
print("Quantidade itens na lista original " + str(len(animais)))
# Removendo as instancias cachorro da lista
while 'cachorro' in animais:
    animais.remove('cachorro')

# Exibindo a lista alterada
print(animais)
print("Quantidade itens na lista alterada " + str(len(animais)))