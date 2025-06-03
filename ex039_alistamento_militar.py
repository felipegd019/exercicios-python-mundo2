# Exercício 39 - Curso em Vídeo Python
# Verifica situação de alistamento militar com base no ano de nascimento

nascimento = int(input('Ano de nascimento: '))
ano = 2017  # ano fixo usado no exercício
idade = ano - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano}.')

if idade < 18:
    faltam = 18 - idade
    print(f'Ainda faltam {faltam} anos para o alistamento.')
elif idade == 18:
    print('Você tem que se alistar imediatamente!')
else:
    atraso = idade - 18
    ano_alistamento = ano - atraso
    print(f'Você já deveria ter se alistado há {atraso} anos.')
    print(f'Seu alistamento foi em {ano_alistamento}.')

