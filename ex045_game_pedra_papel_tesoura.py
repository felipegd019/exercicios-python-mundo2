import random

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)

print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
print('KEN')
print('PÔ!!!')

print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')

if computador == jogador:
    print('EMPATE!')
elif (computador == 0 and jogador == 2) or (computador == 1 and jogador == 0) or (computador == 2 and jogador == 1):
    print('COMPUTADOR VENCE!')
else:
    print('JOGADOR VENCE!')
