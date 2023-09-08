# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
v1 = float(input('Digite o salário do funcionário: R$'))

s = v1 * 1.15

print(f'O salário do funcionário com aumento de 15% é igual a R${s:.2f}')
