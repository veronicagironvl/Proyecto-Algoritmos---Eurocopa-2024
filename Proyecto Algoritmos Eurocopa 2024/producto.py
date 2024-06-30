class Producto:
    def __init__(self, nombre, quantity, precio, stock):
        self.nombre = nombre
        self.quantity = quantity 
        self.precio = precio
        self.stock = stock
        self.vendidos = 0
            
    def __str__(self):
        return (f"Producto: {self.nombre}, Cantidad: {self.quantity}, Precio: {self.precio}, "
                f"Stock: {self.stock}, Vendidos: {self.vendidos}")
    
    
class Comida(Producto):
    def __init__(self, nombre, quantity, precio, stock, tipo):
        super().__init__(nombre, quantity, precio, stock)
        self.tipo = tipo

    def __str__(self):
        return (super().__str__() +
                f", Tipo: {self.tipo}")
    
class Bebida(Producto):
    def __init__(self, nombre, quantity, precio, stock, tipo):
        super().__init__(nombre, quantity, precio, stock)
        self.tipo = tipo
        
    def __str__(self):
        return (super().__str__() +
                f", Tipo: {self.tipo}")