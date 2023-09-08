# Faça um programa que leia um número inteiro e mostra na tela a sua tabuada
n1 = int(input('Digite um número: '))

c1 = n1 * 1
c2 = n1 * 2
c3 = n1 * 3
c4 = n1 * 4
c5 = n1 * 5
c6 = n1 * 6
c7 = n1 * 7
c8 = n1 * 8
c9 = n1 * 9
c10 = n1 * 10

print(f'A tabuada para este número é: \n {n1} x 1 = {c1} \n {n1} x 2 = {c2} \n {n1} x 3 = {c3} \n', end=' ')
print(f'{n1} x 4 = {c4} \n {n1} x 5 = {c5} \n {n1} x 6 = {c6} \n {n1} x 7 = {c7} \n {n1} x 8 = {c8}\n', end=' ')
print(f'{n1} x 9 = {c9} \n {n1} x 10 = {c10}')
