#Operadores Aritiméticos

#Algoritimo que mostra os diferentes tipos de operadores aritiméticos
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
soma = num1 + num2
subt = num1 - num2
mult = num1 * num2
div = num1 / num2
pot = num1 ** num2
divint = num1 // num2
rest = num1 % num2
equal = num1 == num2
print (f'Soma: {soma} \nSubtração: {subt}\nMultiplicação: {mult}\nDivisão: {div:.2f}\n'
       f'Potenciação: {pot}\nDivisão Inteira: {divint}\nResto: {rest}\nIgualdade: {equal}')

#Algoritimo que exemplifica a ORDEM DE PRECEDÊNCIA dos operadores aritiméticos
example1 = int(num1 + num2 * 2)
example2 = int(num1 * num2 + 4 ** 2)
example3 = int(3 * ( 5 + 4 ) ** 2)
print(f'exemplo 1 - (num1 + num2 * 2): {example1},'
      f'exemplo 2 - (num1 * num2 + 4 ** 2): {example2},'
      f'exemplo 3 - (3 * ( 5 + 4 ) ** 2): {example3}')

#Exemplificação do uso de potência
raiz_quadrada = num1 ** 2 #raiz quadrada é a potencia multiplicando por (1/2)
raiz_cubica = num1 ** 3 #raiz cúbica é a potencia multiplicando por (1/3)
potencia_num = num1 ** 3 #potenciação elevada ao valor correspondente, (3,4,5..)

#Exemplificando com Strings
hello = 'hello' + ' girl'
hi = 'hi' * 10
word = '=' * 10
print(f'Exemplos de identação com Fstrings: {hello}, {hi}, {word}')