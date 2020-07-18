#!/usr/bin/env python3.8

print("Trabalahando com listas...")
# listas
names = ['danilo', 'regina']
nomes = names[:]
# Adicionando itens as listas
names.append('telma')
nomes.append('valdemir')
# Provando que são listas diferentes
print("nomes que estão na lista names:")
for namess in names:
    print(namess)
print("nomes que estão na lista nomes:")
for nomess in nomes:
    print(nomess)


