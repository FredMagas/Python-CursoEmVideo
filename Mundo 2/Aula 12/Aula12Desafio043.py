# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status, conforme
# tabela abaixo:

# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

peso = float(input('Qual o seu peso em Kg: '))
altura = float(input('Qual a sua altura em metros: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'O seu IMC é {imc:.1f} e você está Abaixo do Peso!')
elif (imc >= 18.5) and (imc < 25):
    print(f'O seu IMC é {imc:.1f} e você está no Peso Ideal!')
elif (imc >= 25) and (imc < 30):
    print(f'O seu IMC é {imc:.1f} e você está com Sobrepeso!')
elif (imc >= 30) and (imc < 40):
    print(f'O seu IMC é {imc:.1f} e você está com Obesidade!')
elif imc >= 40:
    print(f'O seu IMC é {imc:.1f} e você está com Obesidade Mórbida!')
