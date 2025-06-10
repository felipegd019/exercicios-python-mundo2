preco = float(input('Digite o preço do produto: R$ '))

print('''Formas de pagamento:
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Escolha a opção: '))

if  opcao == 1:
    print(f'Você recebeu 10% de desconto ')
    d1 = preco * 0.10
    d2 = preco - d1
    print(f'O valor vai ficar em R${d2:.2f}')
elif opcao == 2:
    print(f'Você recebeu 5% de desconto ')
    d3 = preco * 0.05
    d4 = preco - d3
    print(f'O valor vai ficar em R${d4:.2f}')
elif    opcao == 3:
    print(f'Sem desconto o preço vai ser o mesmo R${preco:.2f}')
elif    opcao == 4:
    juros = preco * 0.20
    calc_juros = preco + juros
    print(f'Você vai receber 20% de juros e o valor vai ficar em R${calc_juros:.2f}')
    parcelas = int(input('Quantas parcelas? '))
    valor_parcela = calc_juros / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R$ {valor_parcela:.2f}')
else:
    print('Opção inválida de pagamento. Tente novamente.')



