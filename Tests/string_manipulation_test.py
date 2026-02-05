# Uso do len()
text = input('Insira uma string: ')
print(f'Quantas caracteres? (len): {len(text)}')

# Uso do .count() para contar as letras 'o'
print(text.count('o'))

# Uso do .find() - Retorna a POSIÇÃO da memória, se não houver, o resultado é '-1'
print(text.find('gal'))

# Uso do 'in' - Retorna um valor BOOLEANO - True or False
print('gal' in text)

# Uso do .strip() - limpa os espaços direito e esquerdo
print(text.strip())
# Uso do .lstrip() e .rstrip() removem do lado esquerdo OU direito
print(text.lstrip())
print(text.rstrip())

# Uso do replace(x,y)
text = text.replace('gal', 'lindo')
print(text)

# Uso do .upper() e .lower()
print(text.upper())
print(text.lower())

# Uso do  title() e capitalize()
print(f'Title: {text.title()}')
print(f'Capitalize: {text.capitalize()}')

# Uso do .split()
print(text.split())

# Uso do .join()
'-'.join(text)
print(text)
