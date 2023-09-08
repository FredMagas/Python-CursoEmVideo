# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo é negado.

imovel = float(input('Qual o valor do imóvel? R$'))
renda = float(input('Qual o valor da sua renda mensal? R$'))
anos = int(input('Em quantos anos você gostaria de terminar o pagamento? '))

meses = anos * 12
parcela = imovel / meses
limite = (parcela / renda) * 100

if limite >= 30:
    print('Infelizmente não será possível realizarmos empréstimo para você no momento. Tente novamente em alguns meses.')
elif limite < 30:
    print(f'O valor das parcelas em {anos} anos para o imóvel no valor de R${imovel:.2f} é de R${parcela:.2f}.')
