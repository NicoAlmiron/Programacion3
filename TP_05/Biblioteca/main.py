import os
import os.path

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
#lo anterior se realiza para poder limpiar la consola


# Diccionarios De Datos
# Libro:
#codigo - Entero - 6 bits
#titulo - Cadena - 30 bits
#autor - Cadena - 30 bits
#categoria - Cadena - 20 bits
#stock - Entero - 4 bits
#REGISTRO: 
#1     |harry potter                  |jk rowling                    |Redes               |20  |


# Prestamo:
#prestamoId - Entero - 6 bits
#nombre - Cadena - 30 bits
#fechaActual - Cadena - 10 bits
#fechaEntrega - Cadena - 10 bits
#codigoLibro - Entero - 6 bits
#entregado - Entero - 1 bits
#REGISTRO:
#1     |cosme fulanito                |14-06-2026|          |1     |0|








libro = {}

libros = [
    # {
    #     "codigo": 0,
    #     "titulo": "harry potter",
    #     "autor": "jk rowling",
    #     "categoria": "Redes",
    #     "stock": "18",
    #  },
    #  {
    #     "codigo": 1,
    #     "titulo": "SQlite",
    #     "autor": "pepito",
    #     "categoria": "Programación",
    #     "stock": "18",
    #  },
    #  {
    #     "codigo": 2,
    #     "titulo": "prueba",
    #     "autor": "pepito",
    #     "categoria": "Redes",
    #     "stock": "1",
    #  },
]

# Archivos

# ------- Leer archivos
def leer_file_libros():


    registros = []

    with open('libros.txt', 'r') as file:
        registros = file.readlines()
        if len(registros) <= 0:
            return
        for reg in registros:
            libro ={
                "codigo": int(reg[0:6]),
                "titulo": reg[7:36].strip('  '),
                "autor": reg[38:67].strip('  '),
                "categoria": reg[69:88].strip('  '),
                "stock": int(reg[90:93]),
                }
            libros.append(libro)

    

# ------- Escribir archivos
def escribir_file_libro(libro):
    with open('libros.txt', 'a') as arch_lib:
        reg_libro = ""
        reg_libro += f"{libro['codigo']}{(" " * ( 6 - len(str(libro['codigo'])) ) )}|" # codigo
        reg_libro += f"{libro['titulo']}{(" " * ( 30 - len(libro['titulo']) ) )}|" # titulo
        reg_libro += f"{libro['autor']}{(" " * ( 30 - len(libro['autor']) ) )}|" # autor
        reg_libro += f"{libro['categoria']}{(" " * ( 20 - len(libro['categoria']) ) )}|" # categoria
        reg_libro += f"{libro['stock']}{(" " * ( 4 - len(str(libro['stock'])) ) )}|\n" # stock
        arch_lib.write(reg_libro)


def buscar_libro_archivo(id_libro):

    with open('libros.txt', 'r') as file:
        registros = file.readlines()
        if len(registros) <= 0:
            return
        for reg in registros:
            libro ={
                "codigo": int(reg[0:6]),
                "titulo": reg[7:36].strip('  '),
                "autor": reg[38:67].strip('  '),
                "categoria": reg[69:88].strip('  '),
                "stock": int(reg[90:93]),
                }
            if libro['codigo'] == id_libro:
                return libro


def reescribir_archivo():
    with open('libros.txt', 'w') as arch_lib:
        for libro in libros:
            reg_libro = ""
            reg_libro += f"{libro['codigo']}{(" " * ( 6 - len(str(libro['codigo'])) ) )}|" # codigo
            reg_libro += f"{libro['titulo']}{(" " * ( 30 - len(libro['titulo']) ) )}|" # titulo
            reg_libro += f"{libro['autor']}{(" " * ( 30 - len(libro['autor']) ) )}|" # autor
            reg_libro += f"{libro['categoria']}{(" " * ( 20 - len(libro['categoria']) ) )}|" # categoria
            reg_libro += f"{libro['stock']}{(" " * ( 4 - len(str(libro['stock'])) ) )}|\n" # stock
            arch_lib.write(reg_libro)




prestamo = {}

prestamos = [
    # {
    #     "prestamoId": 0,
    #     "nombre": "Nicolas almiron",
    #     "fechaActual": "22-05-2026",
    #     "fechaEntrega": "",
    #     "codigoLibro": 0,
    #     "entregado": False,
    # },
    # {
    #     "prestamoId": 1,
    #     "nombre": "Cosme fulanito",
    #     "fechaActual": "20-05-2026",
    #     "fechaEntrega": "",
    #     "codigoLibro": 0,
    #     "entregado": False,
    # },
    # {
    #     "prestamoId": 2,
    #     "nombre": "pepito",
    #     "fechaActual": "23-05-2026",
    #     "fechaEntrega": "",
    #     "codigoLibro": 2,
    #     "entregado": False,
    # }
]

