#!/usr/bin/env python3.8

# Código criado para armazernar um dicionário dentro de outro dicionário

# Definindo
users = {
    'dan_boy': {
        'firstname': 'danilo',
        'last_name': 'bastos',
        'age': 25,
        },
    'rosy_girl': {
        'firstname': 'rosy',
        'last_name': 'nascimento',
        'age': 30,
        },
    }
for username, userinfo in users.items():
    fullname = userinfo['firstname']+" "+userinfo['last_name']
    idade = userinfo['age']
    print("Nome completo: " + fullname + " " + ", idade: " + str(idade))