# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
from time import sleep
sorteado = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n = int(input('Qual o número que escolhi? '))
print('PROCESSANDO...')
sleep(3)
if n == sorteado:
    print(f'Você venceu! O número sorteado era mesmo o {n}!')
else:
    print(f'Você perdeu! O número sorteado é {sorteado} e não o {n}!')
