ano = int(input('Qual o ano do seu nascimento? '))
calculo = 2025 - ano
print(f'O atleta tem {calculo} anos.')

if calculo <= 9:
    print('Classificação: MIRIM')
elif calculo <= 14:
    print('Classificação: INFANTIL')
elif calculo <= 19:
    print('Classificação: JUNIOR')
elif calculo <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

