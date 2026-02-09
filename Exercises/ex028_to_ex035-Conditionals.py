# Exercise 28: Um programa que faça o computador pensar em um número inteiro entre 0-5
# Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Import and generate a interger ' to 5' random number
from random import randint
random_number = randint(0,5)
# User input
user_num = int(input('Insira um número de 0 a 5: '))
# Verify if the 'user_num' is higher or lower between 1-5
if user_num > 5 or user_num < 0:
    print('O número não é valido!')
# Show if the number predicted is correct or wrong
else:
    if user_num != random_number:
        print(f'Você errou! O numero digitado foi: {user_num}.\n'
              f'O correto é {random_number}!')
    else:
        print(f'Você acertou! O número digitado foi: {user_num}!\n'
              f'O computador imaginou: {random_number}!')

# Exercise 29: Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre que ele foi multado
# A multa vai custar R$ 7 por cada KM acima do limite

# Immutable values for penalty and max speed
penalty = 7
max_speed = 80

# User KM/h input
car_kmh = float(input('Insert the car speed: '))

if car_kmh < 0:
    print('Não tem como tomar multa de ré, amigo.')
else:
    # It shows how much it surpassed the limit
    if car_kmh > max_speed:
        # Calc the diff between user speed and the limit speed and calc the tax paid for it
        speed_diff = car_kmh - max_speed
        penalty_paid = speed_diff * penalty
        print(f'Você passou a: {car_kmh}KM/h!\n'
              f'Sendo {speed_diff} acima do limite de: {max_speed}!\n'
              f'Multa por KM/h acima: R${penalty_paid:.2f}')
    else:
        print(f'Você passou a {car_kmh} KM/h!\n'
              f'Está dentro do limite de {max_speed} KM/h!')

# Exercise 30: Crie um programa leia um num inteiro mostre e se é par ou impar
usr_num = int(input('Digite um número: '))
calc = usr_num % 2
if calc == 0:
    print(f'O número {usr_num} é par!')
else:
    print(f'O número {usr_num} é ímpar!')

# Exercise 31: Pergunte a distância de uma viagem em KM
# Calcule o preço da passagem cobrando R$ 0,50 por KM/h para até 200km
# e R$0,45 para viagens + longas

# Immutable numbers
green_flag = 0.5
red_flag = 0.45

# User KM input
dist_km = float(input('Digite a distância: '))

# Conditional of taxes green vs red
if dist_km <= 200:
    green_tax = dist_km * green_flag
    print(f'Você irá pagar R${green_tax:.2f} nessa viagem!')
else:
    red_tax = dist_km * red_flag
    print(f'Você irá pagar R${red_tax:.2f} nessa viagem!')

# Exercise 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

year = int(input('Insira o ano: '))

if year % 4 == 0: # se o ano for divisível por 4 segue
    if year % 100 == 0: #se o ano for divisível por 4 E por 100
        if year % 400 == 0:
            print('é bissexto')
        else:
            print('não é bissexto!')
    else:
        print('É bissexto!')
else:
    print('Não é bissexto')

# Exercício 33 — Maior e menor entre três números
# Objetivo: ler três números e determinar qual é o maior e qual é o menor
# usando apenas estruturas condicionais básicas (if).

# Leitura dos valores de entrada
# Usamos float para aceitar números inteiros e decimais
num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
num3 = float(input('Terceiro número: '))

# Estado inicial:
# Assumimos, inicialmente, que o primeiro número é
# tanto o maior quanto o menor.
# Essa é apenas uma hipótese inicial, que será corrigida depois.
maior = num1
menor = num1

# Comparação do segundo número
# Se o segundo número for maior que o maior atual,
# atualizamos a variável maior
if num2 > maior:
    maior = num2

# Se o segundo número for menor que o menor atual,
# atualizamos a variável menor
if num2 < menor:
    menor = num2

# Comparação do terceiro número
# Se o terceiro número for maior que o maior atual,
# atualizamos a variável maior
if num3 > maior:
    maior = num3

# Se o terceiro número for menor que o menor atual,
# atualizamos a variável menor
if num3 < menor:
    menor = num3

# Após todas as comparações, as variáveis maior e menor
# representam corretamente o maior e o menor valor informados
print(f'O maior é {maior} e o menor é {menor}!')


# Exercise 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para salários iguais ou inferiores a R$ 1.250,00, o aumento é de 15%.
base_income = float(input('Insira salário base: R$ '))
if base_income <= 1250:
    higher_increase = base_income * 0.15
    higher_income = higher_increase + base_income
    print(f'Seu salário base é: R$ {base_income:.2f}\n'
          f'Acréscimo de 15%: R$ {higher_increase:.2f}\n'
          f'Total pós aumento: R$ {higher_income:.2f}')
else:
    lower_increase = base_income * 0.1
    lower_income = lower_increase + base_income
    print((f'Seu salário base é: R$ {base_income:.2f}\n'
          f'Acréscimo de 10%: R$ {lower_increase:.2f}\n'
          f'Total pós aumento: R$ {lower_income:.2f}'))

# Exercise 35: Desenvolva um programa que leia o comprimento de três retas
# diga ao usuário se elas podem ou não formar um triângulo.
side_a = float(input('Lado A: '))
side_b = float(input('Lado B: '))
side_c = float(input('Lado C: '))

verify_a = side_a < side_b + side_c
verify_b = side_b < side_a + side_c
verify_c = side_c < side_b + side_a

if verify_a and verify_b and verify_c:
    print(f'A: {side_a:.1f}\n'
          f'B: {side_b:.1f}\n'
          f'C: {side_c:.1f}\n'
          f'Isso é um triângulo!')
else:
    print(f'A: {side_a:.1f}\n'
          f'B: {side_b:.1f}\n'
          f'C: {side_c:.1f}\n'
          f'Isso NÃO é um triângulo!')