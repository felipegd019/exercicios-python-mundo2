soma_idades = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
total_mulheres_jovens = 0

for i in range (1,5):
    nome = str(input('Qual é o seu nome? '))
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual é o seu sexo? F/M : ')).upper()
    soma_idades = soma_idades + idade
    if  sexo == 'M':
        if  idade >= maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_mais_velho = nome
    if  sexo == 'F':
        if  idade < 20:
            total_mulheres_jovens = total_mulheres_jovens + 1
        
media = soma_idades / 4

print(f'A média de idade do grupo é de {media} anos!')
print(f'O nome do homem mais velho é {nome_homem_mais_velho}')
print(f'Existem {total_mulheres_jovens} mulheres com menos de 20 anos')



        
