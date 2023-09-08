# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2 m²
n1 = float(input('Digite a Comprimento: '))
n2 = float(input('Digite a Altura:'))
pa = float(input('Digite o rendimento em L/m² da tinta: '))

c1 = (n1 * n2)
c2 = c1 / pa

print(f'Para pintar uma parede com área de {c1}m² e uma tinta com rendimento de {pa}m² será necessário {c2}L de tinta!')
