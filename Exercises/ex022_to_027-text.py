# Exercise 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# Nome com todas as letras maiúsculas
# Nome com todas minúsculas
# Quantas letras ao todo
# Quantas letras tem o primeiro nome
nome_usuario = str(input('Insira o nome completo: ')).strip()
# len() mede o total; count(' ') conta os espaços; a subtração dá o total de letras reais
nome_total = len(nome_usuario) - nome_usuario.count(' ')
# O método .upper() cria uma nova versão do texto com todas as letras em maiúsculas
nome_up = nome_usuario.upper()
# O método .lower() cria uma versão do texto com todas as letras em minúsculas
nome_down = nome_usuario.lower()
# O método .split() fatia a string onde houver espaços e guarda os pedaços em uma lista (gaveteiro)
lista = nome_usuario.split()
# Acessa a primeira "gaveta" (índice 0) da lista para isolar o primeiro nome
first = lista[0]
# Usa a função len() especificamente no objeto 'first' para contar a suas letras
first_num = len(lista[0])

print(f'Seu nome tem {nome_total} caracteres \n'
      f'Maiúsculas: {nome_up}\n'
      f'Minúsculas: {nome_down}\n'
      f'Primeiro nome: {first} tem {first_num} letras.')

# Exercise 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
numero = int(input("Digite um número de 0 a 9999: "))

# A lógica do fatiamento matemático:
# 1. // (Divisão Inteira) remove as casas que não queremos à direita.
# 2. % (Módulo 10) isola o último dígito que sobrou.

unidade = numero // 1 % 10
dezena  = numero // 10 % 10
centena = numero // 100 % 10
milhar  = numero // 1000 % 10

# Exibição formatada com F-Strings
print(f'Analisando o número {numero}:')
print(f'Unidade: {unidade}')
print(f'Dezena:  {dezena}')
print(f'Centena: {centena}')
print(f'Milhar:  {milhar}')

# Exercise 24: Versão Corrigida e PEP 8
cidade = str(input("Digite o nome da cidade: ")).strip()
# A variável 'resultado' aqui já é um booleano (True ou False)
comeca_com_santo = cidade[:5].upper() == 'SANTO'
print(f'Analisando a cidade: {cidade}')
if comeca_com_santo:
    print('Sim, a cidade começa com SANTO.')
else:
    print('Não, a cidade não começa com SANTO.')

# Exercise 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
name1 = str(input('Insira o seu nome: ').upper().strip())
if 'SILVA' in name1:
    print(f'O nome {name1} possui "SILVA"!')
else:
    print('"SILVA" não existe no nome solicitado!')

# Exercise 26: Leia uma frase e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a PRIMEIRA vez
# Em que posição aparece a ÚLTIMA vez
frase = str(input('Escreva uma frase: ').upper().strip())
nmbr = frase.count('A')
first_a = frase.find('A') + 1 # O "+1" Serve para não retornar a posiçao "0" no índice para o usuário
last_a = frase.rfind('A') + 1
print(f'A frase contém {nmbr} repetições de "A".\n'
      f'A primeira aparição de "A" é {first_a} no índice.\n'
      f'A última aparição de "A" é {last_a} no índice.')

# Exercise 27: Leia o nome completo de uma pessoal, mostre o primeiro e o último nome separadamente
name2 = str(input('Insira o nome: ').title().strip())
splitt = name2.split()
f_name = splitt[0]
l_name = splitt[-1] # O número negativo procura na lista DE TRÁS PARA FRENTE (-1 == último, -2 == penúltimo)
print(f'Para o nome {name2}: \n'
      f'Primeiro nome: {f_name}\n'
      f'Último nome: {l_name}')