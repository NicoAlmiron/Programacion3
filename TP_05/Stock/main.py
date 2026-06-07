import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
#lo anterior se realiza para poder limpiar la consola

producto = {}
productos = [
    {
        "id": 1,
        "nombre": "teclado mecanico",
        "precio": 150000,
        "stock": 8
    },
    {
        "id": 2,
        "nombre": "mouse gamer RGB",
        "precio": 50000,
        "stock": 9
    }
]


ventas = [
    {
        "id_venta": 1,
        "detalle_venta": {
            1 : (2, 300000),
            2 : (1, 50000)
        },
        "importe_total": 350000,
        "forma_pago": 'Efectivo'
    },
    {
        "id_venta": 2,
        "detalle_venta": {
            
            2 : (1, 50000)
        },
        "importe_total": 50000,
        "forma_pago": 'Tarjeta'
    },
]

metodos_pago = ("Efectivo", "Transferencia", "Tarjeta")

def agregar_prod():
    print('|###--··  TecStore  ··--###|')
    print('|##-· Producto Nuevo')
    producto['id'] = len(productos)+1
    print(f'|##-· Producto ID: {producto['id']}')
    producto['nombre'] = input('|-Nobre del articulo: ').lower()
    producto['precio'] = float(input('|-Precio: $'))
    producto['stock'] = int(input('|-Stock Inicial: '))

    productos.append(producto)
    print("Se Guardo el producto exitosamente!")


def mod_prod():
    print('|###--··  TecStore  ··--###|')
    print('|##-· Ingrese el Id del producto')
    id_buscar = input('|##-· ID: ')
    for prod in productos:
        for clave, valor in prod.items():
            if clave == 'id' and int(id_buscar) == valor:      
                producto['id'] = len(prod)+1
                print(f'|##-· Producto ID: {producto['id']}')
                print(f"|-Nobre anterior *{prod['nombre']}*")
                producto['nombre'] = input('|-Nobre del articulo: ')
                print(f"|-Precio anterior $*{prod['precio']}*")
                producto['precio'] = float(input('|-Precio: $'))
                prod.update(producto)
    print("Se Guardo el producto exitosamente!")

def mod_stock_prod():
    print('|###--··  TecStore  ··--###|')
    print('|##-· Ingrese el Id del producto')
    id_buscar = input('|##-· ID: ')
    for prod in productos:
        for clave, valor in prod.items():
            if clave == 'id' and int(id_buscar) == valor:      
                print(f"|-Stock actual *{prod['stock']}*")
                prod.update({'stock': int(input('|-Stock: '))})
    print("Se actualizo el stock exitosamente!")

def eliminar_producto():
    print('|###--··  TecStore  ··--###|')
    print('|##-· Ingrese el Id del producto')
    id_buscar = input('|##-· ID: ')
    for prod in productos:
        for clave, valor in prod.items():
            if clave == 'id' and valor == int(id_buscar):
                productos.remove(prod)
    print("Se Elimino el Producto exitosamente!")

def abm_producto():
    while True:
        limpiar_consola()
        print('|###--··  TecStore  ··--###|')
        print('|##······················##|')
        print('| 1 ) --- Agregar Nuevo')
        print('| 2 ) --- Modificar Existente')
        print('| 3 ) --- Modificar Stock')
        print('| 4 ) --- Eliminar')
        print('| 0 ) --- Salir')
        op = input('|OPCION···---: ')

        limpiar_consola()
        match op:
            case "1":
                agregar_prod()
            case "2":
                mod_prod()
            case "3":
                mod_stock_prod()
            case "4":
                eliminar_producto()
            case "0":
                break
            case _:
                print('Ingrese una opcion valida!')
        
        input('precione una tecla para continuar!')



def listar_productos():
    if len(productos) == 0:
        print('|\t·No se emcontraron productos!')
        return
    for producto in productos:
        print(f'|ID: {producto['id']} | {producto['nombre']} | ${producto['precio']} | STOCK: {producto['stock']}')


def mostrar_un_prod(id):
    for producto in productos:
        if producto['id'] == id:
            print(f'|Nro. Art: {producto['id']} | {producto['nombre']} | ${producto['precio']}')


