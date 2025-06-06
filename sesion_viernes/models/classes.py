class Product:
    def _init_(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def _str_(self):
        return f"Nombre: {self.name} \nPrecio: {self.price} \nExistencia: {self.stock}"
