# Exercise 5 - Crie um programa que leia e mostre um número inteiro e mostre na tela o seu sucessor e antecessor
ex5_num = float(input('Digite um número: '))
ant = ex5_num - 1
suc = ex5_num + 1
print(f'Sendo: {ex5_num:.0f}, seu sucessor é: {suc:.0f} e seu antecessor é: {ant:.0f}')

#Exercise 6: Crie um algoritmo que leio o nùmero e mostre o seu dobro, triplo e raiz quadrada
ex6_num2 = float(input('Insira um número: '))
ex6_double = ex6_num2 * 2
ex6_triple = ex6_num2 * 3
ex6_squareroot = ex6_num2 ** (1/2)
print (f'O número é {ex6_num2:.0f}, o dobro é: {ex6_double:.0f},'
       f' o triplo é: {ex6_triple:.0f} e a raiz quadrada é: {ex6_squareroot:.2f}')

#Exercise 7: Um programa que leia as duas notas do aluno, calcule e mostre a média
nota1 = float(input("Nota do primeiro semestre: "))
nota2 = float(input("Nota do segundo semestre: "))
media = (nota1 + nota2) / 2
print(f'A nota do primeiro semestre é: {nota1:.1f}, '
      f'a nota do segundo semestre é: {nota2:.1f} '
      f'e a média semestral é: {media:.1f}')

#Exercise 8: Escreva um programa que leia um valor em (m) e converta em (cent) e (mili):

metros = float(input('Digite um número em metros: '))
cent = metros * 100
mili = metros * 1000
print(f'Metros: {metros:.1f}, Centímetros: {cent:.0f} e Milímetros: {mili:.0f}')

#Exercise 9: Faça um programa que leia um número inteiro e mostre na tela sua tabuada
ex9_num = int(input('Digite um número para sua tabuada: '))
x1 = ex9_num * 1
x2 = ex9_num * 2
x3 = ex9_num * 3
x4 = ex9_num * 4
x5 = ex9_num * 5
x6 = ex9_num * 6
x7 = ex9_num * 7
x8 = ex9_num * 8
x9 = ex9_num * 9
print(f'Para: {ex9_num} é:'
      f'\n{ex9_num} x 1 = {x1:2}\n{ex9_num} x 2 = {x2:2}'
      f'\n{ex9_num} x 3 = {x3:2}\n{ex9_num} x 4 = {x4:2}'
      f'\n{ex9_num} x 5 = {x5:2}\n{ex9_num} x 6 = {x6:2}'
      f'\n{ex9_num} x 7 = {x7:2}\n{ex9_num} x 8 = {x8:2}'
      f'\n{ex9_num} x 9 = {x9:2}')

# Exercício 10: Um programa que mostre quantos dinheiro ela
# tem na carteira e quantos dólares ela pode comprar

reais = float(input("Quanto você quer converter para dólar?: "))
dolar = reais / 5.29
print(f'Você pode comprar US${dolar:.2f} com R${reais:.2f}.')

# Exercício 11: Faça um programa que leia a largura e a altura de uma parede em metros
# calcule a área e a quantidade de tinta sabendo que cada lata pinta 2m.
larg = float(input("Insira a largura: "))
alt = float(input("Insira a altura: "))
area = larg * alt
paint = area / 2
print(f'Com uma altura de {alt:.1f} e largura de {larg:.2f}, a área total é de {area:.2f}.\n'
      f'Serão necessários {paint:.1f} baldes de tinta para pintar a parede totalmente.')

# Exercise 12: Um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
price = float(input('Insira o valor: '))
desconto = (price / 100) * 5
valor_final = price - desconto
print(f'Preço original: R${price:.2f}\n '
      f'Desconto: R${desconto:.2f}\n'
      f'Valor final: R${valor_final:.2f}.')

# Exercise 13: Faça um algoritimo que leia o salário de um funcionário
# e mostre seu novo salário com 15% de aumento

salario = float(input('Insira o salário: '))
aumento = (salario / 100) * 15
salario_novo = salario + aumento
print(f'Salário: R${salario:.0f}\n'
      f'Aumento: R${aumento:.2f}\n'
      f'Novo salário R${salario_novo:.2f} (15%)')

# Exercise 14: Escreva um programa que converta uma temperatura em C° e converta para F°
grau = float(input('Insira a temperatura em C°: '))
fahrenheit  = grau * 1.8 + 32
print(f'Celcius: {grau:.2f} \n'
      f'Fahrenheit: {fahrenheit:.2f}')

# Exercise 15: Quantidade de KM percorridos por um carro alugado e a quantidade de dias que foi alugado
# Calcule o preço a pagar sabendo que o carro custa R$60 o dia e R$ 0,15km rodado
dias = int(input('Quantos dias alugou o carro? '))
km = float(input('Quantos km rodados? '))
dias_rodado = dias * 60
km_rodado = km * 0.15
total = dias_rodado + km_rodado
print(f'Dias: {dias}\n'
      f'Km percorridos: {km:.2f}\n'
      f'Valor da diária: {dias_rodado:.2f}\n'
      f'Valor Km percorridos: {km_rodado:.2f}\n'
      f'Valor final: {total:.2f}')