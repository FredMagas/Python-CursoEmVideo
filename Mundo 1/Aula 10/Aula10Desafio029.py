# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.
v = float(input('Digite qual a sua velocidade em Km/h: '))
# Cores
ciano = '\033[1;36m'
li = '\033[m'
ver = '\033[1;31m'

if v > 80:
    valor = 7.00 * (v - 80)
    print(f'{ver}Você foi multado!{li} A velocidade máxima é de {ciano}80Km/h{li} e você estava à {ver}{v}Km/h{li}')
    print(f'O valor da multa é de {ver}R${valor:.2f}{li}!')
else:
    print('Parabéns você não foi multado! Continue assim e sempre dirija com segurança!')
