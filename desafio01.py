# 1. Execute e analise a saída do seguinte código no Google Colab1

print('Questao 01\n ')
inicio = 0
fim = 100

for numero in range(inicio, fim):
    if numero % 5 == 0:
        print(numero)

print('\n')
print('Questao 02\n ')

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
print(f'Divisores por 02: \n{lista02}')
print(f'Divisores por 05: \n{lista05}')
print(f'Divisores por 07: \n {lista07}')

print('\n')

print('Questão 03\n')

inicio = 0
fim = 1000
divisor = int(input('Digite um numero: '))

lista = []

for numero in range(inicio, fim + 1):
    while numero % divisor == 0 and numero <= fim:
        lista.append(numero)
        break
print(f'Lista divisivel por {divisor}')
print(lista)
