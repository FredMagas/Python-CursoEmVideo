# Escreva um programa que leia dois números inteiros e compare-os, mostrando uma mensagem na tela:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))

if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n1 < n2:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS!')
