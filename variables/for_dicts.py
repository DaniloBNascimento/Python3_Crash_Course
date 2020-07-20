#!/usr/bin/env python3.8

import os
import time
# Declarando o dicionário
user_infos = {
    'nome':'danilo',
    'sobrenome':'bastos nascimento',
    'idade':25,
    'DDD':79,
    'telefone':999522415,
    'endereço':'Rua 160 Albano Franco',
    'número':1,
    }
for key, value in user_infos.items():
    print("\n"+key)
    print(value)

time.sleep(2)
os.system('clear')
time.sleep(2)
my_value = 'java'

# Definindo outro dicionário
favorites_languages = {
    'danilo':'C++',
    'marcos':'javascript',
    'matheus':'shellscript',
    'nycolas': my_value,
}

for name, language in favorites_languages.items():
    print("\nNome: "+name)
    print("Linguagem favorita: "+language)

print("O participantes da pesquisa foram os seguintes:")

for key in favorites_languages.keys():
    print(key)
+.,



