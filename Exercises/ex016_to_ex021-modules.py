# Exercise 16: Crie um programa que leia um número Real e mostre a sua porção inteira
# Ex: Digite um número: 6.127 - O número acima tem a parte inteira 6.
from math import floor
num = float(input('Digite um número real: '))
print(f'O número acima tem a parte inteira: {floor(num):.0f}')
#Poderia ter sido usado o MATH.TRUNC quer CORTARIA as casas decimais 1.23 == 1
#Poderia ter sido usado o int() para mostrar apenas a versão sem decimais - SEM IMPORTAR

# Exercise 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# Calcule e mostre o comprimento da hipotenusa:

# SEM A FUNÇÃO DE "HYPOT" que calcula automaticamente o teorema de pitágoras (a² + b² = c²)
from math import pow,sqrt, hypot
ca_oposto = float(input('Insira o CO: '))
ca_adj = float(input('Insira o CA: '))
hipo = sqrt(pow(ca_oposto, 2) + pow(ca_adj,2))

# Versão que utiliza a função "hypot" da livraria "MATH" do python (calcula automaticamente através da função)
hipo2 = hypot(ca_oposto, ca_adj)
print(f'A hipotenusa para CO: {ca_oposto:.1f} e CA: {ca_adj:.1f} é {floor(hipo):.1f} \n'
      f'Em sua versão alternativa, temos a hipoteusa como {hipo2:.3}')

# Exercise 18: Programa que lê um ângulo e mostra SEN, COS e TAN
# IMPORTANTE: As funções trigonométricas do Python (math.sin, math.cos, etc)
# trabalham com RADIANOS, não com GRAUS.
# Precisamos usar a função math.radians() para converter.

from math import cos, sin, tan, radians

ang = float(input('Insira um ângulo em graus: '))

# 2. Conversão de Graus para Radianos
rad = radians(ang)

cosine = cos(rad)
tang = tan(rad)
sine = sin(rad)

print(f'Para o ângulo de {ang:.1f}°:')
print(f'-> O Seno é: {sine:.2f}')
print(f'-> O Cosseno é: {cosine:.2f}')
print(f'-> A Tangente é: {tang:.2f}')
# --- RESULTADO ---
# Se você digitar 30 (graus), o Python faria o cálculo de 30 radianos.
# A função radians(ang) faz a conta: (ângulo * PI) / 180.
# EXPLICAÇÃO DO RESULTADO (Ângulo 180°):
# No círculo trigonométrico, o ângulo de 180° está exatamente à esquerda.

# 3. TANGENTE (Sen/Cos): -0.00
# Como Tangente = Seno / Cosseno -> 0 / -1 = 0.
# O sinal de "-" aparece por uma pequena imprecisão de arredondamento do Python ao lidar com o número PI.


#Exercise 19: Um professor quer sortear um dos seus 4 alunos para apagar o quadro;
#Faça um programa que ajude ele lendo o nome do escolhido:
from random import choice
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = choice(lista)
print(f'O aluno escolhido foi "{escolhido}"')
# EXERCÍCIO 19: Sorteio Simples
# A função 'choice' seleciona aleatoriamente um único elemento da lista.
# É ideal para quando você precisa de apenas um resultado (amostragem unitária).

#Exercise 20: O mesmo professor quer sortear a ordem de apresentação de trabalhos
# Crie um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista2 = [a1,a2,a3,a4]
shuffle(lista2)
print(f'A lista de alunos é {lista2}')
# EXERCÍCIO 20: Sorteio de Ordem
# A função 'shuffle' (embaralhar) reordena a lista original.
# Diferente da 'choice', ela altera a própria lista (operação in-place) e não retorna um novo valor.

# Exercise 21: Reproduza um MP3
from playsound import playsound
playsound("C:/Users/Augusto/Desktop/Music/Schranz/William Luck - IDGAF (Extended).wav")

