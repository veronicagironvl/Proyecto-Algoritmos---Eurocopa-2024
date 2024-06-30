from cliente import Cliente
from entrada import Entrada


#################### Modulo Gestión de venta de entradas ####################

                 
def registrar_cliente(clientes):
    """     
    Funcion para registrar un nuevo cliente en el sistema
    """

    # Da la bienvenida al usuario
    print('\n**** REGISTRO DE CLIENTES ****\n')

    # Solicita nombre y cedula al usuario
    nombre_cliente = input('Nombre y apellido: ').title()
    cedula = input('Cédula: ')
        
    # Verifica que el input de la cedula sea correcto
    while (not cedula.isdigit()) or (len(cedula) != 7 and len(cedula) != 8):
        print('\nError: Ingrese un número de cédula válido.')
        cedula = input('Cédula: ')
            
    for cliente in clientes:
        if cedula == cliente.cedula:
            print("\nYa existe un usuario con ese número de cédula. Intente de nuevo.")
            return

    # Solicita la edad al usuario    
    edad = input("Edad: ")
    
    # Verifica que el input de la edad sea un número
    while (not edad.isdigit()):
        print('\nError: Ingrese su edad en números.')
        edad = input('Edad: ')
     
    # Crea el objeto cliente    
    cliente = Cliente(nombre_cliente, cedula, edad)
    
    # Agrega al objeto cliente a la lista de clientes registrados
    clientes.append(cliente)
    
    # Le confirma al usuario que se  registro
    print(f'\n{nombre_cliente} registrado/a exitosamente!')
    return cliente

def comprar_entrada(clientes, partidos):
    """ Funcion para comprar entradas
    """
    
    print('\n**** COMPRA DE ENTRADAS ****\n')
    
    # Verifica que el cliente esté registrado
    cliente = verificar_cedula(clientes)     
    if cliente == None:
        return 
    
    # Ordenar partidos
    partidos.sort(key=lambda partido: partido.numero)  
        
    # Muestra todos los partidos        
    print('\n** Seleccione el partido **\n') 
    for index, partido in enumerate(partidos):
        print(f'- {partido}\n')
        
    # Pide al usuario el partido al que desea asistir     
    index = input('\nIngrese el número del partido al que desea asistir: ')
    
    # Valida el input del usuario
    while (not index.isdigit()) or (int(index) - 1 not in range(len(partidos))):
        print('\nError: Ingrese un número válido.')
        index = input('Ingrese el número del partido al que desea asistir: ')
    index = int(index) - 1
    
    # Selecciona el partido elegido
    partido_seleccionado = partidos[index]
    
    # Muestra las opciones de entradas disponible
    print(f'\n** {partido_seleccionado.equipo_local.nombre} vs {partido_seleccionado.equipo_visitante.nombre} - Selecciona el tipo de entrada que deseas **\n')
    opciones_entradas = ['Entrada general - $35.00', 'Entrada VIP - $75.00 (incluye acceso a restaurantes)']
    for index, opcion in enumerate(opciones_entradas):
        print(f'{index + 1}. {opcion}')
        
    # Pregunta al usuario que entrada quiere    
    seleccion_entrada = input('\nIngrese el número del tipo de entrada: ')
    
    # Verifica que el input de la entrada sea correcto
    while (not seleccion_entrada.isdigit()) or (int(seleccion_entrada) - 1 not in range(len(opciones_entradas))):
        print('\nError: Ingrese una opcion valida.')
        seleccion_entrada = input('Ingrese el número del tipo de entrada: ')
    
    # Convierte la seleccion a un numero 
    seleccion_entrada = int(seleccion_entrada) - 1    
    
    # Verifica si es un cliente vip 
    if seleccion_entrada == 1:
        cliente.es_vip = True
    
    # Llama a la funcion que busca el estadio donde sera el partido escogido    
    estadio = buscar_estadio(partido_seleccionado, partidos)
    
    # Muestra el mapa de los asientos del estadio de ese partido
    print(f'\n** {partido_seleccionado.equipo_local.nombre} vs {partido_seleccionado.equipo_visitante.nombre} - ', end='')
    partido_seleccionado.mostrar_asientos()
    asiento, fila, columna = partido_seleccionado.seleccionar_asiento()
      
    # Calcula el precio de la entrada    
    precio_total, iva, precio_inicial, descuento = calcular_precio_entrada(cliente.cedula, seleccion_entrada)
    
    # Selecciona el tipo de entrada a mostrar en la info de compra
    if seleccion_entrada == 0:
        tipo_entrada = 'General'
    if seleccion_entrada == 1:
        tipo_entrada =  'VIP'
      
    # Genera la informacion de la compra    
    generar_info_compra(cliente, partido_seleccionado, tipo_entrada, precio_total, iva, precio_inicial, descuento, asiento)
    
    # Le pregunta al usuario si desea completar la compra
    pagar = input('\nDesea completar la compra? (s/n): ')
    
    # Verifica el input de pagar
    while (not pagar.lower() == 's') and (not pagar.lower() == "n"):
        print('\nError: Ingrese un valor valido')
        pagar = input('Desea completar la compra? (s/n): ')
    
    # Completa o cancela la compra segun el input del usuario
    if pagar.lower() == 's':
        
        # Aparta el asiento
        partido_seleccionado.apartar_asiento(fila, columna)
        
        # Crea la entrada y su id
        entrada = Entrada(tipo_entrada, precio_total, partido_seleccionado, asiento, cliente)
        entrada.id = entrada.generar_id_entrada(partido_seleccionado.entradas_vendidas)
        cliente.n_entradas_compradas += 1
        
        # Agrega la entrada a las entradas compradas por el cliente
        cliente.entradas_compradas.append(entrada)
        
        # Suma la compra a la cuenta del cliente
        cliente.cuenta += precio_total
        
        # Agrega la entrada a la lista de entradas vendidas del partido
        partido_seleccionado.entradas_vendidas.append(entrada)
        partido_seleccionado.cantidad_entradas_vendidas += 1
                
        # Confirma la compra al usuario y le muestra el ID de su entrada
        print('\nPago realizado con éxito. ¡Disfruta del partido!')
        print('\nIMPORTANTE: ', end='')
        print(f'{entrada.id} es el ID de tu entrada. Anotalo! Lo necesitarás para entrar al estadio.')

    else:
        print('Compra cancelada.')
    
