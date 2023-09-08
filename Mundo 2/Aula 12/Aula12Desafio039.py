# Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade:
# Se ele ainda vai se alistar no serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
print(2 * '---', 'Verifique se você precisa se alistar:', 2 * '---')
n1 = int(input('Em que ano você nasceu? '))

ano = date.today().year

idade = ano - n1

if idade == 18:
    print(f'Você tem {idade} e precisa se alistar no serviço militar!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você não tem 18 anos ainda faltam {saldo} anos para o alistamento!')
    tempo = ano + saldo
    print(f'Seu alistamento será em {tempo}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos!')
    tempo = ano - saldo
    print(f'Seu alistamento foi em {tempo}')
