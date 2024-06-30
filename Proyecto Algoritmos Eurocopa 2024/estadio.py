class Estadio:
    def __init__(self, id, nombre, ciudad, capacidad_general, capacidad_vip, restaurantes):
        self.id = id
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad_general = capacidad_general
        self.capacidad_vip = capacidad_vip
        self.total_asientos = capacidad_general + capacidad_vip # Cálculo del total de asientos
        self.columnas = "ABCDEFGHIJ" # Letras que representan las columnas del estadio
        self.filas = self.total_asientos // 10 # Número total de filas (tomando 10 columnas por fila)
        
        
        # Lista de objetos de restaurantes dentro del estadio
        self.restaurantes = restaurantes 
        
    def __str__(self):
        return f'{self.nombre} en {self.ciudad} - {self.capacidad_general} entradas general y {self.capacidad_vip} entradas VIP'
       
    # Método para mostrar el mapa de asientos del estadio    
    def mostrar_asientos(self, asientos):  
        """
        Imprime los asientos del estadio seleccionado
        """
                      
        print(f'Mapa de asientos del {self.nombre} **\n')
        
        # Imprime el encabezado de las columnas
        print('   ', end=' ')
        for columna in self.columnas:
            print (f'{columna}', end = ' ')
        print()
        
        numero_fila = 0 # Inicialización del contador de filas
       
        # Imprime las filas de asientos
        for fila in asientos:
            numero_fila += 1 # Incrementa el número de fila
            print(f'{numero_fila:>3}', end= ' ') # Imprime el número de fila
            for asiento in fila:
                # Imprime 'O' si el asiento está desocupado, 'X' si está ocupado
                if asiento == 0:
                   print('O', end=' ')
                else:
                   print('X', end=' ')
            print()
