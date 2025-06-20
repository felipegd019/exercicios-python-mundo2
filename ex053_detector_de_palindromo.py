frase = str(input('Digite uma frase: ')).lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for i in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[i]

if  inverso == frase:
    print('A frase é um palindromo!')
else:
    print('Não temos um palindromos')


