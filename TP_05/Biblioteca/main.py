import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
#lo anterior se realiza para poder limpiar la consola


libro = {}

libros = [
    {
        "codigo": 0,
        "titulo": "harry potter",
        "autor": "jk rowling",
        "categoria": "Redes",
        "stock": "18",
     },
     {
        "codigo": 1,
        "titulo": "SQlite",
        "autor": "pepito",
        "categoria": "Programación",
        "stock": "18",
     },
     {
        "codigo": 2,
        "titulo": "prueba",
        "autor": "pepito",
        "categoria": "Redes",
        "stock": "1",
     },
]

prestamo = {}

prestamos = [
    {
        "prestamoId": 0,
        "nombre": "Nicolas almiron",
        "fechaActual": "22-05-2026",
        "fechaEntrega": "",
        "codigoLibro": 0,
        "entregado": False,
    },
    {
        "prestamoId": 1,
        "nombre": "Cosme fulanito",
        "fechaActual": "20-05-2026",
        "fechaEntrega": "",
        "codigoLibro": 0,
        "entregado": False,
    },
    {
        "prestamoId": 2,
        "nombre": "pepito",
        "fechaActual": "23-05-2026",
        "fechaEntrega": "",
        "codigoLibro": 2,
        "entregado": False,
    }
]

categorias = ("Programación", "Base de Datos", "Redes", "Electronica")



def agregar_libro():
    print('-------|###| BIBLIOTECA |###|-------')
    print('-------|# Agregar un libro #|-------')
    libro['codigo'] = len(libros)
    libro['titulo'] = input('Titulo: ').lower()
    libro['autor'] = input('Autor: ').lower()
    print('Categorias: ')
    for _ in range(len(categorias)):
            print(f"-({_}): {categorias[_]}")
    libro['categoria'] = categorias[int((input('categoria: ')))]
    libro['stock'] = int(input('cantidad de existencias: '))

    for l in libros:
       if l['titulo'].lower() != libro['titulo'].lower():
            print('Este libro ya se registro en el sistema!')
            input('Precione cualquier tecla para continuar...')
            return
           
    libros.append(libro)
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
        for libro in libros:
            if libro.get('titulo') == libroAPrestar:
                
                print(f'--|#Codigo: {libro.get('codigo')}')
                print(f'#Titulo: {libro.get('titulo')}')
                print(f'#Autor: {libro.get('autor')}')
                print(f'#Categoria: {libro.get('categoria')}')
                print(f'#Stock: {libro.get('stock')}')

                if libro.get('stock') > 0:
                    confirmar = input('Confirmar este libro? (S/N):')
                    if confirmar.lower() == "s":
                        prestamo['prestamoId'] = len(prestamos)
                        print('se confirmo')
                        prestamo['nombre'] = input('Nombre completo: ').lower()
                        prestamo['fechaActual'] = input('Fecha Actual (dd-mm-aaaa): ')
                        prestamo['fechaEntrega'] = ""
                        prestamo['codigoLibro'] = int(libro.get('codigo'))
                        libro['stock'] = int(libro.get('stock')) - 1
                        prestamo['entregado'] = False
                        prestamos.append(prestamo)
                        break
                else:
                    print('|-- Libro Sin Stock!!!!')
                
            else:
                print('No se encontro el libro')
    input('Precione cualquier tecla para continuar...')

def mostrar_prestamos():
    print('-------|###| BIBLIOTECA |###|-------')
    print('-----|# Lista de Prestamos #|-------')
    for prestamo in prestamos:
        print(f'--|#Id Prestamo: {prestamo['prestamoId']}')
        print(f'#Nombre: {prestamo['nombre']}')
        print(f'#Fecha Actual: {prestamo['fechaActual']}')
        print(f'#Fecha Entrega: {prestamo['fechaEntrega']}')
        print(f'#Libro: {libros[prestamo.get('codigoLibro')].get('titulo')}')
        if prestamo.get('entregado') == False:
            print(f'#Entregado?: *No entregado*')
        elif prestamo.get('entregado') == True:
            print(f'#Entregado?: Entregado')

    input('Precione cualquier tecla para continuar...')
        


def devolver_prestamo():
    print('-------|###| BIBLIOTECA |###|-------')
    print('-------|#Devolver Prestamo#|-------')
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
    input('Precione cualquier tecla para continuar...')
    

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
    print('-( 0 )- - - -> Salir')
    opcion = int(input('-( OPCION )- ->: '))

    limpiar_consola()

    if opcion == 1:
        agregar_libro()
    elif opcion == 2:
        mostrar_libros()
    elif opcion == 3:
        buscar_libro()
    elif opcion == 4:
        prestar_libro()
    elif opcion == 5:
        mostrar_prestamos()
    elif opcion == 6:
        devolver_prestamo()
    elif opcion == 7:
        eliminar_libro()
    elif opcion == 0:
        break
    else:
        print('-( X )- - -> opcion incorrecta')


