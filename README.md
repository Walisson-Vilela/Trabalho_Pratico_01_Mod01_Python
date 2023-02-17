#Trabalho Prático
Primeiro desafio prático do curso Desenvolvedor Python da XP Educação

1. Execute e analise a saída do seguinte código no Google Colab1
.
# declaração das variáveis
inicio = 0
fim = 100
# verifica quais números são divisíveis por cinco, e exibe aqueles que são
for numero in range(inicio, fim):
 if numero % 5 == 0:
 print(numero)
 
2. Altere o código da atividade 1 para que ele exiba os números múltiplos de
2, 5 e 7 (simultaneamente) e que estejam dentro do intervalo entre 100 e
500 (incluindo o 100 e o 500).

3. Altere o código da atividade 1, criando uma variável divisor e, em seguida,
verifique quais os números no intervalo entre 0 e 1000 (incluindo o 0 e
excluindo o 1000) são múltiplos da variável divisor.
Por exemplo, se o valor de divisor for igual a 3, todos os números múltiplos de 3,
dentro do intervalo, deverão ser exibidos (0, 3, 6, 9, ..., 996, 999).

4. Crie um código declarando as seguintes variáveis do tipo string:
# variáveis do tipo string
nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'
Em seguida, realize as seguintes transformações nas variáveis:
● Transforme todos os caracteres das variáveis em maiúsculo;
● Transforme todos os caracteres das variáveis em minúsculo;
● Exiba a posição do caractere ã, se presente, em cada uma das variáveis;
● Exiba o número de caracteres de cada variável;
● Remova os pontos (.) e o hífen (–) da variável cpf.
1 https://colab.research.google.com/

5. Crie um código que realize o somatório de todos os caracteres da seguinte
string:
numero = '127957'
Para resolver este problema, considere as seguintes dicas:
● A soma deverá ser 1 + 2 + 7 + 9 + 5 + 7 = 31;
● Utilize o laço de repetição for … in; para percorrer cada caractere da string;
● Utilize a conversão do tipo string para o tipo inteiro (int(caractere)) para
converter os caracteres em valores numéricos;
● Utilize uma variável auxiliar, soma, para acumular o somatório dos valores.
