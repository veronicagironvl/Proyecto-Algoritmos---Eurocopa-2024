#################### Modulo Gestión de asistencia a partidos ####################     
             
def verificar_entrada(partidos):
    """
    Funcion para verificar el ID de una entrada 

    """
    # Ordena la lista de los partidos
    partidos.sort(key=lambda partido: partido.numero)
    
    # Muestra todos los partidos  
    print('\n**** VERIFICAR UNA ENTRADA PARA ASISTIR A UN PARTIDO ****') 
    print('\n** Seleccione el Partido **\n')    
    for index, partido in enumerate(partidos):
        print(f'- Partido {partido.numero}: {partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre} ({partido.grupo})')
        
    # Pide al usuario el partido al que desea asistir     
    index = input('\nIngrese el número del partido al que desea asistir: ')
    
    # Valida el input del usuario
    while (not index.isdigit()) or (int(index) - 1 not in range(len(partidos))):
        print('\nError: Ingrese un número válido.')
        index = input('Ingrese el número del partido al que desea asistir: ')   
    index = int(index) - 1
    
    # Selecciona el partido elegido
    partido = partidos[index]
    
    # Pide al usuario el ID de la entrada
    id_entrada = input('\nIngresa el id de la entrada: ').upper()
    
    # Valida el input del usuario
    while (not id_entrada.isalnum()) or len(id_entrada) != 8:
        print('\nError: el ID debe tener 8 caracteres alfanuméricos.')
        id_entrada = input('Ingresa el ID de la entrada: ')
     
    # Verifica si la entrada ya fue usada    
    for entrada in partido.entradas_usadas:
        if id_entrada == entrada.id:
            print('\nError: esta entrada ya fue utilizada.')
            return
        
    # Verifica si la entrada existe
    for entrada in partido.entradas_vendidas:
        if id_entrada == entrada.id:
            partido.entradas_usadas.append(entrada)
            print('\nBienvenido/a! Disfruta el partido.')
            partido.asistencia += 1
