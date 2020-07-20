#!/usr/bin/env python3.8
# Script de exemplo para ordenar dados de um dicionário

# Definindo o dicionário:
users_and_id = {
    'danilo':1,
    'telma':4,
    'rosy':5,
    'joaquim':2,
    'nycolas':3,
}

# Ordenando dados de acordo com o id dos usuários:
for id in sorted(users_and_id.values()):
    print(id)

