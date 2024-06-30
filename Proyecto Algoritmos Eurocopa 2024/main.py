import requests
from equipo import Equipo
from estadio import Estadio
from partido import Partido
from restaurante import Restaurante
from producto import Comida, Bebida
from modulo1 import buscar_partido_por_pais, buscar_partido_por_estadio, buscar_partido_por_fecha 
from modulo2 import registrar_cliente, comprar_entrada
from modulo3 import verificar_entrada
from modulo4 import buscar_producto_por_tipo, buscar_por_rango_precio, buscar_producto_por_nombre
from modulo5 import ver_restaurante
from modulo6 import ver_estadisticas

def obtener_datos_api(url):
    """
    Obtiene los datos de la API en formato JSON.
    
    """
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json() # Retorna los datos en formato JSON si la respuesta es exitosa
    else:
        raise Exception(f'Error al obtener datos de la api {respuesta.status_code}') # Lanza una excepción si ocurre un error
    
# Urls de los endpoints de estadios, equipos y partidos    
URL_EQUIPOS = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json'
URL_ESTADIOS = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json'
URL_PARTIDOS = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json'

# Obtiene los datos de la API
datos_equipos = obtener_datos_api(URL_EQUIPOS)
datos_estadios = obtener_datos_api(URL_ESTADIOS)
datos_partidos = obtener_datos_api(URL_PARTIDOS)

def registrar_equipos(datos_equipos_api):
    """
    Convierte los datos de equipos obtenidos de la API en objetos de la clase Equipo.
    """
    equipos = []
    for equipo in datos_equipos_api:
        id_equipo = equipo['id']
        nombre = equipo['name']
        codigo = equipo ['code']
        grupo = equipo['group']
        equipo = Equipo(id_equipo, nombre, codigo, grupo)
        equipos.append(equipo)
    return equipos

def registrar_estadios(datos_estadios_api):
    """ 
    Funcion para convertir los datos de los estadios a objetos
    """
    estadios = []
    for estadio in datos_estadios_api:
        id_estadio = estadio['id']
        nombre_estadio = estadio['name']
        ciudad_estadio = estadio['city']
        capacidad_general = estadio['capacity'][0]
        capacidad_vip = estadio['capacity'][1]
        restaurantes = []
        
        for restaurante in estadio['restaurants']:
            nombre_restaurante = restaurante['name']
            productos = []
            
            for producto in restaurante['products']:
                nombre_producto = producto['name']
                quantity_producto = producto['quantity']
                precio_producto = float(producto['price']) * 1.16 # Se aplica el 16% de IVA
                stock = producto['stock']
                tipo = producto['adicional']
                
                # Crear objeto Comida o Bebida según el tipo de producto
                if tipo == 'plate' or tipo == 'package':
                    producto = Comida(nombre_producto, quantity_producto, precio_producto, stock, tipo)
                elif tipo == 'alcoholic' or tipo == 'non-alcoholic':
                    producto = Bebida(nombre_producto, quantity_producto, precio_producto, stock, tipo)
                else:
                    continue
                productos.append(producto)
            restaurante = Restaurante(nombre_restaurante, productos)
            restaurantes.append(restaurante)
        estadio = Estadio(id_estadio, nombre_estadio, ciudad_estadio, capacidad_general, capacidad_vip, restaurantes)
        estadios.append(estadio)
    return estadios
 
def encontrar_equipo_por_id(equipos, id):
    """ 
    Función para encontrar un equipo por su ID  
    """     

    for equipo in equipos:
        if id == equipo.id:
            return equipo
    return None
      
def encontrar_estadio_por_id(estadios, id):
    """
    Función para encontrar un estadio por su ID
    """  
    for estadio in estadios:
        if id == estadio.id:
            return estadio
    return None
              
