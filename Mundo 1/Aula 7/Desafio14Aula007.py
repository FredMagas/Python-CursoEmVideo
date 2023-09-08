# Faça um programa que leia a temperatura em °C e realize a conversão para Fahrenheit

temperatura = float(input(f'Digite a temperatura em °C: '))
c = (temperatura * 1.8) + 32

print(f'A temperatura de {temperatura:.1f}°C corresponde a {c:.1f}°F')
