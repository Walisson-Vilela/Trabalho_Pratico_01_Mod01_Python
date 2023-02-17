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

print('\n')

print('Questão 04\n')

nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'

print('Transforme todos os caracteres das variáveis em maiúsculo')
print(nome.upper())
print(cidade.upper())
print(cpf.upper())

print('\nTransforme todos os caracteres das variáveis em maiúsculo')
print(nome.lower())
print(cidade.lower())
print(cpf.lower())

print('\nExiba a posição do caractere ã, se presente, em cada uma das variáveis')
print(nome.find('ã'))
print(cidade.find('ã'))

print('\nExiba a posição do caractere ã, se presente, em cada uma das variáveis')
print(len(nome))
print(len(cidade))
print(len(cpf))

print('\nRemova os pontos (.) e o hífen (–) da variável cpf')
new_cpf = ''.join(char for char in cpf if char.isalnum())
print(new_cpf)

print('\nQuestao 05')

numero = '127957'
soma = 0

for numero_ in numero:
    numero_inteiro = int(numero_)
    soma += numero_inteiro
print(f'\nA soma deverá ser 1 + 2 + 7 + 9 + 5 + 7 = {soma}')
