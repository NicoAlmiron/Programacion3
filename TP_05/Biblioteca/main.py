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

libros = [
]

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
    categoria = categorias[int((input('categoria: '))) - 1]
    stock = int(input('cantidad de existencias: '))


    libro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "stock": stock
    }

    libros.append(libro)


def mostrar_libros():
    print('-------|###| BIBLIOTECA |###|-------')
    print('-----|# Lista de Existencias #|-------')
    for libro in libros:
        
        print(f'--|#Codigo: {libro['codigo']}')
        print(f'#Titulo: {libro['titulo']}')
        print(f'#Autor: {libro['autor']}')
        print(f'#Categoria: {libro['categoria']}')
        print(f'#Stock: {libro['stock']}')


while True:
    print('-------|###| BIBLIOTECA |###|-------')
    print('-( 1 )- - - -> Agregar Libro')
    print('-( 2 )- - - -> Mostrar Libros')
    print('-( 3 )- - - -> X')
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
        print('-( 3 )- - -> Buscar Libro')
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


