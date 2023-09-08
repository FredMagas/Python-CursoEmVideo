# Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre para ela quantos dólares ela pode comprar

from datetime import date

data_atual = date.today()
data_em_texto = data_atual.strftime('%d/%m/%Y')

n1 = float(input('Quantos reais você tem? R$'))

# US$5,06 data consulta 09/04/2023

c = n1 / 5.06

print(f'Você pode comprar US${c:.2f} na cotação de hoje {data_em_texto}')
