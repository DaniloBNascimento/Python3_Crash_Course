#!/usr/bin/env python3.8

def ola_users(names):
    for name in names:
        msg = "Olá usuário: " + name.title() + " seja bem vindo!"
        print(msg)
users = ['danilo', 'telma', 'valdemir']

ola_users(users)