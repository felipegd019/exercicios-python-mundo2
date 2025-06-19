frase = str(input('Digite uma frase: '))
frase = frase.replace(' ', '')
frase = frase.lower()

ultima = len(frase)-1
invertida = ''

for i in range(ultima ,-1 ,-1):
    invertida = invertida + frase[i]
    
if frase == invertida:
    print(f'A frase {frase} é um palindromo')
else:
    print(f'A frase {frase} náo é um palindromo')
