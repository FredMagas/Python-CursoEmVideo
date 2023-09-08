# Cores no terminal
# ANSI: Sequence escape
# \033[CODdaCORm = \033[STYLE;TEXT;BACKm = \033[0;33;44m
# Style: 0=None 1=Negrito 4=Underline 7=Negative
# Text: 30=Preto 31=Vermelho 32=Verde 33=Amarelo 34=Azul 35=Roxo 36=Ciano 37=Cinza 97=Branco
# Background: 40=Preto 41=Vermelho 42=Verde 43=Amarelo 44=Azul 45=Roxo 46=Ciano 47=Cinza 107=Branco
# print('\33[7;36;41m Olá,Mundo! \033[m')
# a = 3
# b = 5
# print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!')
nome = str(input('Digite o seu nome: '))
ciano = '\033[1;36m'
limpa = '\033[m'
print(f'Olá! Muito prazer em te conhecer, {ciano}{nome}{limpa}!!')
