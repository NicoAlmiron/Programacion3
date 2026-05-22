import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
#lo anterior se realiza para poder limpiar la consola

# libro = {
#         "codigo": 0,
#         "titulo": "",
#         "autor": "",
#         "categoria": "",
#         "stock": "",
#      }

libros = []

prestamos = []

categorias = ("Programación", "Base de Datos", "Redes", "Electronica")


def agregar_libro():
    print('-------|###| BIBLIOTECA |###|-------')
    print('-------|# Agregar un libro #|-------')
    codigo = len(libros) + 1
    titulo = input('Titulo: ')
    autor = input('Autor: ')
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
    tituloLibro = input('Titulo:  ')
    
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
        libroAPrestar= input('--#Titulo del Libro: ')
        for libro in libros:
            if libro.get('titulo') == libroAPrestar:
                print(f'--|#Codigo: {libro.get('codigo')}')
                print(f'#Titulo: {libro.get('titulo')}')
                print(f'#Autor: {libro.get('autor')}')
                print(f'#Categoria: {libro.get('categoria')}')
                print(f'#Stock: {libro.get('stock')}')
                
                confirmar = input('Confirmar este libro? (S/N):')
                if confirmar == "S" :
                    print('se confirmo')
                    nombre = input('Nombre completo: ')
                    fechaActual = input('Fecha Actual (dd-mm-aaaa): ')
                    codigoLibro = libro['codigo']                    
                    prestamo = {
                        "nombre": nombre,
                        "fechaActual": fechaActual,
                        "fechaEntrega": "",
                        "codigoLibro": codigoLibro,
                        "entregado": False
                    }
                    
                    prestamos.append(prestamo)
            else:
                print('No se encontro el libro')
        

while True:
    limpiar_consola()
    print('-------|###| BIBLIOTECA |###|-------')
    print('-( 1 )- - - -> Agregar Libro')
    print('-( 2 )- - - -> Mostrar Libros')
    print('-( 3 )- - - -> Buscar Libros')
    print('-( 4 )- - - -> X')
    print('-( 5 )- - - -> X')
    print('-( 6 )- - - -> X')
    print('-( 7 )- - - -> Agregar Categoria')
    print('-( 8 )- - - -> Salir')
    opcion = int(input('-( OPCION )- ->: '))

    limpiar_consola()

    if opcion == 1:
        agregar_libro()
    elif opcion == 2:
        mostrar_libros()
    elif opcion == 3:
        buscar_libro()
    elif opcion == 4:
        print('-( 4 )- - -> Prestar Libro')
    elif opcion == 5:
        print('-( 5 )- - -> Devolver Libro')
    elif opcion == 6:
        print('-( 6 )- - -> Eliminar Libro')
    elif opcion == 8:
        break
    else:
        print('-( X )- - -> opcion incorrecta')


