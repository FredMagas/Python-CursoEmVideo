# Faça um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = str(input('Digite seu nome completo: '))

busca = 'SILVA' in nome.upper()

if busca is False:
    print(f'O nome {nome.title()} não contém a palavra Silva')
if busca is True:
    print(f'O nome {nome.title()} contém a palavra Silva')
