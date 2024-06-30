import matplotlib.pyplot as plt

#################### Modulo Indicadores de gestión (Estadísticas) ####################
    
def ver_estadisticas(clientes, partidos, estadios):
    """
    Función para ver todas las estadísticas    
    """

    while True:
        
        print('\n**** ESTADÍSTICAS DE LA EUROCOPA 2024 ****\n')
        # Lista de opciones de estadísticas disponibles
        opciones =  ['Promedio de gasto de clientes VIP', 'Partido(s) con mayor asistencia', 'Partido(s) con mayor venta de entradas', 'Tabla de asistencias a los partidos', 'Top 3 productos más vendidos', 'Top 3 clientes', 'Promedio de gasto de clientes VIP (Graficos)', 'Partido(s) con mayor asistencia (Graficos)', 'Partido(s) con mayor venta de entradas (Graficos)', 'Tabla de asistencias a los partidos (Graficos)', 'Regresar al menú principal']
        
        for index, opcion in enumerate(opciones):
            print(f'{index + 1}. {opcion}')
            
        seleccion_opcion = input('\nIngrese el número de la estadística que desea ver: ')
        
        while (not seleccion_opcion.isdigit()) or (int(seleccion_opcion) - 1 not in range(len(opciones))):
            print('Error: Ingrese una opción válida.')
            seleccion_opcion = input('\nIngrese el número de la estadística que desea ver: ')
            
        seleccion_opcion = int(seleccion_opcion) - 1
        
        if seleccion_opcion == 0:
            promedio_gasto_cliente_vip(clientes)
        elif seleccion_opcion == 1:
            partido_mayor_asistencia(partidos)
        elif seleccion_opcion == 2:
            partido_mayor_venta_entradas(partidos)
        elif seleccion_opcion == 3:
            tabla_asistencia_partidos(partidos)
        elif seleccion_opcion == 4:
            top_tres_productos(estadios)
        elif seleccion_opcion == 5:
            top_tres_clientes(clientes)
        elif seleccion_opcion == 6:
            grafico_promedio_gasto_vip(clientes)
        elif seleccion_opcion == 7:
            grafico_partido_mayor_asistencia(partidos)
        elif seleccion_opcion == 8:
            grafico_partido_mayor_venta_entradas(partidos)
        elif seleccion_opcion == 9:
            grafico_tabla_asistencia_partidos(partidos)
        elif seleccion_opcion == 10:
            break # Sale del bucle y regresa al menú principal
   
def promedio_gasto_cliente_vip(clientes):
    """
    Función para calcular el promedio de gastos de un cliente vip       
    """
    
    # Inicializa las variables para el cálculo del gasto total y el promedio
    gasto_total_clientes = 0
    cantidad_total_clientes = 0
    promedio_gasto_vip = 0
    clientes_vip = []
    
    # Ordenar la lista de clientes según quién ha gastado más
    clientes.sort(key=lambda cliente: cliente.cuenta, reverse=True)
    
    # Agrega los cliente VIP a una nueva lista
    clientes_vip.clear()
    for cliente in clientes:
        if cliente.es_vip:
            clientes_vip.append(cliente)
    
    print('\n**** ESTADÍSTICAS DE LA EUROCOPA 2024 ****\n')
      
    # Verifica si hay clientes vip registrados  
    if not clientes_vip:   
        print('\nNo hay clientes VIPs registrados.')
        return
    
    #Calcula el gasto total y la cantidad total de clientes vip
    for cliente in clientes_vip:
        cantidad_total_clientes += 1
        gasto_total_clientes += cliente.cuenta
       
    #Calcula y muestra el promedio 
    promedio_gasto_vip = gasto_total_clientes / cantidad_total_clientes
    print(f'El promedio de gasto de un cliente VIP es ${promedio_gasto_vip:.2f}')

