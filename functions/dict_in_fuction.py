#!/usr/bin/env python3.8

def build_person(firs_name, last_name):
    """ Devolve um dicionário com informações sobre pessoa """
    person = {'first': firs_name, 'last': last_name}
    print(person)
    return person

nome = input("Informe o nome: ")
sobrenome = input("Informe o sobrenome: ")
build_person(nome, sobrenome)

