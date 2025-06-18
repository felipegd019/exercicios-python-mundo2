soma = 0 
for i in range(1,7):
    i = int(input('Digite seis números: '))
    if  i % 2 == 0:
        soma = soma + i
if  soma == 0:
    print('Nenhum número é par')
else:
    print(f'A soma dos numeros pares é: {soma}')        