def tabla_asistencia_partidos(partidos):
    """
    Función para mostrar la tabla de asistencia a los partidos
    """
    
    # Ordena la lista de partidos según asistencia
    partidos.sort(key=lambda partido: partido.asistencia, reverse=True)
    
    print('\n**** TABLA DE ASISTENCIAS DE LA EUROCOPA 2024 ****\n')
    
    # Itera sobre cada partido y muestra la su información del partido
    for partido in partidos:
        print(f' - Partido {partido.numero}: {partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre}')
        print(f'     Estadio: {partido.estadio.nombre}')
        print(f'     Asistencia: {partido.asistencia} persona(s)')
        print(f'     Cantidad de entradas vendidas: {partido.cantidad_entradas_vendidas}')
       
        # Calcula la relación asistencia/venta
        if partido.asistencia > 0 and partido.cantidad_entradas_vendidas > 0:
            relacion_asistencia_venta = partido.asistencia / partido.cantidad_entradas_vendidas
        else: 
            relacion_asistencia_venta = 0
         
        # Mostrar la relación asistencia/venta calculada       
        print(f'     Relación asistencia/venta: {relacion_asistencia_venta}')
        print('')

def partido_mayor_asistencia(partidos):
    """
    Función para verificar y mostrar el partido con mayor asistencia
    """

    # Inicializa variables para el cálculo del partido con mayor asistencia
    mayor_asistencia = 0
    partidos_mayor_asistencia = []

    # Iterar sobre todos los partidos para encontrar los que tienen la mayor asistencia
    for partido in partidos:
        if partido.asistencia > mayor_asistencia and partido.asistencia != 0:
            # Si encuentra un partido con mayor asistencia, actualiza la lista
            mayor_asistencia = partido.asistencia
            partidos_mayor_asistencia.clear() # Limpia la lista para incluir solo el partido con la mayor asistencia
            partidos_mayor_asistencia.append(partido)
        elif partido.asistencia == mayor_asistencia and partido.asistencia != 0:
            # Si hay un empate en la mayor asistencia, agrega el partido a la lista
            partidos_mayor_asistencia.append(partido)
    
    print('\n**** ESTADÍSTICAS DE LA EUROCOPA 2024 ****\n')
            
    # Verifica si se encontraron partidos con la mayor asistencia
    if partidos_mayor_asistencia:
        # Si hay solo un partido con la mayor asistencia, imprime su información
        if len(partidos_mayor_asistencia) == 1:
            for partido in partidos_mayor_asistencia:
                print(' El partido con mayor asistencia de la Eurocopa 2024 es...')
                print(f'  Partido {partido.numero}: {partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre} con {partido.asistencia} asistente(s).')
        # Si hay varios partidos con la mayor asistencia (empate), imprime la información de cada uno
        elif len(partidos_mayor_asistencia) > 1:
            print('    Hubo un empate! Los partidos con mayor asistencia de la Eurocopa 2024 son...')
            for partido in partidos_mayor_asistencia:
                print(f'    - Partido {partido.numero}: {partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre} con {partido.asistencia} asistente(s).')
    else:
        print('Ups! Parece que nadie ha asistido a los partidos aún.')

def partido_mayor_venta_entradas(partidos):
    """ 
    Función para verificar y mostrar el partido con mayor venta de entradas
    """

    # Inicializa las variables
    mayor_venta = 0
    partidos_mayor_venta_entradas = []
    
    # Recorre la lista de partidos para encontrar el partido con la mayor venta de entradas
    for partido in partidos:
        # Verifica si la cantidad de entradas vendidas del partido actual es mayor que la mayor venta registrada hasta ahora
        if partido.cantidad_entradas_vendidas > mayor_venta and partido.cantidad_entradas_vendidas != 0:
            mayor_venta = partido.cantidad_entradas_vendidas # Actualiza la mayor venta encontrada
            partidos_mayor_venta_entradas.clear() # Limpia la lista de partidos con mayor venta (solo se guarda el último máximo)
            partidos_mayor_venta_entradas.append(partido) # Agrega el partido actual a la lista de mayor venta
        # Si hay un empate en la cantidad de entradas vendidas, agrega el partido a la lista
        elif partido.cantidad_entradas_vendidas == mayor_venta and partido.cantidad_entradas_vendidas != 0:
            partidos_mayor_venta_entradas.append(partido)
    
    print('\n**** ESTADÍSTICAS DE LA EUROCOPA 2024 ****\n')

    # Verifica si se encontraron partidos con mayor venta de entradas
    if partidos_mayor_venta_entradas:
        # Si hay un solo partido con la mayor venta
        if len(partidos_mayor_venta_entradas) == 1:
            for partido in partidos_mayor_venta_entradas:
                print(' El partido con mayor venta de entradas de la Eurocopa 2024 es...')
                print(f'  Partido {partido.numero}: {partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre} con {partido.cantidad_entradas_vendidas} entrada(s) vendida(s)') 
        # Si hay varios partidos con la misma mayor venta de entradas
        elif len(partidos_mayor_venta_entradas) > 1:
            print('   Hubo un empate! Los partidos con mayor venta de entradas de la Eurocopa 2024 son...')
            for partido in partidos_mayor_venta_entradas:
                print(f'     - Partido {partido.numero}: {partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre} con {partido.cantidad_entradas_vendidas} entrada(s) vendida(s)')   
    else:
        # Si no se encontraron partidos con ventas de entradas
        print('\nUps! Parece que nadie ha comprado entradas para los partidos aún.')

