# Faça um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras no total sem considerar espaços
# Quantas letras tem no primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()

ma = nome.upper()
mi = nome.lower()
total = len(nome) - nome.count(' ')
# p1nome = nome.find(' ')
separa = nome.split()

print(f'O seu nome maiúsculo:{ma}')
print(f'O seu nome Minúsculo: {mi}')
print(f'O seu nome tem {total} de letras.')
print(f'O seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras.')
