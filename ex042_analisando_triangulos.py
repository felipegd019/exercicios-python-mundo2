a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Forma um triângulo')

    if a == b == c:
        print('É um triângulo Equilátero!')
    elif a == b or b == c or a == c:
        print('É um triângulo Isósceles!')
    else:
        print('É um triângulo Escaleno!')
else:
    print('Não forma um triângulo')
