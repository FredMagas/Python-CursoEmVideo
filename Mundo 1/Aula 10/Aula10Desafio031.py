# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 km e R$0,45 para viagens mais longas.
d = float(input('Qual a distância da viagem em Km? '))
if d <= 200:
    c = 0.50 * d
    print(f'O valor da passagem para uma viagem com {d}Km é igual a: R${c:.2f}')
else:
    c = 0.45 * d
    print(f'O valor da passagem para uma viagem com {d}Km é igual a: R${c:.2f}')
