#!/usr/bin/env python3.8

cubes = []
count = 0
for cube in range(1,11):
    cubes.append(cube**3)
    print("Cubo de "+str(cube)+" é "+str(cubes[count]))
    count += 1

