# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# Ex: Ana Maria de Souza → Primeiro = Ana Último = Souza
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print(f'Muito prazer em te conhecer {nome.title()}!')
print(f'O seu primeiro nome é {n[0]}')
print(f'O seu último nome é {n [-1]}')
