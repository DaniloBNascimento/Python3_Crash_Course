#!/usr/bin/env python3.8

# Estudando a estrutura de dados dicionário
# Dicionário simples
name = {'name':'danilo'}
# exibindo o valor de name
print(name['name'])

# Dicionário um pouco mais complexo (com mais valores).
name_age = {'name':'danilo', 'last_name':'bastos', 'age': 25}
# Exibindo dados do dicionário acima
print("O nome gravado foi "+name_age['name'])
print(" O sobrenome gravado foi "+name_age['last_name'])
print("  A idade gravada foi "+str(name_age['age']))

# Gravando dados em um dicionário mais completo e com código organizado
user_infos = {
    'nome':'danilo',
    'sobrenome':'bastos nascimento',
    'idade':25,
    'DDD':79,
    'telefone':999522415,
    'endereço':'Rua 160 Albano Franco',
    'número':1,
}
# Exibindo dados do dicionário acima
print("O nome do indivíduo é: "+user_infos['nome'])
print("O endereço do indivíduo é: "+user_infos['endereço'])
print("Número de telefone: "+str(user_infos['telefone']))

# Adicionando um valor manualmente ao dicionário user_info
user_infos['id'] = 7803
# Exibindo todos os valores da lista
print(user_infos)


