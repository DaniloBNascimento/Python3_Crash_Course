#!/usr/bin/env python3.8

# Criando uma estrutura de dados que armazene uma lista em um dicionário
# Utilizando dados de uma pizza

# Definindo dicionario
pizza = {
    'massa': 'penne',
    'ingredientes': ['tomate', 'cebola', 'pimenta'],
}

print("O tipo de massa pedido foi "+pizza['massa'])
print("Essas é sua lista de ingredientes:")
for ingrediente in pizza['ingredientes']:
    print(ingrediente)