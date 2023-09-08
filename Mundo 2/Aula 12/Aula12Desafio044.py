# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:

# à vista no dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print(f'{" LOJAS MAGA ":=^40}')

preco = float(input('Qual o valor da compra? R$ '))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual a opção? '))

if opcao == 1:
    dinheiro = preco * 0.90
    print(f'Sua compra de R${preco:.2f} vai custar R${dinheiro:.2f} no final.')
elif opcao == 2:
    cartao = preco * 0.95
    print(f'Sua compra de R${preco:.2f} vai custar R${cartao:.2f} no final.')
elif opcao == 3:
    parcela = preco / 2
    print(f'Sua compra vai custar R${preco:.2f} com 2 parcelas de R${parcela} SEM JUROS.')
elif opcao == 4:
    parcelas = int(input('Em quantas parcelas: '))
    vlr_total = preco * 1.20
    vlr_parcelas = vlr_total / parcelas

    print(f'Sua compra será parcelada em {parcelas}x de R${vlr_parcelas:.2f} COM JUROS.')
    print(f'Sua compra de R${preco:.2f} vai custar R${vlr_total:.2f} no final.')
else:
    print('[ERRO] Digite uma opção válida!')
