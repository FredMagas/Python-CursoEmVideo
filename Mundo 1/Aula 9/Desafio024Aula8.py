# Faça um programa que leia o nome de uma cidade e diga se ela começa com o nome "Santo"
cidade = str(input('Digite o nome de uma Cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')
