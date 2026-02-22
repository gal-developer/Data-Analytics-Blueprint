# Exercise 36: escreva um programa para aprovar o empréstimo bancário de uma casa
# Pergunte o Valor da casa, o salário do comprador e em quantos anos ele vai pagar
# a prestação mensal não pode ser maior que 30% do salário ou então o empréstimo será negado

house_price = float(input('Insira o valor da casa: R$ ').replace(',', '.'))  # valor da casa
years_to_pay = int(input('Em quantos anos quer pagar? '))  # meses para o pagamento
buyer_income = float(input('Insira o seu salário liquido: R$ ').replace(',', '.'))  # renda mensal

if house_price <= 0 or years_to_pay <= 0 or buyer_income <= 0:
    print("O valor é inválido!")

else:
    years_in_months = years_to_pay * 12  # converte anos para meses
    monthly_payment = house_price / years_in_months  # pagamento mensal que o cliente deseja
    safe_tax = buyer_income * 0.3  # taxa mínima segura com o salário do cliente

    if monthly_payment <= safe_tax:
        print(f'Financiamento Aprovado!\n'
              f'Valor do financiamento: R$ {house_price:.2f}\n'
              f'Número de parcelas: {years_in_months:.0f}\n'
              f'Pagamento mensal: R$ {monthly_payment:.2f}\n')
    else:
        print(
            f'Financiamento negado! A parcela de R$ {monthly_payment:.2f} é maior que o valor seguro de 30% (R${safe_tax:.2f}!')

# Exercise 37: Leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal
# O programa deve converter o número informado para a base escolhida e exibir o resultado na tela.

base_convertion = int(input("Selecione uma base: (Binário: 1) (Octal: 2) (Hex: 3): ")) #base de comparação para escolha
nmbr = int(input("Insira um número inteiro: ")) #input de numero inteiro
if base_convertion == 1: #escolha binaria
    binary_conversion = bin(nmbr)
    print(f'Você escolheu: Binário1\n'
          f'A sua versão binária é: {binary_conversion}!')
elif base_convertion == 2: # escolha octal
    oct_conversion = oct(nmbr)
    print(f'Você escolheu: Octal\n'
          f'A sua versão octal é: {oct_conversion}!')
elif base_convertion == 3: #escolha hexadecimal
    hex_convertion = hex(nmbr)
    print(f'Você escolheu: Hexadecimal\n'
          f'A sua versão hexadecimal é: {hex_convertion}!')
else: # caso a escolha não seja valida
    print('A escolha não é válida!')

# Exercise 38: Escreva um programa que leia DOIS números inteiros e compare-os
# mostrrando na tela uma mensagem:
# O primeiro valor é maior
# O Segundo valor é maior
# Não existem valores maiores.
num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))

if num1 > num2:
    print(f'O primeiro número "{num1}" é maior que o segundo número: {num2}!')
elif num1 < num2:
    print(f'O segundo número {num2} é maior que o primeiro número: {num1}!')
else:
    print('Não existem valores maiores, os dois números são iguais!')

# Exercise 39: Leia o Ano de Nascimento de um jovem e informe:
# Se ele AINDA vai se alistar, se é hora de se alistar ou se já passou do tempo de alistamento;
# Deve mostrar o tempo que falta ou que passou do prazo
from math import ceil
enlistment_days = 6570
user_age = float(input('Insira a idade: '))
age_in_days = user_age * 365
enlist_diff = age_in_days - enlistment_days

if age_in_days >= enlistment_days: # ve se o usuário ja pode se alistar
    if enlist_diff >= 365:
        diff_year = enlist_diff / 365 #divide o resultado para apresentar em anos!
        print(f'Você já deveria ter se alistado! A diferença é de aproximadamente {diff_year:.0f} ano(s)')
    else:
        print(f'Você já deveria ter se alistado! A diferença é de aproximadamente {ceil(enlist_diff)} dias!') #ceil pois o dia já é descontado e não pode ser feito no mesmo!
else:
    days_to_go = -enlist_diff
    year_to_go = days_to_go / 365
    print(f'Você ainda não precisa se alistar! Faltam aproximadamente {ceil(days_to_go):.0f} dias ou {year_to_go:.0f} anos!')

