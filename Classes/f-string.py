nome = input("Qual seu nome? ")

#A f-string (:20) após a escrita, adiciona 20 espaços após a entrada de texto!
print(f'Prazer em te conhecer {nome:20}!') #Output: Prazer em te conhecer gal                 !

#A f-string (:>20) com > após a escrita, alinha o texto à direita (>) ou a Esquerda (<)
print(f'Prazer em te conhecer {nome:>20}!') #Output: Prazer em te conhecer                  gal!
print(f'Prazer em te conhecer {nome:<20}!') #Output: Prazer em te conhecer gal                 !

#A f-string (:^20) com ^ após a escrita, alinha o texto ao centro (^)
print(f'Prazer em te conhecer {nome:^20}!') #Output: Prazer em te conhecer         gal         !

# Adiciondo '=' após os dois pontos (:=20):
print(f'Prazer em te conhecer: {nome:=^20}') #Output: Prazer em te conhecer ==========gal==========!

#Usos do f-string: Limitar
print('Divisão de dois números:')
num1 = float(input('Adicione um número:'))
num2 = float(input('Adicione outro número:'))
numfloat = num1 / num2
# A f-string (:.3f) pode ser usada para limita as casas decimais a 3.
print(f'O resultado é:{numfloat:.3f}') # Output: 0.625

#Usos do f-string: Somar 2 prints
print(f'O resultado é', end=' ')
print('tudo que você quiser') #Output: 'O resultado é tudo que você quiser'
# O (END=' ') funciona para "concatenar os dois prints exemplificados" acima
# Você pode adicionar qualquer símbolo entre as aspas '' do END

# Ao contrário, para QUEBRAR uma linha devemos adicionar (\n)
print(f'O resultado é: \n{numfloat:.1f}')