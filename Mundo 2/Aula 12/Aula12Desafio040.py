# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
# média atingida:

# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÂO
# Média 7.0 ou superior: APROVADO

nota1 = float(input('Qual a sua nota da P1: '))
nota2 = float(input('Qual a sua nota da P2: '))

media = (nota1 + nota2) / 2

if media <= 5.0:
    print(f'Sua média é {media:.1f} e você foi REPROVADO!')
elif (media > 5.0) and (media <= 6.9):
    print(f'Sua média é {media:.2f} e você está de RECUPERAÇÃO!')
elif (media > 6.9) and (media < 7):
    print(f'Sua média é {media:.2f} e foi arredondada para 7 você foi APROVADO mais precisa se dedicar mais!')
elif media >= 7.0:
    print(f'Sua média é {media:.1f} e você foi APROVADO!')