# Prestamo:
#prestamoId - Entero - 6 bits
#nombre - Cadena - 30 bits
#fechaActual - Cadena - 10 bits
#fechaEntrega - Cadena - 10 bits
#codigoLibro - Entero - 6 bits
#entregado - Entero - 1 bits
#REGISTRO:
#1     |cosme fulanito                |14-06-2026|          |1     |0|



def leer_file_prestamo():


    registros = []

    with open('prestamos.txt', 'r') as file:
        registros = file.readlines()
        if len(registros) <= 0:
            return 
        for reg in registros:
            prestamo ={
                "prestamoId": int(reg[0:5]),
                "nombre": reg[7:36].strip('  '),
                "fechaActual": reg[38:47].strip('  '),
                "fechaEntrega": reg[49:58].strip('  '),
                "codigoLibro": int(reg[60:65]),
                "entregado": int(reg[67]),
                }
            prestamos.append(prestamo)

def escribir_file_prestamo(prestamo):
    with open('prestamos.txt', 'a') as arch_pres:
        reg_prestamo = ""
        reg_prestamo += f"\n{prestamo['prestamoId']}{(" " * ( 6 - len(str(prestamo['prestamoId'])) ) )}|" # codigo
        reg_prestamo += f"{prestamo['nombre']}{(" " * ( 30 - len(prestamo['nombre']) ) )}|" # titulo
        reg_prestamo += f"{prestamo['fechaActual']}{(" " * ( 10 - len(prestamo['fechaActual']) ) )}|" # autor
        reg_prestamo += f"{prestamo['fechaEntrega']}{(" " * ( 10 - len(prestamo['fechaEntrega']) ) )}|" # categoria
        reg_prestamo += f"{prestamo['codigoLibro']}{(" " * ( 6 - len(str(prestamo['codigoLibro'])) ) )}|" # stock
        reg_prestamo += f"{int(prestamo['entregado'])}{(" " * ( 1 - len(str(prestamo['entregado'])) ) )}|" # stock
        arch_pres.write(reg_prestamo)

def devolucion_archivo(pres):
    with open('prestamos.txt', 'w') as arch_pres:            
        for prestamo in prestamos:
            reg_prestamo = ""
            reg_prestamo += f"\n{prestamo['prestamoId']}{(" " * ( 6 - len(str(prestamo['prestamoId'])) ) )}|" # codigo
            reg_prestamo += f"{prestamo['nombre']}{(" " * ( 30 - len(prestamo['nombre']) ) )}|" # titulo
            reg_prestamo += f"{prestamo['fechaActual']}{(" " * ( 10 - len(prestamo['fechaActual']) ) )}|" # autor
            reg_prestamo += f"{prestamo['fechaEntrega']}{(" " * ( 10 - len(prestamo['fechaEntrega']) ) )}|" # categoria
            reg_prestamo += f"{prestamo['codigoLibro']}{(" " * ( 6 - len(str(prestamo['codigoLibro'])) ) )}|" # stock
            reg_prestamo += f"{int(prestamo['entregado'])}{(" " * ( 1 - len(str(prestamo['entregado'])) ) )}|" # stock
            arch_pres.write(reg_prestamo)

categorias = ("Programacion", "Base de Datos", "Redes", "Electronica")



def agregar_libro():
    print('-------|###| BIBLIOTECA |###|-------')
    print('-------|# Agregar un libro #|-------')
    libro['codigo'] = len(libros) + 1
    libro['titulo'] = input('Titulo: ').lower()
    libro['autor'] = input('Autor: ').lower()
    print('Categorias: ')
    for _ in range(len(categorias)):
            print(f"-({_}): {categorias[_]}")
    libro['categoria'] = categorias[int((input('categoria: ')))]
    libro['stock'] = int(input('cantidad de existencias: '))

    for l in libros:
       #print(f"{l['titulo'].lower()} - {libro['titulo']}")
       if l['titulo'].lower() == libro['titulo'].lower():
            print('Este libro ya se registro en el sistema!')
            input('Precione cualquier tecla para continuar...')
            return
           
    libros.append(libro)
    escribir_file_libro(libro)
    input('Precione cualquier tecla para continuar...')



