# Faça um programa que realize a conversão de um valor em metros para centímetros e milímetros

n1 = float(input('Digite um valor em metros: '))

km = n1 / 1000
hm = n1 / 100
dam = n1 / 10
dm = n1 * 10
cm = n1 * 100
mm = n1 * 1000

print(f'O valor de {n1} metros é igual a: \n {km}km \n {hm}hm \n {dam}dam \n {dm}dm \n {cm:.0f}cm \n {mm:.0f} mm')
