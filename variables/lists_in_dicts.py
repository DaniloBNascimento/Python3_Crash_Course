#!/usr/bin/env python3.8
# Código simples criado para interação entre lista e dicionários:


# Executando um for do tipo function range para criar 30 aliéniginas verdes em um jogo:
aliens = []
for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow',
    }
    aliens.append(new_alien)

#Mostrando itens
for alien in aliens[0:4]:
    print(alien)

# Mostrando a quantidade total de aliens:
print("A quantidade total de aliens criados foi: "+str(len(aliens)))

# Modificando dados dos 4 primeiros alieníginas
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['points'] = 10
        alien['speed'] = 'medium'

# Mostrando itens modificados
for alien in aliens[0:4]:
    print(alien)