def mostrar_libros():
    while True:
        limpiar_consola()
        print('-------|###| BIBLIOTECA |###|-------')
        print('----|#  Listas de libros   #|-----')
        print('-( 1 )- - - -> Listar Todo')
        print('-( 2 )- - - -> Listar Alfabeticamente')
        print('-( 3 )- - - -> Listar Con Stock Bajo')
        #print('-( 4 )- - - -> Buscar por Codigo')
        print('-( 0 )- - - -> Salir')
        opcion = input('-( OPCION )- ->: ')

        match opcion:
            case "1": 
                print('---|# Lista de Existencias')
                for libro in libros:
                    print(f'--|#Codigo: {libro['codigo']}')
                    print(f'#Titulo: {libro['titulo']}')
                    print(f'#Autor: {libro['autor']}')
                    print(f'#Categoria: {libro['categoria']}')
                    print(f'#Stock: {libro['stock']}')
                input('Precione cualquier tecla para continuar...')
            case "2": 

                print('-------|###| BIBLIOTECA |###|-------')
                print('---|# Listado Alfabeticamente')

                libros_ordenados = sorted(libros, key=lambda lib: lib['titulo'].lower()) #key es el criterio que va a usar para ordenar, en este caso se usa el titulo del libro ("lambda" es una funcion INLINE)

                for libro in libros_ordenados:

                    print(f'--|#Codigo: {libro['codigo']}')
                    print(f'#Titulo: {libro['titulo']}')
                    print(f'#Autor: {libro['autor']}')
                    print(f'#Categoria: {libro['categoria']}')
                    print(f'#Stock: {libro['stock']}')
                input('Precione cualquier tecla para continuar...')
            case "3": 
                print('---|# Lista de bajo stock')
                for libro in libros:
                    if int(libro['stock']) <= 2:
                        print(f'--|#Codigo: {libro['codigo']}')
                        print(f'#Titulo: {libro['titulo']}')
                        print(f'#Autor: {libro['autor']}')
                        print(f'#Categoria: {libro['categoria']}')
                        print(f'#Stock: {libro['stock']} ¡STOCK BAJO!')
                input('Precione cualquier tecla para continuar...')
            case "0": 
                print('|#| SALIENDO.....')
                break
            case _:
                print('|#|*** INGRESE UNA OPCION VALIDA ***|#|')

def buscar_libro():
    while True:
        limpiar_consola()
        print('-------|###| BIBLIOTECA |###|-------')
        print('----|#  Buscador de libros   #|-----')
        print('-( 1 )- - - -> Buscar por Titulo')
        print('-( 2 )- - - -> Buscar por Autor')
        print('-( 3 )- - - -> Buscar por Categoria')
        print('-( 4 )- - - -> Buscar por Codigo')
        print('-( 0 )- - - -> Salir')
        opcion = input('-( OPCION )- ->: ')
        limpiar_consola()
        match opcion:
            case "1": 
                print('ingrese el titulo del libro')
                tituloLibro = input('Titulo:  ').lower()
                bandera = False                
                for libro in libros:
                    if libro.get('titulo') == tituloLibro:
                        print(f'--|#Codigo: {libro.get('codigo')}')
                        print(f'#Titulo: {libro.get('titulo')}')
                        print(f'#Autor: {libro.get('autor')}')
                        print(f'#Categoria: {libro.get('categoria')}')
                        print(f'#Stock: {libro.get('stock')}')
                        bandera = True
                if bandera is False:
                    print('No se encontro el libro '+tituloLibro)
            case "2": 
                print('ingrese el Autor del libro')
                autor = input('Autor:  ').lower()
                bandera = False                
                for libro in libros:
                    if libro.get('autor') == autor:
                        print(f'--|#Codigo: {libro.get('codigo')}')
                        print(f'#Titulo: {libro.get('titulo')}')
                        print(f'#Autor: {libro.get('autor')}')
                        print(f'#Categoria: {libro.get('categoria')}')
                        print(f'#Stock: {libro.get('stock')}')
                        bandera = True
                if bandera is False:
                    print('No se encontro el libro del autor ' + autor)
            case "3": 
                
                print('ingrese la categoria a buscar: ')
                for _ in range(len(categorias)):
                    print(f"-({_}): {categorias[_]}")
                categ = categorias[int((input('Categoria: ')))]
                bandera = False                
                limpiar_consola()
                print('Categoria: ' + categ)
                for libro in libros:
                    if libro.get('categoria') == categ:
                        print(f'--|#Codigo: {libro.get('codigo')}')
                        print(f'#Titulo: {libro.get('titulo')}')
                        print(f'#Autor: {libro.get('autor')}')
                        print(f'#Categoria: {libro.get('categoria')}')
                        print(f'#Stock: {libro.get('stock')}')
                        bandera = True
                if bandera is False:
                    print('No se encontraron libros en la categoria ' + categ)
            case "4": 
                print('ingrese el Codigo del libro')
                cod = input('Codigo:  ').lower()
                bandera = False                
                for libro in libros:
                    if libro.get('codigo') == int(cod):
                        print(f'--|#Codigo: {libro.get('codigo')}')
                        print(f'#Titulo: {libro.get('titulo')}')
                        print(f'#Autor: {libro.get('autor')}')
                        print(f'#Categoria: {libro.get('categoria')}')
                        print(f'#Stock: {libro.get('stock')}')
                        bandera = True
                if bandera is False:
                    print('No se encontro el libro con el codigo: ' + autor)
            case "0": 
                print('|#| SALIENDO.....')
                break
            case _:
                print('|#|*** INGRESE UNA OPCION VALIDA ***|#|')

        input('Precione cualquier tecla para continuar...')
        print('-------|###| BIBLIOTECA |###|-------')
        print('-------|#  Buscar libros   #|-------')

    
    
