#!/usr/bin/env python3.8

import os
import time

t1 = time.localtime()
print(t1)
soma = 0

for value in range(1, 100000001):
    soma += value
print(soma)

t2 = time.localtime()
print(t2)


