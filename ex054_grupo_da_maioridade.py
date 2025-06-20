ano_atual = 2025
maiores = 0 
menores = 0

for i in range(1, 8):
    ano = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    if  ano_atual - ano >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1 

print(f'Existem {maiores} maiores de idade, e {menores} menores de idade!')