def generar_info_compra(cliente, partido, tipo_entrada, precio_total, iva, precio_inicial, descuento, asiento):
    """
    Funcion para generar la informacion de compra de una entrada        
    """
    
    print(F'\n-- Datos de compra para {cliente.nombre} --')
    print('-----------------------------------')
    print(f'Partido {partido.numero}: {partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre}. ({partido.grupo})')
    print(f'Fecha: {partido.fecha}')
    print(f'Estadio: {partido.estadio.nombre}')
    print(f'Asiento: {asiento}')
    print(f'Precio entrada: {tipo_entrada} - ${precio_inicial:.2f}')
    print(f'Descuento: ${descuento:.2f}')
    print(f'IVA: ${iva:.2f}')
    print(f'Total a pagar: ${precio_total:.2f}')
     
def verificar_cedula(clientes):  
    """
    Función para verificar si la cédula pertenece a un cliente registrado 
    """
  
    while True:
        # Pide la cedula al usuario
        cedula = input('Ingrese su cédula: ')
    
        # Verifica que el formato de la cedula sea correcto
        while (not cedula.isdigit()) or (len(cedula) != 7 and len(cedula) != 8):
            print('\nError: Ingrese un número de cédula válido.')
            cedula = input('Ingrese su cédula: ')
        
        # Busca que la cedula exista en la lista de clientes registrados    
        for cliente in clientes:
            if cedula == cliente.cedula:
                print(f'\nBienvenido/a {cliente.nombre}')
                return cliente
            
        # Si no encuentra la cedula, le avisa al usuario y llama a la funcion registrar cliente        
        print(f'\nCédula {cedula} no encontrada. Debe registrarse.')  
        return None
  
def buscar_estadio(partido_seleccionado, partidos):
    """
    Función para buscar el estadio donde se jugará el partido seleccionado por el usuario   

    """
    for partido in partidos:
        if partido_seleccionado.id == partido.id:
            return partido.estadio
 
def calcular_precio_entrada(cedula, entrada):
    """
    Funcion para calcular el precio de la entrada

    """
    
    # Fija el precio inicial de la entrada según el tipo seleccionado
    if entrada == 0:
        precio_inicial = 35
    if entrada == 1:
        precio_inicial = 75    

    # Verifica si hay descuento (solo si la cedula es número vampiro)
    descuento = verificar_descuento_vampiro(cedula)
    
    # Agrega el IVA
    iva = precio_inicial * 0.16
    precio = precio_inicial + iva
        
        
    # Si hay descuento, se lo aplica al precio
    if descuento:
        print('Como su cédula es un número vampiro ha recibido un 50% de descuento.')
        descuento_aplicado = precio * 0.5
        precio_total = precio - descuento_aplicado
    else:
        descuento_aplicado = 0
        precio_total = precio
        
    
    return precio_total, iva, precio_inicial, descuento_aplicado

def verificar_descuento_vampiro(cedula):
    """
    Funcion para calcular si la compra de la entrada tiene descuento

    """
    # Convierte la cedula en una lista con sus digitos
    cedula_numero = int(cedula)
    digitos = list(str(cedula))
    
    # Itera sobre los factores posibles desde el 1 hasta la raiz cuadrada de la cedula
    for i in range(1, int(cedula_numero**0.5) + 1):
        # Verifica si i es un factor de la cedula
        if cedula_numero % i == 0:
            factor1 = str(i)
            factor2 = str(cedula_numero // i )    
    
            factores = factor1 + factor2
        # Verifica si factores estan en los digitos de la cedula      
            if sorted(digitos) == sorted(factores) and len(factor1) == len(factor2):
                return True
    return False


