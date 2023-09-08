# Faça um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais o aumento é de 15%.
s = float(input('Digite o salário do funcionário: '))
if s > 1250.00:
    c = s * 1.10
    print(f'Quem ganhava R${s} agora passará a ganhar R${c:.2f}')
else:
    c = s * 1.15
    print(f'Quem ganhava R${s} agora passará a ganhar R${c:.2f}')
