#Calcular el area de un círculo
"""formula area = pi * (r*r)"""

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def main():
    radio = float(input("Ingrese el radio: "))
    area = calcular_area_circulo(radio)
    print(f"El area del círculo es {area:.2f} unidades cuadradas")

main()