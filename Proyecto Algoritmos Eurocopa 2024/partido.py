class Partido:
    def __init__(self, id, numero, equipo_local, equipo_visitante, fecha, grupo, estadio):
        self.id = id
        self.numero = numero
        self.equipo_local = equipo_local 
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha
        self.grupo = grupo
        self.estadio = estadio
        self.asistencia = 0 
        self.entradas_vendidas = []
        self.entradas_usadas = []
        self.asientos = [] # Matriz de asientos del estadio
        self.cantidad_entradas_vendidas = 0
        self.inicializar_asientos() # Inicializa la matriz de asientos
        
    def __str__(self):
        return f'Partido {self.numero}: {self.equipo_local.nombre} vs {self.equipo_visitante.nombre}\n     Fecha {self.fecha}\n     Grupo: {self.grupo}\n     Estadio: {self.estadio.nombre}'
    
    # Método para crear la matriz de asientos
    def inicializar_asientos(self):
        """
        Crea la distribucion de los asientos
        """
        self.asientos = [] # Crea una lista vacía para los asientos
        for fila in range(self.estadio.filas):
            fila_asientos = [] # Crea una lista vacía para una fila de asientos
            for asiento in self.estadio.columnas:
                fila_asientos.append(0) # Añade un asiento disponible (0) a la fila
            self.asientos.append(fila_asientos) # Añade la fila de asientos a la matriz de asientos
     
    # Método para mostrar el mapa de los asientos del estadio       
    def mostrar_asientos(self):
        """
        Llama a la funcion de mostrar asientos de Estadio
        """
        self.estadio.mostrar_asientos(self.asientos)
        
    # Método para seleccionar un asiento    
    def seleccionar_asiento(self):
        """
        Selecciona el asiento que el usuario ingrese
        """
        repetir = True
        while repetir:
            columnas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] # Columnas del estadio
            filas = self.estadio.total_asientos // 10 # Número total de filas del estadio
        
            # Solicita al usuario la letra de la columna del asiento que desea
            seleccion_columna = input("\nIngrese la letra del asiento (ej. A): ")
            
            while (not seleccion_columna.isascii()) or seleccion_columna.upper() not in columnas:
                print("\nError: Ingrese una opción válida (ej. A).")
                seleccion_columna = input("Ingrese la letra del asiento (ej. A): ")
                
            # Convierte la letra de la columna en un índice numérico
            columna = columnas.index(seleccion_columna.upper())

            # Solicita al usuario el número de la fila del asiento que desea    
            seleccion_fila = input("Ingrese el número del asiento (ej. 1): ")
            
            while (not seleccion_fila.isdigit()) or int(seleccion_fila) - 1 not in range(filas):
                print(f"\nError: Ingrese una número entre 1 y {self.estadio.filas}.")
                seleccion_fila = input("Ingrese el número del asiento (ej. 1): ")
            
            # Convierte la fila en un índice de la matriz
            seleccion_fila = int(seleccion_fila) - 1
                
            # Verifica si el asiento esta disponible
            seleccion_asiento = self.asientos[seleccion_fila][columna]
                
            if seleccion_asiento == 0:
                repetir = False
                print(f'\nUsted ha seleccionado el asiento "{seleccion_columna.upper()}{seleccion_fila + 1}" exitosamente.\n')
            elif seleccion_asiento == 1:
                print('\nAsiento ocupado. Por favor, seleccione otro.\n')
            
        return f'{seleccion_columna.upper()}{seleccion_fila + 1}', seleccion_fila, columna
    
    # Método para apartar el asiento
    def apartar_asiento(self, fila, columna):
        """
        Le cambia la disponibilidad al asiento que el usuario eligio
        """
        # Verifica de nuevo si el asiento esta disponible  
        seleccion_asiento = self.asientos[fila][columna]
         
        # Cambia el estado del asiento   
        if seleccion_asiento == 0:
            self.asientos[fila][columna] = 1