def registrar_partidos(datos_partidos_api, equipos, estadios):
    """
    Funcion para convertir los datos de los partidos a objetos
    """  
    partidos = []
    for partido in datos_partidos_api:
        id_partido = partido['id']    
        numero_partido = partido['number']
        fecha = partido['date']
        grupo = partido['group']
        id_equipo_local = partido['home']['id']
        id_equipo_visitante = partido['away']['id']
        id_estadio = partido['stadium_id']
        
        # Buscar a los equipos por su ID en la lista de registrados
        equipo_local = encontrar_equipo_por_id(equipos, id_equipo_local)
        equipo_visitante = encontrar_equipo_por_id(equipos, id_equipo_visitante)
        
        # Crea un nuevo objeto  Equipo si no existe en la lista
        if not equipo_local:
            codigo_local = partido['home']['code']
            nombre_local = partido['home']['name']
            grupo_local = partido['home']['group']
            equipo_local = Equipo(id, nombre_local, codigo_local, grupo_local)
            equipos.append(equipo_local)
            
        if not equipo_visitante:
            codigo_visitante = partido['away']['code']
            nombre_visitante = partido['away']['name']                
            grupo_visitante = partido['away']['group']
            equipo_visitante = Equipo(id, nombre_visitante, codigo_visitante, grupo_visitante)
            equipos.append(equipo_visitante)
            
        # Buscar el estadio por su ID    
        estadio = encontrar_estadio_por_id(estadios, id_estadio)
            
        # Crea el objeto Partido y lo agrega a la lista de partidos    
        partido = Partido(id_partido, numero_partido, equipo_local, equipo_visitante, fecha, grupo, estadio)
        partidos.append(partido)
            
    return partidos
                
                      
def main():
    """
    Función princial del programa
    """
    # Crea las listas de equipos, estadios, partidos y clientes
    equipos = registrar_equipos(datos_equipos)
    estadios = registrar_estadios(datos_estadios)
    partidos = registrar_partidos(datos_partidos, equipos, estadios)
    clientes = []

    while True:
        # Muestra el menú principal
        print('\n***********************************************************')
    
        print('* * *          E U R O C O P A  2 0 2 4               * * *')
        
        print('***********************************************************\n')
    
        opciones = ['Ver todos los partidos de un país', 
                    'Ver todos los partidos de un estadio',
                    'Ver todos los partidos de una fecha',
                    'Registrar un usuario', 'Comprar una entrada', 
                    'Asistir a un partido (Verificar entrada)', 
                    'Comprar en el restaurante',
                    'Ver porductos por nombre', 
                    'Ver productos por tipo',
                    'Ver productos por rango de precio', 
                    'Ver estadísticas', 
                    'Salir del sistema']
    
        print('**** MENÚ PRINCIPAL ****\n')
        for index, opcion in enumerate(opciones):
            print(f'{index + 1}. {opcion}')
        
        # Solicita al usuario que seleccione una opción
        seleccionar_opcion = input('\nIngrese la opción deseada: ')
        
        while (not seleccionar_opcion.isdigit()) or (int(seleccionar_opcion) - 1 not in range(len(opciones))):
            print('\nError: Ingrese un valor válido.')    
            seleccionar_opcion = input('Ingrese la opción deseada: ')
        
        seleccionar_opcion = int(seleccionar_opcion) - 1
        
        # Ejecuta la función correspondiente según la opción seleccionada
        if seleccionar_opcion == 0:
            buscar_partido_por_pais(partidos)
        elif seleccionar_opcion == 1:
            buscar_partido_por_estadio(partidos, estadios)
        elif seleccionar_opcion == 2:
            buscar_partido_por_fecha(partidos)
        elif seleccionar_opcion == 3:
            registrar_cliente(clientes)
        elif seleccionar_opcion == 4:
            comprar_entrada(clientes, partidos)
        elif seleccionar_opcion == 5:
            verificar_entrada(partidos)
        elif seleccionar_opcion == 6:
            ver_restaurante(clientes)
        elif seleccionar_opcion == 7:
            buscar_producto_por_nombre(estadios)
        elif seleccionar_opcion== 8:
            buscar_producto_por_tipo(estadios)
        elif seleccionar_opcion == 9:
            buscar_por_rango_precio(estadios)
        elif seleccionar_opcion == 10:
            ver_estadisticas(clientes, partidos, estadios)
        elif seleccionar_opcion == 11:
            print('\nGracias por usar el sistema de la Eurocopa 2024!')
            print('Saliendo...')
            break          
          
main()
