#################### Modulo Gestión de venta de restaurantes ####################

def verificar_vip(clientes):
    """
    Función para verificar si el cliente es vip
    """
    while True:
        # Pide la cedula al usuario
        cedula = input('Ingrese su cédula: ')
    
        # Verifica que el formato de la cedula sea correcto
        while (not cedula.isdigit()) or (len(cedula) != 7 and len(cedula) != 8):
            print('\nError: Ingrese un número de cédula válido.')
            cedula = input('Ingrese su cédula: ')
        
        # Verifica si la entrada le pertenece a un cliente VIP    
        for cliente in clientes:
            if cliente.cedula == cedula and cliente.es_vip:
                print(f'\nBienvenido/a {cliente.nombre}!')
                return cliente
            
        # Si no encuentra la cedula, le avisa al usuario        
        print('\nNo se encontró un cliente VIP con esa cedula.\nPara acceder a los restaurantes debes comprar una entrada VIP.')  
        return  None

def ver_restaurante(clientes):
    """
    Función para ver los restaurantes a los que el usuario tiene acceso como cliente vip
    """
    
    print('\n**** COMPRAR EN EL RESTAURANTE  ****\n')
    
    # Verifica que el cliente esté registrado y sea vip
    cliente = verificar_vip(clientes)     
    
    # Si el cliente no está registrado, termina la función
    if cliente is None:
        return
    
    # Si el cliente no ha comprado entradas, termina la función
    if not cliente.entradas_compradas:
        print('Para acceder a los restaurantes debes comprar una entrada VIP.')
        return
            
    # Lista de entradas VIP del cliente
    entradas_con_vip = []
    for entrada in cliente.entradas_compradas:
        if entrada.tipo_entrada == 'VIP':
            entradas_con_vip.append(entrada)
       
    # Si el cliente no tiene entradas VIP, termina la función        
    if not entradas_con_vip:
        print('No tienes entradas VIP para ningún partido.')
        return
    
    # Lista de estadios a los que el cliente VIP tiene acceso
    estadios_disponibles = []
    for entrada in entradas_con_vip:
        if entrada.partido.estadio not in estadios_disponibles:
            estadios_disponibles.append(entrada.partido.estadio)
            
    # Muestra los estadios a los que el cliente tiene acceso VIP
    print('Estos son los estadios a los que tienes acceso como cliente VIP: \n')        
    for index, estadio in enumerate(estadios_disponibles):
        print(f'{index + 1}. Estadio: {estadio.nombre} \n')
    
    # Solicitar al cliente que seleccione un estadio
    seleccion_e = input('\nIngresa el numero del estadio del que deseas ver sus restaurantes: ')
    while (not seleccion_e.isdigit()) or (int(seleccion_e) - 1 not in range(len(cliente.entradas_compradas))):
        print('\nError: Ingrese un valor válido.')
        seleccion_e = input('Ingresa el numero del estadio del que deseas ver sus restaurantes: ')
    
    seleccion_e = int(seleccion_e) - 1
    estadio = estadios_disponibles[seleccion_e]
  
    # Muestra los restaurantes en el estadio seleccionado
    print(f'\n** Restaurantes en el estadio {estadio.nombre} **\n')
    for index, restaurante in enumerate(estadio.restaurantes):
        print(f'  {index + 1}. {restaurante.nombre}')
        
    # Solicita al cliente que seleccione un restaurante    
    seleccion_r = input('\nIngresa el número del restaurante donde deseas comprar: ')
    while (not seleccion_r.isdigit()) or (int(seleccion_r) - 1 not in range(len(estadio.restaurantes))):
        print('\nError: Ingrese un valor válido.')
        seleccion_r = input('Ingresa el número del restaurante donde deseas comprar: ')
        
    seleccion_r = int(seleccion_r) - 1
    restaurante = estadio.restaurantes[seleccion_r]
    
    # Llama a la función para comprar de productos en el restaurante seleccionado
    comprar_productos(cliente, restaurante)

