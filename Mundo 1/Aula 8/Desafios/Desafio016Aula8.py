# Faça um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Ex: Digite um número: 6.127 => O número 6.127 tem a porção Inteira 6.
from math import trunc
num = float(input('Digite um número Real: '))
inteiro = trunc(num)

print(f'O número {num} tem a porção inteira {inteiro}')
