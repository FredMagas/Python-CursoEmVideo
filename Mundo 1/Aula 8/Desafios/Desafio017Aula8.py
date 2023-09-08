# Faça um program que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
from math import hypot
op = float(input('Digite o Cateto Oposto: '))
ad = float(input('Digite o Cateto Adjacente: '))

hipotenusa = hypot(op, ad)

print(f'O valor da hipotenusa deste triângulo retângulo é: {hipotenusa:.2f}')
