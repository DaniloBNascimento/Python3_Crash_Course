#!/usr/bin/env python3.8
# Código Python criado para transferir dados entre listas
# Lista de usuários não confirmados
users_not_confirmed = ['danilo', 'telma', 'valdemir']
# Lista de usuários confirmados
users_yes_confirmed = []

# Laço que verifica cada usuário não confirmado
while users_not_confirmed:
    current_user = users_not_confirmed.pop()
    print("Verificando usuário " + current_user.title())
    users_yes_confirmed.append(current_user)

# Exibindo todos os usuários inseridos
for users_confirmed in users_yes_confirmed:
    print(users_confirmed)
print(" Fim da lista!")