# ESTRUTURAS CONDICIONAIS (if / else)
# OBJETIVO
# Controlar o fluxo do programa com decisões lógicas.
# O código executa blocos diferentes dependendo de condições
# que resultam em True ou False.
#
# ------------------------------------------------------------
#
# ESTRUTURA BÁSICA
#
# if condição:
#     bloco executado se a condição for verdadeira
# else:
#     bloco executado se a condição for falsa
#
# A indentação DEFINE o bloco em Python.
#
# ------------------------------------------------------------
#
# OPERADORES DE COMPARAÇÃO
#
# >   maior que
# <   menor que
# >=  maior ou igual
# <=  menor ou igual
# ==  igual
# !=  diferente
#
# ------------------------------------------------------------
#
# EXEMPLOS PRÁTICOS
#
# Exemplo 1: idade
idade = int(input('Idade: '))
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')
#
# Exemplo 2: nota
nota = float(input('Nota: '))
if nota >= 7:
    print('Aprovado')
else:
    print('Reprovado')
#
# Exemplo 3: número positivo ou negativo
numero = int(input('Número: '))
if numero > 0:
    print('Positivo')
else:
    print('Negativo ou zero')
#
# ------------------------------------------------------------
#
# MODELO MENTAL
#
# Pense no if como uma pergunta SIM / NÃO:
# - Condição verdadeira → executa o if
# - Condição falsa → executa o else (se existir)
#
# O programa escolhe apenas UM caminho.
#
# ------------------------------------------------------------
#
# ERROS COMUNS
#
# 1) Confundir = com ==
# 2) Indentação errada quebrando a lógica
# 3) Achar que if repete código (if NÃO é loop)
#
# ------------------------------------------------------------
#
# RESUMO
#
# - if / else controlam decisões
# - condições sempre retornam True ou False
# - indentação é parte da lógica
# - programar é transformar regras em decisões
