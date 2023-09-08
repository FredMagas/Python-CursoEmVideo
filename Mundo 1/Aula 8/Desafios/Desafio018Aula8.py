# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
ang = float(input('Digite um ângulo: '))

seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print(f'Os valores calculados para esse angulo são: \n Seno: {seno:.3f} \n Cosseno: {coss:.3f} \n Tangente: {tang:.3f}')
