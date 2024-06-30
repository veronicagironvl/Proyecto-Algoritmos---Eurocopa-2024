class Restaurante:
    def __init__(self, nombre, productos):
        self.nombre = nombre 
        self.productos = productos # Lista de productos
            
    def __str__(self):
        return f'Restaurante: {self.nombre}'