def prestar_libro():
    print('-------|###| BIBLIOTECA |###|-------')
    print('-------|#Solicitar Prestamo#|-------')
    while True:
        libroAPrestar = input('--#Titulo del Libro (para salir digitar "Salir"): ')
        if libroAPrestar.lower() == 'salir':
            break
        bandera = False
        for libro in libros:
            if libro.get('titulo').lower() == libroAPrestar.lower():
                
                print(f'--|#Codigo: {libro.get('codigo')}')
                print(f'#Titulo: {libro.get('titulo')}')
                print(f'#Autor: {libro.get('autor')}')
                print(f'#Categoria: {libro.get('categoria')}')
                print(f'#Stock: {libro.get('stock')}')

                if int(libro.get('stock')) > 0:
                    confirmar = input('Confirmar este libro? (S/N):')
                    if confirmar.lower() == "s":
                        prestamo['prestamoId'] = len(prestamos) + 1
                        print('se confirmo')
                        prestamo['nombre'] = input('Nombre completo: ').lower()
                        prestamo['fechaActual'] = input('Fecha Actual (dd-mm-aaaa): ')
                        prestamo['fechaEntrega'] = ""
                        prestamo['codigoLibro'] = int(libro.get('codigo'))
                        libro['stock'] = int(libro.get('stock')) - 1
                        prestamo['entregado'] = False
                        prestamos.append(prestamo)
                        escribir_file_prestamo(prestamo)
                        bandera = True
                        break
                else:
                    print('|-- Libro Sin Stock!!!!')
                
        if bandera is False:
            print('No se encontro el libro...')
    input('Precione cualquier tecla para continuar...')

def mostrar_prestamos():
    print('-------|###| BIBLIOTECA |###|-------')
    print('-----|# Lista de Prestamos #|-------')
    if len(prestamos) <= 0:
        print('|#-- No hay prestamos en el sistema')
        input('Precione cualquier tecla para continuar...')
        return
    for prestamo in prestamos:
        print(f'--|#Id Prestamo: {prestamo['prestamoId']}')
        print(f'#Nombre: {prestamo['nombre']}')
        print(f'#Fecha Actual: {prestamo['fechaActual']}')
        print(f'#Fecha Entrega: {prestamo['fechaEntrega']}')
        for libro in libros:
            if libro['codigo'] == prestamo['codigoLibro']:
                print(f'#Libro: {libro['titulo']}')
        if prestamo.get('entregado') == False:
            print(f'#Entregado?: *No entregado*')
        elif prestamo.get('entregado') == True:
            print(f'#Entregado?: Entregado')

    input('Precione cualquier tecla para continuar...')
        