def realizar_venta():
    venta = {}
    list_venta = {}
    print('|###--··  TecStore  ··--###|')
    listar_productos()
    total_venta = 0
    print('|##-· Ingrese el Id del producto o X para continuar')
    while True:
        id_v = input('|##-· ID: ')
        if id_v.lower() == 'x':
            break
        for producto in productos:
            if int(id_v) == producto['id']:
                cant = int(input('|##-· Cantidad: '))
                if producto['stock'] > 0:
                    v = (cant , (producto['precio'] * cant))
                    total_venta = total_venta + (producto['precio'] * cant)
                    producto['stock'] = producto['stock'] - cant
                    list_venta.update({producto['id'] : v})
                else:
                    print('|# Producto Sin Stock')
                print(f'|#-{producto['nombre']} Agregado a la compra')        
    venta["importe_total"] = total_venta
    if len(list_venta) > 0:
        venta['id_venta'] = len(ventas) + 1
        venta['detalle_venta'] = list_venta
        print('|##-· Ingrese la forma de pago para continuar')
        print('|· (1) Efectivo · (2) Transferencia · (3) Tarjeta · (0) Cancelar')
        op = input('|##-Forma de Pago: ')

        match op:
            case '1':
                venta['forma_pago'] = metodos_pago[int(op)-1]
            case '2':
                venta['forma_pago'] = metodos_pago[int(op)-1]
            case '3':
                venta['forma_pago'] = metodos_pago[int(op)-1]
            case "0":
                print('|##- Venta Cancelada! ')
                return
            case _:
                print('Ingrese una opcion valida!')
        
        ventas.append(venta)
        print("Se realizo la venta exitosamente!")
        print('|# Resumen')
        print('|- Productos')
        print('|········································')
        for prod, detalle in venta['detalle_venta'].items():
            mostrar_un_prod(prod)
            print(f'|\t\tx {detalle[0]} - SubTotal ${detalle[1]} ')
            print('|········································')
        print(f'|- Total: ${venta['importe_total']}')
        print(f'|- Forma de pago: {venta['forma_pago']}')
        
def listar_ventas():
    print('|# Lista de Ventas')
    if len(ventas) == 0:
        print('| ·No se emcontraron ventas!')
        return
    for venta in ventas:
        print(f'|- Venta Nroº: {venta['id_venta']}')
        print('|- Productos')
        for prod, detalle in venta['detalle_venta'].items():
            for producto in productos:
                if producto['id'] == prod:
                    print(f'|\t-{producto['nombre']} | ${producto['precio']} - x {detalle[0]} - SubTotal ${detalle[1]} ')
        print(f'|- Total: ${venta['importe_total']}')
        print(f'|- Forma de pago: {venta['forma_pago']}')
        print('|········································')

def fitrador(filtro, buscar):
    encontrado = False
    for producto in productos:
        for clave, valor in producto.items():
            if clave == filtro and valor == buscar:
                encontrado = True
                return mostrar_un_prod(int(producto['id']))
    if encontrado == False:
        print('|#·No se econtro el producto!***')


def buscador():
     
     while True:
        limpiar_consola()
        print('|###--··  TecStore  ··--###|')
        print('|##······················##|')
        if len(productos) == 0:
            print('|\t·No se emcontraron productos!')
            return
        print('| 1 ) --- Buscar por Nombre')
        print('| 2 ) --- Buscar por ID')
        print('| 3 ) --- Buscar por Precio')
        print('| 0 ) --- Salir')
        op = input('|OPCION···---: ')

        limpiar_consola()
        match op:
            case "1":
                print('|###--··  TecStore  ··--###|')
                print('|##--- Ingrese el Nombre a Buscar')
                nombre = input('|Nombre···---: ').lower()
                fitrador('nombre', nombre.lower())
            case "2":
                print('|###--··  TecStore  ··--###|')
                print('|##--- Ingrese el ID a Buscar')
                id_prod = int(input('|ID ···---: '))
                fitrador('id', id_prod)
            case "3":
                print('|###--··  TecStore  ··--###|')
                print('|##--- Ingrese el Precio a Buscar')
                precio = float(input('|Precio ···---: $'))
                fitrador('precio', precio)
            case "0":
                break
            case _:
                print('Ingrese una opcion valida!')
        
        input('precione una tecla para continuar!')

while True:
    limpiar_consola()
    print('|###--··  TecStore  ··--###|')
    print('|##······················##|')
    print('| 1 ) --- Agregar Producto') #·
    print('| 2 ) --- Mostrar Productos')
    print('| 3 ) --- Modificar Stock') #·
    print('| 4 ) --- Realizar Venta')
    print('| 5 ) --- Mostrar Ventas')
    print('| 6 ) --- Buscar Producto')
    print('| 7 ) --- Eliminar Producto') #·
    print('| 0 ) --- Salir')
    op = input('|OPCION···---: ')

    limpiar_consola()
    match op:
        case "1":
            abm_producto()
        case "2":
            print('|·# Productos')
            listar_productos()
        case "3":
            mod_stock_prod()
        case "4":
            realizar_venta()
        case "5":
            listar_ventas()
        case "6":
            buscador()
        case "7":
            eliminar_producto()
        case "0":
            print('Saliendo.....')
            break
        case _:
            print('Ingrese una opcion valida!')
    
    input('precione una tecla para continuar!')

