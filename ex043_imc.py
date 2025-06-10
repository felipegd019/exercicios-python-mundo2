peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print(f'Seu IMC é {imc:.2f}')

if  imc <= 18.5:
    print('Abaixo do peso')
elif    imc <= 25:
    print('Peso Ideal')
elif    imc <= 30:
    print('Sobrepeso')
elif    imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')