def top_tres_productos(estadios):   
    """ 
    Función para calcular los top 3 productos de cada restaurante
    """

    # Ordena los productos de cada restaurante por la cantidad vendida
    for estadio in estadios:
        for restaurante in estadio.restaurantes: 
            restaurante.productos.sort(key=lambda producto: producto.quantity, reverse=True)
    
    print('\n**** TOP 3 PRODUCTOS DE CADA RESTAURANTE ****\n')
    
    # Itera sobre cada estadio y sus restaurantes para mostrar los productos más vendidos        
    for estadio in estadios:
        for restaurante in estadio.restaurantes:
            print(f'\n  * Restaurante {restaurante.nombre}  ')
            for index, producto in enumerate(restaurante.productos[:3]): 
                print(f'    - Número {index + 1}: {producto.nombre} (historico vendido: {producto.quantity})')

def top_tres_clientes(clientes):
    """
    Función para calcular los top 3 clientes            
    """
    
    # Ordena la lista de clientes por el número de entradas compradas
    clientes.sort(key=lambda cliente: cliente.n_entradas_compradas, reverse=True)
    
    # Lista para almacenar los top 3 clientes
    top_clientes = []
    
    print('\n**** TOP 3 CLIENTES DE LA EUROCOPA 2024 ****\n')
    
    # Itera sobre los primeros 3 clientes con más entradas compradas y los añade a top_clientes
    for cliente in clientes[:3]:
        if cliente.n_entradas_compradas > 0:
            top_clientes.append(cliente)
        
    # Verifica si se encontraron clientes para mostrar en el top 3
    if top_clientes:    
        for index, cliente in enumerate(top_clientes):
            print(f'   - Número {index + 1}: {cliente.nombre} con {cliente.n_entradas_compradas} entrada(s) comprada(s)') 
    else:
        print('No hay top 3 clientes porque no se han vendido entradas para ningún partido aún.')

def grafico_promedio_gasto_vip(clientes):
    """
    Funcion para mostrar el promedio de gasto de los clientes vip con graficos
    """
    
    # Inicializa las variables para el cálculo del gasto total y el promedio
    gasto_total_clientes = 0
    cantidad_total_clientes = 0
    promedio_gasto_vip = 0
    clientes_vip = []
    
    # Ordena la lista de clientes según quién ha gastado más
    clientes.sort(key=lambda cliente: cliente.cuenta, reverse=True)
    
    # Agrega los clientes VIP a una nueva lista
    clientes_vip.clear()
    for cliente in clientes:
        if cliente.es_vip:
            clientes_vip.append(cliente)
    
    # Verifica si hay clientes VIP registrados  
    if not clientes_vip:   
        print('\nNo hay clientes VIPs registrado en este partido.')
        return
    
    # Calcula el gasto total y la cantidad total de clientes VIP
    for cliente in clientes_vip:
        cantidad_total_clientes += 1
        gasto_total_clientes += cliente.cuenta
       
    # Calcula el promedio 
    promedio_gasto_vip = gasto_total_clientes / cantidad_total_clientes
    
    # Crea el gráfico
    fig, ax = plt.subplots()
    ax.bar('Promedio de Gasto VIP', promedio_gasto_vip, color='blue')
    ax.set_ylabel('Dinero gastado ($)')
    ax.set_title('Promedio de Gasto de Clientes VIP')
    ax.grid(True)
    
    # Muestra el gráfico
    plt.tight_layout()
    plt.show()
    
