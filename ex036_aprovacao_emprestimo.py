valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salario do comprador? '))
anos = int(input('Em quantos anos voce vai pagar a casa? '))
anos_meses = anos * 12
porcentagem = salario * 0.30

calculo_emprestimo = valor / anos_meses
print(f'Para pagar uma casa de R${valor:.2f} em {anos} a prestação será de R${calculo_emprestimo:.2f}')

if  calculo_emprestimo <= porcentagem:
    print(f'Empréstimo pode ser concedido!')
else: 
    print(f'Emprestimo negado!')