def devolver_prestamo():
    print('-------|###| BIBLIOTECA |###|-------')
    print('-------|#Devolver Prestamo#|-------')
    if len(prestamos) <= 0:
        print('|#-- No hay prestamos en el sistema')
        input('Precione cualquier tecla para continuar...')
        return
    
    print('ingrese el nombre de la persona y el titulo del libro')
    nombre = input('#Nombre: ').lower()
    titulo = input('#Titulo: ').lower()
    codigo = 0
    for prestamo in prestamos:
        if prestamo.get('nombre') == nombre:
            for libro in libros:
                if libro.get('titulo') == titulo:
                    codigo = int(libro.get('codigo'))
            if prestamo.get('codigoLibro') == codigo:
                print('---|#Prestamos encontrado!')
                print(f'--|#Id Prestamo: {prestamo['prestamoId']}')
                print(f'#Fecha Actual: {prestamo['fechaActual']}')
                print(f'#Fecha Entrega: {prestamo['fechaEntrega']}')
                if prestamo.get('entregado') == False:
                    print(f'#Entregado?: *No entregado*')
                elif prestamo.get('entregado') == True:
                    print(f'#Entregado?: Entregado')
                confirmar = input('---|###Confirmar la devolucion? (S/N) --> ')
                fechaDeEntrega = input('#Fecha Actual (dd-mm-aaa): ')
                if confirmar.lower() == 's':
                    prestamo['fechaEntrega'] = fechaDeEntrega
                    prestamo['entregado'] = True
                    devolucion_archivo(prestamo)
                    print('---|#Devolucion Exitosa!')
                    break
                elif confirmar.lower() == 'n': 
                    print('---|#Devolucion cancelada!')    
            else:
                print('-|#No se encontro el libro registrado con ese nombre!')
                break
    input('Precione cualquier tecla para continuar...')


def eliminar_libro():
    print('-------|###| BIBLIOTECA |###|-------')
    print('-------|#  Eliminar Libro  #|-------')
    titulo = input('#Titulo: ').lower()
    for libro in libros:
        if libro.get('titulo') == titulo:
            libros.remove(libro)
            print('Se elimino correctamente!')
            reescribir_archivo()
    input('Precione cualquier tecla para continuar...')
    
def estadisticas():
    print('-------|###| BIBLIOTECA |###|-------')
    print('-------|#   Estadisticas   #|-------')
    cantidad_libros_general = 0
    cantidad_libros_stock = 0
    cantidad_libros_prestados = len(prestamos)
    cantidad_libros_entregados = 0
    cantidad_libros_sin_entregar = 0
    for libro in libros:
        cantidad_libros_stock += int(libro['stock'])
    for prestamo in prestamos:
        for clave, valor in prestamo.items():
            if clave == 'entregado' and valor is True:
                cantidad_libros_entregados += 1
            elif clave == 'entregado' and valor is False:
                cantidad_libros_sin_entregar += 1
    
    libros_ordenados = sorted(libros, key=lambda lib: int(lib['stock']), reverse=True)
    
    libro_mayor_stock = libros_ordenados[0]['titulo']
    
    cantidad_libros_general = cantidad_libros_stock + cantidad_libros_prestados
    
    print(f'|#-- Cantidad de libros: {cantidad_libros_general}')    
    print(f'|#-- Cantidad de libros en stock: {cantidad_libros_stock}')
    print(f'|#-- Cantidad de libros prestamos: {cantidad_libros_prestados}')
    print(f'|#-- Libro con mas stock: {libro_mayor_stock}')
    print(f'|###--- Prestamos: {cantidad_libros_prestados}')
    print(f'|#-- Cantidad de libros devueltos: {cantidad_libros_entregados}')
    print(f'|#-- Cantidad de libros sin devolver: {cantidad_libros_sin_entregar}')
    input('Precione cualquier tecla para continuar...')


def leer_archivos():
    leer_file_libros()
    leer_file_prestamo()







leer_archivos()
while True:
    limpiar_consola()
    print('-------|###| BIBLIOTECA |###|-------')
    print('-( 1 )- - - -> Agregar Libro')
    print('-( 2 )- - - -> Mostrar Libros')
    print('-( 3 )- - - -> Buscar Libros')
    print('-( 4 )- - - -> Prestar Libro')
    print('-( 5 )- - - -> Listar Prestamos')
    print('-( 6 )- - - -> Devolver Prestamo')
    print('-( 7 )- - - -> Eliminar Libro')
    print('-( 8 )- - - -> Estadisticas')
    print('-( 0 )- - - -> Salir')
    opcion = input('-( OPCION )- ->: ')
    limpiar_consola()
    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        mostrar_libros()
    elif opcion == "3":
        buscar_libro()
    elif opcion == "4":
        prestar_libro()
    elif opcion == "5":
        mostrar_prestamos()
    elif opcion == "6":
        devolver_prestamo()
    elif opcion == "7":
        eliminar_libro()
    elif opcion == "8":
        estadisticas()
    elif opcion == "0":
        break
    else:
        print('-( X )- - -> opcion incorrecta')


