import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
#lo anterior se realiza para poder limpiar la consola


libros = [
    {
        "codigo": 0,
        "titulo": "harry potter",
        "autor": "jk rowling",
        "categoria": "redes",
        "stock": "18",
     },
     {
        "codigo": 1,
        "titulo": "SQlite",
        "autor": "pepito",
        "categoria": "redes",
        "stock": "18",
     },
     {
        "codigo": 2,
        "titulo": "prueba",
        "autor": "pepito",
        "categoria": "redes",
        "stock": "18",
     },
]

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
    codigo = len(libros)
    titulo = input('Titulo: ').lower()
    autor = input('Autor: ').lower()
    print('Categorias: ')
    for _ in range(len(categorias)):
            print(f"-({_}): {categorias[_]}")
    categoria = categorias[int((input('categoria: ')))]
    stock = int(input('cantidad de existencias: '))


    libro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "stock": stock
    }

    libros.append(libro)
    input('Precione cualquier tecla para continuar...')


def mostrar_libros():
    print('-------|###| BIBLIOTECA |###|-------')
    print('-----|# Lista de Existencias #|-------')
    for libro in libros:
        
        print(f'--|#Codigo: {libro['codigo']}')
        print(f'#Titulo: {libro['titulo']}')
        print(f'#Autor: {libro['autor']}')
        print(f'#Categoria: {libro['categoria']}')
        print(f'#Stock: {libro['stock']}')
    input('Precione cualquier tecla para continuar...')


def buscar_libro():
    print('-------|###| BIBLIOTECA |###|-------')
    print('-------|#  Buscar libros   #|-------')
    print('ingrese el titulo del libro')
    tituloLibro = input('Titulo:  ').lower()
    
    for libro in libros:
        if libro.get('titulo') == tituloLibro:
            print(f'--|#Codigo: {libro.get('codigo')}')
            print(f'#Titulo: {libro.get('titulo')}')
            print(f'#Autor: {libro.get('autor')}')
            print(f'#Categoria: {libro.get('categoria')}')
            print(f'#Stock: {libro.get('stock')}')
        
    input('Precione cualquier tecla para continuar...')
    
    
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
                
                if libro['stock'] <= 0:
                    print('Libro sin Stock')
                    break
                    
                
                confirmar = input('Confirmar este libro? (S/N):')
                if confirmar.lower() == "s":
                    idprestamo = len(prestamos)
                    print('se confirmo')
                    nombre = input('Nombre completo: ').lower()
                    fechaActual = input('Fecha Actual (dd-mm-aaaa): ')
                    codigoLibro = int(libro.get('codigo'))
                    libro['stock'] = int(libro.get('stock')) - 1
                    prestamo = {
                        "prestamoId": idprestamo,
                        "nombre": nombre,
                        "fechaActual": fechaActual,
                        "fechaEntrega": "",
                        "codigoLibro": codigoLibro,
                        "entregado": False
                    }
                    
                    prestamos.append(prestamo)
                    break
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


