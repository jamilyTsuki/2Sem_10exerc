numeros = [10, 25, 8, 40, 15, 30, 7, 50, 12, 20]
busca = int(input('Digite o número que deseja buscar: '))

for i, valor in enumerate(numeros):
    if valor == busca:
        print(f'Número encontrado no índice {i}')
        break
else:
    print('Número não encontrado.')