# Exercise 40: Leia duas notas de um aluno e calcule sua média mostrando uma mensagem final:
# Menos que 5.0 - reprovado, Média entre 5.0 e 5.9: Rec e + que 7 aprovado
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))

if nota1 < 0 or nota1 > 10:
    print('Primeira nota inválida! Deve estar entre 0 e 10.')
elif nota2 < 0 or nota2 > 10:
    print('Segunda nota inválida! Deve estar entre 0 e 10.')
else:
    media = (nota1 + nota2) / 2

    if media >= 7:
        print(f'Aprovado!\nSua média foi {media:.1f}')
    elif media >= 5:
        print(f'Recuperação!\nSua média foi {media:.1f}')
    else:
        print(f'Reprovado!\nSua média foi {media:.1f}')

# Exercise 41: Leia o nascimento de um atleta e mostre sua categoria, de acordo com a idade:
from datetime import date
actual_year = date.today().year

birth_year = int(input('Insira seu ano de nascimento: '))
if birth_year < 1900 or birth_year > actual_year:
    print('A data não é válida!')
else:
    age = actual_year - birth_year
    if age <= 9:
        print(f'Com {age} anos, sua categoria é MIRIM')
    elif age <= 14:
        print(f'Com {age} anos, sua categoria é INFANTIL')
    elif age <= 19:
        print(f'Com {age} anos, sua categoria é JUNIOR')
    elif age <= 25:
        print(f'Com {age} anos, sua categoria é SÊNIOR')
    else:
        print(f'Com {age} anos, sua categoria é MASTER')

# Exercise 43: Leia o peso e a altura de uma pessoa e calcule seu IMC, mostre status na tabela:
# - de 18.5: abaixo do peso, entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso, 30 até 40: obesidade e acima de 40: obesidade mórbida

weight = float(input('Insira o seu peso (kg): '))
height_cm = float(input('Insira a sua altura (cm): '))

height_m = height_cm / 100
imc = weight / (height_m ** 2)

print(f'Seu IMC é {imc:.1f}')

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc < 25:
    print('Você está no peso ideal!')
elif imc < 30:
    print('Você está em sobrepeso!')
elif imc < 40:
    print('Você está em obesidade!')
else:
    print('Você está em obesidade mórbida!')

# Exercise 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

# Input de valor
price = float(input('Insira o valor do produto: R$ ').replace(',', '.'))
# Gera o menu de seleção

if price > 0:
    method = int(input('1 - Dinheiro ou Cheque 10% OFF\n'
                       '2 - CC 1x 5% OFF\n'
                       '3 - CC 2x SEM DESCONTO\n'
                       '4 - CC 3x 20% de juros\n'
                       'Qual forma de pagamento? '))
    if method == 1:
        cash_payment = price - (price * 0.1)  # Á vista no dinheiro (-10%)
        print(f'Pagamento á vista: R$ {cash_payment:.2f} com 10% de desconto!')
    elif method == 2:
        cc_one = price - (price * 0.05)  # Á vista no cartão (-5%)
        print(f'CC - 1x: R$ {cc_one:.2f} com 5% de desconto!')
    elif method == 3:
        cc_two = price  # Preço comum (+0%)
        print(f'CC - 2x: R$ {cc_two:.2f} sem desconto!')
    elif method == 4:
        cc_three = price + (price * 0.2)  # Três vezes no cartão (+20%)
        print(f'CC 3x ou mais: R$ {cc_three:.2f} com 20% de juros!')
    else:
        print('Seleção não válida!')
elif price == 0:
    print('O produto será grátis! R$ 0')
else:
    print(f'O valor não pode ser negativo!')

# Exercise 45 - JO KEN PO
from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
pc = randint(0, 2)

print("""Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura
""")
try:
    user = int(input("Qual sua jogada? "))
except ValueError:
    print("Entrada inválida! Digite 0, 1 ou 2.")
    raise SystemExit

if user not in (0, 1, 2):
    print("Jogada inválida! Digite 0, 1 ou 2.")
    raise SystemExit

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)

print("-=" * 12)
print(f"Computador jogou {itens[pc]}")
print(f"Você jogou {itens[user]}")
print("-=" * 12)

if pc == user:
    print("EMPATE!")
elif (pc == 0 and user == 2) or (pc == 1 and user == 0) or (pc == 2 and user == 1):
    print("COMPUTADOR VENCEU!")
else:
    print("VOCÊ VENCEU!")