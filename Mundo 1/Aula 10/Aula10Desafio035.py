# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'O triângulo formado por: \n {r1} \n {r2} \n {r3} \n Pode existir!')
else:
    print(f'O triângulo formado por: \n {r1} \n {r2} \n {r3} \n Não pode existir!')
