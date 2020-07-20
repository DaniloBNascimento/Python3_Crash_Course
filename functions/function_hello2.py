#!/usr/bin/env python3.8

def camiseta(tamanho, texto):
    print(" O tamanho da camiste é: "+str(tamanho))
    print(" O texto estampado será: "+texto)

tam = float(input("Informe o tamanho da camiseta: "))
txt = input("Escreva o texto aqui: ")

camiseta(tam, txt)
print(" Usando parametros nomeados")
camiseta(texto=txt, tamanho=tam)
