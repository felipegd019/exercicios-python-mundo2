frase = str(input('Digite uma frase: '))
frase = frase.replace(' ', '')
frase = frase.lower()

if  frase[::-1] == frase:
    print('É um palindromo')
else: 
    print('Nao é um palindromo')