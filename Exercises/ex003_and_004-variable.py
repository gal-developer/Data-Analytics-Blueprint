#Exercício3: Faça um algoritimo que some dos números com a entrada de usuário e exiba para o cliente
num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))
soma = int(num1 + num2)
# Aqui, a f-string .format() é utilizada para adicionar as variáveis em ordem dentro da string de exibição (print)
print('A soma do número {} e {} é {}!'.format(num1, num2, soma))

#Exercício 4: teste para saber o tipo de variavel (str, int, float, bool)
#n1 = input('Digite o valor: ')
#print(type(n1))

letter = input('Digite algo: ')
print('o tipo primitivo é: {}'.format(letter.isnumeric()))
print('o tipo primitivo é: {}, é um espaço? {} '.format(letter.isnumeric(),letter.isspace()))

# EXPLICAÇÃO DO CÓDIGO:
# 1.A frase 'o tipo primitivo é: {}' é uma string com um espaço reservado {}.
# 2.O método .format() deve vir logo após o fechamento das aspas da string.
# 3.Dentro do .format(), chamamos a.isnumeric() para testar se 'a' é um número.
# 4.O resultado desse teste (True ou False) é enviado para o par de chaves {}.
# 5.Todo esse conjunto deve estar dentro dos parênteses do print() para ser exibido.
