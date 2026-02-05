# MASTER FILE: MANIPULAÇÃO DE STRINGS (AULA 09 + MERCADO)
frase = "  Python é a Linguagem do Futuro!  "

# 1. ANÁLISE (Descobrindo dados sobre a String)
print(f"Comprimento: {len(frase)}")          # len(): Conta todos os caracteres (incluindo espaços)
print(f"Contagem de 'a': {frase.count('a')}") # count(): Frequência de um caractere específico
print(f"Onde está 'Futuro': {frase.find('Futuro')}") # find(): Índice inicial (retorna -1 se não existir)
print(f"Existe 'Python'?: {'Python' in frase}")    # in: Operador lógico que retorna True/False

# 2. LIMPEZA (Trimming)
# strip(): Essencial para tratar inputs de usuários
print(f"Sem espaços nas pontas: '{frase.strip()}'")

# 3. TRANSFORMAÇÃO (Estética)
print(f"Tudo Maiúsculo: {frase.upper()}")      # upper(): Caixa ALTA
print(f"Tudo Minúsculo: {frase.lower()}")      # lower(): caixa baixa
print(f"Só a primeira letra: {frase.capitalize()}") # capitalize(): Apenas o primeiro char da string
print(f"Título de Livro: {frase.title()}")     # title(): Primeira letra de CADA palavra

# 4. EDIÇÃO (Replacing)
# replace(): Substitui um trecho por outro (não altera a original, gera uma nova)
nova_frase = frase.replace("Futuro", "Presente")
print(f"Frase Editada: {nova_frase.strip()}")

# 5. ESTRUTURA (Divisão e Junção)
palavras = frase.strip().split() # split(): Transforma a string em uma LISTA de palavras
print(f"Lista de Palavras: {palavras}")
print(f"Primeira palavra: {palavras[0]}") # Acessando o primeiro item da lista gerada

junto = "-".join(palavras) # join(): Une a lista novamente usando um separador
print(f"Frase com traços: {junto}")

# 6. FATIAMENTO (Slicing Avançado)
# [start : stop : step]
# Lembre-se: o 'stop' é EXCLUSIVO (não entra no resultado)
texto = "Curso de Python"
print(f"Fatiar (0 a 5): {texto[0:5]}")    # 'Curso'
print(f"Pular de 2 em 2: {texto[0:15:2]}") # 'Crod yhn'
print(f"Inverter String: {texto[::-1]}")   # O truque do step -1

# 7. VALIDACAO (Is-Methods)
# Úteis para garantir que o código não quebre ao converter tipos
numero = "123"
print(f"É numérico?: {numero.isnumeric()}") # True
print(f"É alfabético?: {numero.isalpha()}") # False (contém números)

# ============================================================
# Lembre-se que Strings são imutáveis!
# Se você quiser que a 'frase' mude de verdade, faça:
# frase = frase.strip().upper()
# ============================================================