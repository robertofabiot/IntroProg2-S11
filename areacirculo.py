#Calcular el area de un círculo
"""formula area = pi * (r*r)"""

def calcular_area_circulo(radio):
    return 3.1416 * radio * radio

r = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es {calcular_area_circulo(r)} unidades cuadradas.")