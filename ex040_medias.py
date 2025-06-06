n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2
print(f'Sua média: {media:.1f}')

if media >= 7:
    print('Situação: APROVADO')
elif 5 <= media < 7:       
    print('Situação: RECUPERAÇÃO')
else:                         
    print('Situação: REPROVADO')
