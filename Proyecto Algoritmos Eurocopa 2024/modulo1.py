############################# Modulo Gestión de partidos y estadios #############################

def buscar_partido_por_pais(partidos):
    """
    Función para buscar y mostrar todos los partidos de un país según su código FIFA
    """

    
    # Lista de países con sus códigos FIFA correspondientes
    paises = ['Germany - GER', 'Scotland - SCO', 'Hungary - HUN', 'Switzerland - SUI', 'Spain - ESP', 'Croatia - CRO', 'Italy - ITA', 'Albania - ALB', 'Slovenia - SVN', 'Denmark - DEN', 'Serbia - SRB', 'England - ENG', 'Poland - POL', 'Netherlands - NED', 'Austria - FRA', 'France - FRA', 'Romania - ROU', 'Ukraine - UKR', 'Belgium - BEL', 'Slovakia - SVK', 'Turkey - TUR', 'Georgia - GEO', 'Portugal - POR', 'Czech Republic - CZE']
    
    # Lista de códigos FIFA válidos
    codigos_fifa = ['GER', 'SCO', 'HUN', 'SUI', 'ESP', 'CRO', 'ITA', 'ALB', 'SVN', 'DEN', 'SRB', 'ENG', 'POL', 'NED', 'FRA', 'FRA', 'ROU', 'UKR', 'BEL', 'SVK', 'TUR', 'GEO', 'POR', 'CZE']
    
    # Imprime la lista de países y sus códigos FIFA para el usuario
    print('\n**** VER TODOS LOS PARTIDOS DE UN PAÍS ****')
    print("\n** Lista de países y sus códigos FIFA **\n")
    for pais in paises:
        print(f'{pais}')
     
    # Solicita al usuario que ingrese el código FIFA del país que desea buscar    
    buscar_codigo = input('\nIngrese el código FIFA del país (en mayúsculas y tres letras): ').upper()
    
    # Valida el input del usuario
    while (not buscar_codigo.isascii()) or len(buscar_codigo) != 3 or buscar_codigo not in codigos_fifa:
        if not buscar_codigo.isascii() or len(buscar_codigo) !=3:
            print('El código debe tener tres letras en mayúsculas.')
        elif buscar_codigo not in codigos_fifa:
            print('Código no encontrado. Intente nuevamente.')
        buscar_codigo = input('Ingrese el codigo FIFA del pais: ').upper() 
      
    # Lista vacia para guardar los partidos encontrados para el país     
    partidos_del_pais = []
    
    # Itera sobre todos los partidos y agregar aquellos que tengan al país buscado
    for partido in partidos:
        if partido.equipo_local.codigo == buscar_codigo or partido.equipo_visitante.codigo == buscar_codigo:
            partidos_del_pais.append(partido)
    
    # Muestra los partidos encontrados o un mensaje si no se encontraron partidos        
    if partidos_del_pais:    
        print(f'\n** Partidos de {buscar_codigo} **\n')    
        for index, partido in enumerate(partidos_del_pais):
            print(f'  {index + 1}. {partido}')
    else:
        print(f'\nNo se encontraron partidos para {buscar_codigo}')

def buscar_partido_por_estadio(partidos, estadios):
    """
    Buscar todos los partidos que se jugarán en un estadio específico
    """
    
    # Muestra la lista de estadios disponibles
    print('\n**** VER TODOS LOS PARTIDOS DE UN ESTADIO ****')
    print("\n** Lista de estadios **\n")
    for index, estadio in enumerate(estadios):
        print(f'{index + 1}. {estadio.nombre}')
        
    # Pide al usuario que ingrese el número del estadio a buscar    
    busca_estadio = input('\nIngrese el número del estadio a buscar: ')
    
    # Valida el input del usuario
    while (not busca_estadio.isdigit()) or (int(busca_estadio) - 1 not in range(len(estadios))):
        print('\nError: Ingrese un número válido de estadio.')
        busca_estadio = input('Ingrese el número del estadio a buscar: ')
    
    # Convierte el número ingresado por el usuario a uno valido que este en la lista
    busca_estadio = int(busca_estadio) - 1
    
    # Obtiene el ID del estadio seleccionado
    for index, estadio in enumerate(estadios):
        if busca_estadio == index:
            buscar_id = estadio.id
            
    # Lista vacia para guardar los partidos encontrados para el estadio   
    partidos_del_estadio = []
        
    # Itera sobre todos los partidos y agregar aquellos que tengan el id del estadio             
    for partido in partidos:
        if buscar_id == partido.estadio.id:
            partidos_del_estadio.append(partido)
    
    # Muestra los partidos encontrados o un mensaje si no hay partidos        
    if partidos_del_estadio:    
        print(f'\n** Partidos en el {estadios[busca_estadio].nombre} **\n')    
        for index, partido in enumerate(partidos_del_estadio):
            print(f'  {index + 1}. Partido {partido.numero}: {partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre}\n     Fecha: {partido.fecha}\n     Grupo: {partido.grupo}')
    else:
        print(f'\nNo se encontraron partidos para {estadios[busca_estadio].nombre}')
        
def buscar_partido_por_fecha(partidos):
    """
    Buscar todos los partidos que se jugarán en una fecha determinada
    """
    
    fechas_disponibles = []
    
    for partido in partidos:
        if partido.fecha not in fechas_disponibles:
            fechas_disponibles.append(partido.fecha)
    
    # Muestra la lista de fechas de partidos disponibles
    print('\n**** VER TODOS LOS PARTIDOS DE UNA FECHA ****')
    print("\n** Lista de fechas cuando hay partidos **\n")
    for index, fecha in enumerate(fechas_disponibles):
        print(f'{index + 1}. {fecha}')
        
    # Pide al usuario que ingrese el número del estadio a buscar    
    index = input('\nIngrese el número de la fecha a buscar partidos: ')
    
    # Valida el input del usuario
    while (not index.isdigit()) or (int(index) - 1 not in range(len(fechas_disponibles))):
        print('\nError: Ingrese un número válido.')
        index = input('Ingrese el número de la fecha a buscar partidos: ')
    
    # Convierte el número ingresado por el usuario a uno valido que este en la lista de fechas
    index = int(index) - 1
    buscar_fecha = fechas_disponibles[index]
            
    # Lista vacia para guardar los partidos encontrados para la fecha seleccionada   
    partidos_de_fecha = []
        
    # Itera sobre todos los partidos y agregar aquellos que tengan la fecha seleccionada            
    for partido in partidos:
        if buscar_fecha == partido.fecha:
            partidos_de_fecha.append(partido)
    
    # Muestra los partidos encontrados o un mensaje si no hay partidos        
    if partidos_de_fecha:    
        print(f'\n* Partidos del {fechas_disponibles[index]} *\n')    
        for index, partido in enumerate(partidos_de_fecha):
            print(f'  {index + 1}. {partido}')
    else:
        print(f'\nNo se encontraron partidos para {fechas_disponibles[index]}')
   