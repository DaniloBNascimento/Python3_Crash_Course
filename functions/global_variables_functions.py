#!/usr/bin/env python3.8

global onde_vou
onde_vou = ['europa', 'america']

def lugar():
    global onde
    onde = []
    for vou in onde_vou:
        onde.append(vou)
    return onde

lugar()

for aonde in onde:
    print(aonde)

