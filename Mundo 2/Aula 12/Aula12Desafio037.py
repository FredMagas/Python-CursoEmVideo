# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual sera a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

inteiro = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases de conversão: 
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{inteiro} convertido para BINÁRIO é igual a {bin(inteiro)[2:]}')
elif opcao == 2:
    print(f'{inteiro} convertido para OCTAL é igual a {oct(inteiro)[2:]}')
elif opcao == 3:
    print(f'{inteiro} convertido para HEXADECIMAL é igual a {hex(inteiro)[2:]}')
else:
    print('[ERRO] Opção inválida! Digite uma opção entre 1 e 3')
