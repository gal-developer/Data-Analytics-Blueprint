from math import floor
# Inputs de info e cálculo
programa_pontos = input("Qual seu programa de pontos? (Esfera, Livelo, Avios): ")
milheiro_avios = float(input("Qual valor em (R$) do milheiro? "))
real_gasto = float(input("Qual valor em (R$) deseja converter? "))
eqv_pontos = float(input("Qual a equivalência de pontuação?: "))
promo = int(input("Qual valor (%) do desconto? "))
# Cálculos
desconto = milheiro_avios - ((milheiro_avios / 100 ) * promo) # Desconto milheiro
print(f"O valor do milheiro com {promo:.0f}% de desconto é R${desconto:.2f}")
pontos_total = (real_gasto / desconto) * 1000
eqv_programa = pontos_total / eqv_pontos
print(f"O valor convertido de pontos {programa_pontos} equivalem a: {floor(eqv_programa):.0f} milhas")






