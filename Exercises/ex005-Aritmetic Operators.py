#Operadores Aritiméticos
num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')
soma = int(num1) + int(num2)
subt = int(num1) - int(num2)
mult = int(num1) * int(num2)
div = int(num1) / int(num2)
pot = int(num1) ** int(num2)
divint = int(num1) // int(num2)
rest = int(num1) % int(num2)
print (f'Soma: {soma}, Subtração {subt}, Multiplicação {mult}, Divisão {div:.2f},'
       f'Potenciação: {pot}, Divisão Inteira: {divint}, Resto {rest}')