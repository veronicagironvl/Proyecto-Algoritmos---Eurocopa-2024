from unidecode import unidecode

#################### Modulo Gestión de restaurantes ####################

def buscar_producto_por_tipo(estadios):
    """ Función para buscar los productos por tipo
    """

    productos = [] # Lista para almacenar los productos encontrados
    
    print('\n**** VER PRODUCTOS POR TIPO ****\n')

    print('** Tipos de productos disponibles en la Eurocopa 2024 **\n')    
    
    # Opciones de tipos de productos    
    opciones = ['plate', 'package', 'alcoholic', 'non-alcoholic']
    
    for index, opcion in enumerate(opciones):
        print(f' {index + 1}. {opcion}')
        
    # Solicita al usuario que seleccione una opción    
    seleccion_opcion = input('\nIngrese el número del tipo de producto que desea ver: ')
    
    # Valida el input del usuario    
    while (not seleccion_opcion.isdigit()) or (int(seleccion_opcion) - 1 not in range(len(opciones))):
        print('\nError: Ingrese una opción válida.')
        seleccion_opcion = input('\nIngrese el número de tipo de producto que desea ver: ')
            
    tipo_buscar = opciones[int(seleccion_opcion) - 1]
    
    print(F'\n** Productos de tipo {tipo_buscar} en la Eurocopa 2024 **\n')
    
    # Recorre todos los estadios, restaurantes y productos para encontrar los productos del tipo seleccionado
    for estadio in estadios: 
        for restaurante in estadio.restaurantes:
            for producto in restaurante.productos:
                if tipo_buscar == producto.tipo:
                    productos.append(producto)
       
    # Muestra la lista de productos encontrados             
    for index, producto in enumerate(productos):
        print(f'  {index + 1}. {producto.nombre} - ${producto.precio :.2f}')
  
def buscar_por_rango_precio(estadios):
    """
    Función para buscar los productos por rango de precio                    
    """
    
    # Lista para almacenar los productos encontrados dentro del rango de precio
    productos_encontrados = [] 
    
    print('\n**** VER PRODUCTOS POR RANGO DE PRECIO ****\n')

    
    # Solicita y valida el precio mínimo ingresado por el usuario
    while True: 
        try: 
            min_rango = float(input('Ingrese el precio minimo (ejemplo: 10.50): '))
            if min_rango < 0:
                print("\nError: El valor no puede ser negativo.")
                continue
            break
        except ValueError:
            print('\nError: Ingrese un valor válido.')
     
    # Solicita y valida el precio máximo ingresado por el usuario       
    while True:
        try:
            max_rango = float(input('Ingrese el precio máximo (ejemplo: 100.00): '))
            if max_rango < 0:
                print("\nError: El valor no puede ser negativo.")
                continue
            break
        except ValueError:
            print('\nError: Ingrese un valor válido.')
     
    # Recorre todos los estadios, restaurantes y productos para encontrar los productos en el rango de precio
    for estadio in estadios:
        for restaurante in estadio.restaurantes:
            for producto in restaurante.productos:
                if min_rango <= producto.precio <= max_rango:
                    productos_encontrados.append(producto)
                    
       
    # Muestra los productos encontrados dentro del rango de precio             
    print(F'\n** Productos entre ${min_rango :.2f} - ${max_rango :.2f}  en la Eurocopa 2024 **\n')     
    productos_encontrados.sort(key=lambda producto: producto.precio)       
    for index, producto in enumerate(productos_encontrados):
        print(f'  {index + 1}. {producto.nombre} - ${producto.precio :.2f}')
 
    # Mensaje si no se encuentran productos en el rango de precio seleccionado
    if not productos_encontrados:
        print('\nNo hay productos en el rango de precios seleccionado.')
   
def buscar_producto_por_nombre(estadios):
    """
    Función para buscar los productos por nombre     
    """
    
    # Lista para almacenar los productos encontrados    
    productos_encontrados = [] 
    
    print('\n**** VER PRODUCTOS POR NOMBRE ****\n')

    # Solicita al usuario el nombre del producto a buscar
    nombre_buscado = input('Ingrese el nombre del producto que desea buscar: ')
    
    # Recorre todos los estadios, restaurantes y productos para encontrar los productos con el nombre buscado
    for estadio in estadios:
        for restaurante in estadio.restaurantes:
            for producto in restaurante.productos:
                # Compara el nombre buscado con el nombre del producto ignorando mayúsculas/minúsculas y acentos
                if unidecode(nombre_buscado.lower()) in unidecode(producto.nombre.lower()):
                    productos_encontrados.append(producto) 
                    
    # Muestra los productos encontrados 
    print(F'\n** Productos encontrados con {nombre_buscado} en la Eurocopa 2024 **\n')
                
    if productos_encontrados:
        for index, producto in enumerate(productos_encontrados):
            print(f'  {index + 1}. {producto.nombre} - ${producto.precio :.2f}') 
    else:
        print(f'  No hay ningun producto en el sistema que se llame {nombre_buscado}.')    
  
  
 