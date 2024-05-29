from funcoes import *

pc_carbono = float(input("Informe o percentual de carbono do aço: "))
dureza_rockwell = float(input("Informe a dureza da rockwell do aço: "))
resistencia = float(input("Informe a resistência a pressão do aço: "))

grau = calcular_grau_aco(pc_carbono, dureza_rockwell, resistencia)

print(f'O grau do aço é: {grau}')
