# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome escolhido.
from random import choice
n1 = str(input('Digite o nome do primeiro Aluno: '))
n2 = str(input('Digite o nome do segundo Aluno: '))
n3 = str(input('Digite o nome do terceiro Aluno: '))
n4 = str(input('Digite o nome do quarto Aluno: '))
lista = [n1, n2, n3, n4]

sorteio = choice(lista)

print(f'O Aluno sorteado para apagar o quadro é {sorteio}')
