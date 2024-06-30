import random
import string

class Entrada:
    def __init__(self, tipo_entrada, precio, partido, asiento, cliente):
        self.id = ' '
        self.tipo_entrada = tipo_entrada
        self.precio = precio
        self.partido = partido
        self.asiento = asiento
        self.cliente = cliente
        
        
    def __str__(self):
        plantilla_entrada = (
            "----------------------------------------\n"
            "|              ENTRADA                 |\n"
            "----------------------------------------\n"
            "| ID: {:>32} |\n"
            "| Tipo de entrada: {:>20}|\n"
            "| Precio: {:>28} |\n"
            "| Partido: {:>27} |\n"
            "| Asiento: {:>27} |\n"
            "----------------------------------------\n"
        )
        return plantilla_entrada.format(self.id, self.tipo_entrada, f"${self.precio:.2f}", self.partido, self.asiento)
    
    # Método para generar un ID único para la entrada
    def generar_id_entrada(self, entradas_vendidas):
        """
        Genera un codigo unico para la entrada 
        """
        
        opciones = string.ascii_uppercase + string.digits
        
        id_entrada = ''
        
        # Genera un id de 8 caracteres aleatorios
        for i in range(8):
            id_entrada += random.choice(opciones)
        
        duplicado = True
        # Verifica si el id ya existen en las entradas vendidas de ese partido
        while duplicado:
            duplicado = False
            for entrada in entradas_vendidas:
                if id_entrada == entrada.id:
                    duplicado = True
                    id_entrada = ''
                    for i in range(8):
                        id_entrada += random.choice(opciones)  
            
            
        self.id = id_entrada
        
        return self.id
    