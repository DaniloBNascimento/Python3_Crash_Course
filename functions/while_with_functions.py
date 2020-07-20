#!/usr/bin/env python3.8

def get_nome(nome, sobrenome):
    full_name = nome + " " + sobrenome
    if nome == 'quit':
        exit(0)
    print("O nome informado foi: "+full_name.title())
    return full_name


while True:
    get0 = input("Digite o nome: ")
    get1 = input(" Digite o sobrenome: ")
    get_nome(get0, get1)



