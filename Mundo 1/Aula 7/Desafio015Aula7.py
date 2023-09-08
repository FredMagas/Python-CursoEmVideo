# Faça um programa que leia a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele
# foi alugado e calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

carro = float(input('Qual o valor da diária do carro alugado: R$ '))
custokm = float(input('Qual o valor do Km rodado: R$ '))
distancia = float(input('Qual a Km percorrida: '))
dias = int(input('Quantas diárias no total: '))

custodia = carro * dias
custorodado = custokm * distancia

total = custodia + custorodado

print(f'O valor a pagar por {dias:.1f} diárias é de:\n Diária: R${custodia:.2f}', end='')
print(f'\n Km rodados: R${custorodado:.2f} \n Total: R${total:.2f}')
