# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
print('Digite um ano e eu te digo se ele é BISSEXTO ou não!')
ano = int(input('Qua ano quer analisar? (Digite 0 para analisar o ano atual): '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} não é BISSEXTO')
