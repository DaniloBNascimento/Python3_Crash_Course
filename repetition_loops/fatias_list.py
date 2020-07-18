#!/usr/bin/env python3.8

list = ['danilo', 'bastos', 'nascimento', 'regina', 'telma']

print("O primeiro nome da lista é: "+list[0])
print("Os três primeros nomes da lista são: ")
for lists in list[:3]:
    print(lists)
print("Os dois últimos nomes da lista são: ")
for lists2 in list[:-3]:
    print(lists2)

