n1 = int(input('Digite um número: '))
contador = 0 

for i in range(1, n1+1):
    if  n1 % i == 0:
        contador = contador + 1


if  contador == 2:
    print('Ele é primo')
else:
    print('Ele não é primo')
