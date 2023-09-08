# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p1 = float(input('Digite o preço do produto: R$'))

d = p1 * 0.95

print(f'O valor do produto com 5% de desconto é: R${d:.2f}')
