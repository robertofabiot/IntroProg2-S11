import models.classes as c
import dao.functions as f

productos = f.ProductDao()

def menu():
    print("""
        1. Agregar
        2. Mostrar
        6. Salir
        Digite una opción:
    """)

def main():
    while(True):
        menu()
        option = input()
        if option == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            existencia = int(input("Existencia: "))
            producto = c.Product(nombre, precio, existencia)
            productos.add(producto)

        elif option == "2":
            print("Productos")
            productos.show()
        elif option == "6":
            print("Adios")
            False
            break
        else: 
            print("Opción inválida")