def grafico_partido_mayor_asistencia(partidos):
    """
    Funcion para generar el grafico del partido con mayor asistencia
    """
    # Inicializa las variables para el cálculo del partido con mayor asistencia
    mayor_asistencia = 0
    partidos_mayor_asistencia = []

    # Itera sobre todos los partidos para encontrar los que tienen la mayor asistencia
    for partido in partidos:
        if partido.asistencia > mayor_asistencia and partido.asistencia != 0:
            mayor_asistencia = partido.asistencia
            partidos_mayor_asistencia.clear()
            partidos_mayor_asistencia.append(partido)
        elif partido.asistencia == mayor_asistencia and partido.asistencia != 0:
            partidos_mayor_asistencia.append(partido)
    
    # Crea el gráfico
    fig, ax = plt.subplots()
    
    # Verifica si se encontraron partidos con la mayor asistencia
    if partidos_mayor_asistencia:
        # Si hay solo un partido con la mayor asistencia, lo muestra en el gráfico
        if len(partidos_mayor_asistencia) == 1:
            partido = partidos_mayor_asistencia[0]
            ax.bar(f'Partido {partido.numero}', partido.asistencia, color='blue')
            ax.text(f'Partido {partido.numero}', partido.asistencia + 500, f'{partido.asistencia} asistentes', ha='center')
        # Si hay varios partidos con la mayor asistencia (empate), los muestras todos en el gráfico
        elif len(partidos_mayor_asistencia) > 1:
            for partido in partidos_mayor_asistencia:
                ax.bar(f'Partido {partido.numero}', partido.asistencia, color='blue')
                ax.text(f'Partido {partido.numero}', partido.asistencia + 500, f'{partido.asistencia} asistentes', ha='center')
        
        ax.set_ylabel('Cantidad de Asistentes')
        ax.set_title('Partido(s) con Mayor Asistencia - Eurocopa 2024')
        ax.grid(True)
        plt.xticks(rotation=45, ha='right')
    else:
        ax.text(0.5, 0.5, 'Ups! Parece que nadie ha asistido a los partidos aún.', ha='center', va='center', transform=ax.transAxes)
        ax.axis('off')

    # Muestra el gráfico
    plt.tight_layout()
    plt.show()
    
def grafico_partido_mayor_venta_entradas(partidos):
    """
    Funcion para generar el grafico del partido con mayor venta de entradas    

    """
    # Inicializa las variables
    mayor_venta = 0
    partidos_mayor_venta_entradas = []
    
    # Recorre la lista de partidos para encontrar el partido con la mayor venta de entradas
    for partido in partidos:
        if partido.cantidad_entradas_vendidas > mayor_venta and partido.cantidad_entradas_vendidas != 0:
            mayor_venta = partido.cantidad_entradas_vendidas
            partidos_mayor_venta_entradas.clear()
            partidos_mayor_venta_entradas.append(partido)
        elif partido.cantidad_entradas_vendidas == mayor_venta and partido.cantidad_entradas_vendidas != 0:
            partidos_mayor_venta_entradas.append(partido)
    
    # Crea del gráfico
    plt.figure(figsize=(10, 6))
    plt.bar([f'Partido {p.numero}' for p in partidos_mayor_venta_entradas], 
            [p.cantidad_entradas_vendidas for p in partidos_mayor_venta_entradas],
            color='skyblue')
    plt.xlabel('Partido')
    plt.ylabel('Cantidad de Entradas Vendidas')
    plt.title('Partido con Mayor Venta de Entradas - Eurocopa 2024')
    plt.xticks(rotation=45)
    
    # Muestra el gráfico
    plt.tight_layout()
    plt.show()
    
def grafico_tabla_asistencia_partidos(partidos):
    """
    Función para generar el gráfico de la tabla de asistencia a los partidos
    """
    
    # Ordena la lista de partidos según asistencia
    partidos.sort(key=lambda partido: partido.asistencia, reverse=True)
    
    # Extrae los datos necesarios para el gráfico
    numeros_partidos = [f'Partido {partido.numero}' for partido in partidos]
    asistencias = [partido.asistencia for partido in partidos]
    
    # Crea del gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(numeros_partidos, asistencias, color='lightgreen')
    plt.xlabel('Partido')
    plt.ylabel('Asistencia')
    plt.title('Tabla de Asistencias a los Partidos - Eurocopa 2024')
    plt.xticks(rotation=45)
    
    # Muestra el gráfico
    plt.tight_layout()
    plt.show()