def comprar_productos(cliente, restaurante):  
    """
    Función para comprar productos del restaurante        
    """
    precio_compra = 0.0 # Variable para acumular el precio total de la compra
    carrito_con_productos = [] # Lista para almacenar los productos seleccionados
    repetir = True  # Variable de control para repetir el proceso de selección de productos
    
    while repetir:  
        print(f'\n** Menú de {restaurante.nombre} **\n')
        
        # Muestra los productos disponibles en el restaurante
        for index, producto in enumerate(restaurante.productos):
            if producto.stock > 0:
                print(f'  {index + 1}. {producto.nombre} ({producto.tipo}) - ${producto.precio:.2f} (cantidad disponible: {producto.stock})')
        
        # Solicita al cliente que seleccione un producto
        seleccion_producto = input('\nIngrese el número del producto que desea: ')
        while (not seleccion_producto.isdigit()) or (int(seleccion_producto) - 1 not in range(len(restaurante.productos))):
            print('\nError: Ingrese un valor válido.')
            seleccion_producto = input('Ingrese el número del producto que desea: ')

        seleccion_producto = int(seleccion_producto) - 1
        producto = restaurante.productos[seleccion_producto]
        
        # Verifica si el producto seleccionado es alcohólico y si el cliente es mayor de edad
        while producto.tipo == 'alcoholic' and int(cliente.edad) < 18:
            print(f'{producto.nombre} contiene alcohol. Para poder comprarlo debes ser mayor de edad')
            seleccion_producto = input('Elije el número de otro producto: ')   
            while (not seleccion_producto.isdigit()) or (int(seleccion_producto) - 1 not in range(len(restaurante.productos))):
                print('\nError: Ingrese un valor válido.')
                seleccion_producto = input('Ingrese el número del producto que desea: ')
                
            seleccion_producto = int(seleccion_producto) - 1
            producto = restaurante.productos[seleccion_producto]
        
        # Agrega el producto al carrito de compras
        print(f'\n{producto.nombre} ha sido agregado exitosamente a tu carrito de compra.')    
        carrito_con_productos.append(producto)
        precio_compra += int(producto.precio)
        
        # Pregunta al cliente si desea agregar otro producto
        seguir_comprando = input("\nDeseas agregar otro producto? (s/n): ")
        while (not seguir_comprando.lower() == 's') and (not seguir_comprando.lower() == 'n'):
            print('\nError: Ingrese un valor válido.')
            seguir_comprando = input("Deseas agregar otro producto? (s/n): ")
            
        if seguir_comprando.lower() == "n":
            repetir = False # Finaliza el ciclo de selección de productos
    
    # Calcula el precio total y el descuento
    precio_total, descuento = calcular_pago_productos(cliente.cedula, precio_compra)    
    
    # Genera los datos de la compra
    generar_datos_compra(cliente, restaurante, precio_compra, precio_total, descuento, carrito_con_productos)
    
    # Pregunta al cliente si desea completar la compra
    pagar = input('\nDesea completar la compra? (s/n): ')
    while (not pagar.lower() == 's') and (not pagar.lower() == "n"):
        print('\nError: Ingrese un valor valido')
        pagar = input('Desea completar la compra? (s/n): ')
        
    if pagar == 's':
        cliente.cuenta += precio_total # Actualiza la cuenta del cliente
        for producto in carrito_con_productos:
            producto.stock -= 1 # Reduce el stock del producto
            producto.quantity += 1 # Incrementa la cantidad comprada
            producto.vendidos += 1 # Incrementa el contador de productos vendidos
        print('\nCompra realizada con éxito! Gracias por escogernos. A continuación tu factura:\n')
        generar_factura(cliente, restaurante, precio_compra, precio_total, descuento, carrito_con_productos) # Generar la factura
    elif pagar == 'n':
        print('\nCompra cancelada.')
 
def calcular_pago_productos(cedula, precio_compra):
    """
    Función para calcular el precio y aplicar el descuento en la compra  
    """
    
    descuento = 0.0 # Inicializa el descuento en 0
    
    # Verifica si la cédula del cliente califica para un descuento
    if verificar_descuento_perfecto(cedula):
        # Calcula el descuento del 15% sobre el precio de compra
        descuento = precio_compra * 0.15
        print('Como su cedula es un número perfecto obtuvo un descuento de 15%')
        
    # Resta el descuento del precio de compra    
    precio_total = precio_compra - descuento
    
    # Retorna el precio de compra final y el descuento aplicado
    return precio_total, descuento

def generar_datos_compra(cliente, restaurante, precio_compra, precio_total, descuento, carrito_con_productos):
    """
    Función para generar los datos de compra       
    """
    
    print(F'\n-- Datos de compra para {cliente.nombre} --')
    print('-----------------------------------')
    print(f'Restaurante: {restaurante.nombre}')
    print('-----------------------------------')
    print('Productos: ')
    for producto in carrito_con_productos:
        print(f'  {producto.nombre} ${producto.precio:.2f}')
    print('-----------------------------------')
    print(f'Subtotal: ${precio_compra:.2f}')
    print(f'Descuento: ${descuento:.2f}')
    print(f'Total: ${precio_total:.2f}')
    
def verificar_descuento_perfecto(cedula):
    """
    Función para verificar si la cédula es un número perfecto    
    """
    
    # Convierte la cédula en un número entero
    cedula = int(cedula)
    suma_divisores = 0
    
    # Calcula la suma de todos los divisores propios de la cédula
    for i in range(1, cedula):
        if cedula % i == 0:
            suma_divisores += i
    
    # Verifica si la suma de los divisores es igual a la cédula
    if suma_divisores == cedula:
        return True
    else:
        return False

def generar_factura(cliente, restaurante, precio_compra, precio_total, descuento, carrito_con_productos):
    """
    Función para generar la factura de la compra
    """
    
    print(f'Restaurante {restaurante.nombre}')
    print('---------------------------------')
    print(f'Cliente: {cliente.nombre}')
    print(f'Cedula: {cliente.cedula}')
    print('---------------------------------')
    print('Productos: ')
    for producto in carrito_con_productos:
        print(f'  {producto.nombre} ({producto.tipo}) - ${producto.precio:.2f}')
    print('---------------------------------')
    print(f'Subtotal: ${precio_compra:.2f}')
    print(f'Descuento: ${descuento:.2f}')
    print(f'Total: ${precio_total:.2f}')
