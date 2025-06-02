numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[1] converter pra BINÁRIO')
print('[2] converter pra OCTAL')
print('[3] converter pra HEXADECIMAL')
opção = int(input('Sua opção: '))

if opção == 1:
    print(f'O número em binário é {bin(numero)[2:]}')
elif opção == 2:
    print(f'O número em octal é {oct(numero)[2:]}')
elif opção == 3:
    print(f'O número em hexadecimal é {hex(numero)[2:]}')
else:
    print('Opção inválida. Tente novamente.')

