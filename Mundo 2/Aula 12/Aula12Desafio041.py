# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua
# categoria, conforme a sua idade:

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date

nascimento = int(input('Qual o seu ano de nascimento: '))

ano = date.today().year
idade = ano - nascimento

if idade <= 9:
    print(f'Você tem {idade} anos e está na categoria MIRIM!')
elif idade <= 14:
    print(f'Você tem {idade} e está na categoria INFANTIL!')
elif idade <= 19:
    print(f'Você tem {idade} e está na categoria JUNIOR!')
elif idade <= 25:
    print(f'Você tem {idade} e está na categoria SÊNIOR!')
elif idade > 25:
    print(f'Você tem {idade} e está na categoria MASTER!')
