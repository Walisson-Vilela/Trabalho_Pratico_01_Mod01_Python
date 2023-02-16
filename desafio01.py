# 1. Execute e analise a saída do seguinte código no Google Colab1

inicio = 0
fim = 100

for numero in range(inicio, fim):
    if numero % 5 == 0:
        print(numero)


print('2. Altere o código da atividade 1 para que ele exiba os números múltiplos de 2, 5 e 7 (simultaneamente) e que estejam dentro do intervalo entre 100 e 500 (incluindo o 100 e o 500) ')


inicio = 100
fim = 500

lista02 = []
lista05 = []
lista07 = []

for numero in range(inicio, fim + 1):
    while numero % 2 == 0 and numero <= fim:
        lista02.append(numero)
        break
    while numero % 5 == 0 and numero <= fim:
        lista05.append(numero)
        break
    while numero % 7 == 0 and numero <= fim:
        lista07.append(numero)
        break
print(f'Divisores por 02: {lista02}')
print(f'Divisores por 05: {lista05}')
print(f'Divisores por 07: {lista07}')
