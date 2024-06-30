class Cliente:
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.es_vip = False
        self.asientos = [] 
        self.cuenta = 0
        self.n_entradas_compradas = 0
        self.entradas_compradas = []
        
    def __str__(self):
       return f'Nombre: {self.nombre}, Cedula: {self.cedula}, Edad: {self.edad}'
    
    