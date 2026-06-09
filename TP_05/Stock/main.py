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
        if int(producto['stock']) < 4:
            print(f'|ID: {producto['id']} | {producto['nombre']} | ${producto['precio']} | STOCK: {producto['stock']} (STOCK BAJO)')
        elif int(producto['stock']) == 0:
            print(f'|ID: {producto['id']} | {producto['nombre']} | ${producto['precio']} | STOCK: {producto['stock']} (SIN STOCK!!*!*!*!)')
        else:
            print(f'|ID: {producto['id']} | {producto['nombre']} | ${producto['precio']} | STOCK: {producto['stock']}')
            


def mostrar_un_prod(id):
    encontrado = False
    for producto in productos:
        if producto['id'] == id:
            encontrado = True
            return producto
    if encontrado is False : return False


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
        while True:
            print('|##-· Ingrese la forma de pago para continuar')
            print('|· (1) Efectivo · (2) Transferencia · (3) Tarjeta · (0) Cancelar')
            op =  input('|##-Forma de Pago: ')
            match op:
                case '1':
                    venta['forma_pago'] = metodos_pago[int(op)-1]
                    break
                case '2':
                    venta['forma_pago'] = metodos_pago[int(op)-1]
                    break
                case '3':
                    venta['forma_pago'] = metodos_pago[int(op)-1]
                    break
                case "0":
                    print('|##- Venta Cancelada! ')
                    return
                case _:
                    print('Ingrese una opcion valida!')

        while True:
            print('|##-· Aplicar descuentos')
            print('|· (1) % Porcentaje · (2) $ Importe · (0) Sin Descuentos')
            opc = input('|##-Opcion: ')
            desc = float(input('|#  ·Descuento: '))

            if opc == "1":
                venta['importe_total'] = float(venta['importe_total'])*(float(venta['importe_total'])*(desc/100))
                print(f'|-----------Importe Actualizado ${venta['importe_total']}')
                break
            elif opc == "2":
                venta['importe_total'] = venta['importe_total'] - desc
                print(f'|-----------Importe Actualizado ${venta['importe_total']}')
                break
            elif opc == "0":
                print(f'|-----------Importe Actual ${venta['importe_total']}')
                break
            else:
                print(f'|# No se indico una opcion valida!')

        
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
        print('|  ·No se emcontraron ventas!')
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


# def ordenador_stock(orden):
#     if orden == 1:
        
#         return prod_stock
#     elif orden == 2:
        
#         return prod_stock

def estadisticas_productos():
    info_productos = {}

    cant_precio_total = 0
    cant_total = 0
    for producto in productos:
        cant_total = cant_total + int(producto['stock'])
        cant_precio_total = cant_precio_total + (float(producto['precio'])*int(producto['stock']))
    
    prod_mas_stock = sorted(productos, key=lambda prod: prod['stock'],reverse=True)
    prod_menos_stock = sorted(productos, key=lambda prod: prod['stock'])
    
    info_productos.update({'capital_neto':cant_precio_total})
    info_productos.update({'cantidad_existencias':cant_total})
    info_productos.update({'prod_stock_bajo':prod_mas_stock[0]})
    info_productos.update({'prod_stock_alto':prod_menos_stock[0]})

    return info_productos

def estadisticas_ventas():
    info_ventas = {}

    cant_ventas = len(ventas)
    cant_ganancias = 0

    metodos_contados = {
        # 'efectivo':{
        #  cantidad_de_usos : importe_total   
        # }
    }

    prod_vendidos = {
        # id_prod : cantidad_vendidos
    }
    

    for venta in ventas:
        cant_ganancias = cant_ganancias + float(venta['importe_total'])
        for clave, prod in venta.items():
            if clave == 'detalle_venta':
                for id_prod, detalles in prod.items():
                    cant_prod_v = 0
                    if id_prod in prod_vendidos:
                        cant_prod_v = int(prod_vendidos[id_prod]) + detalles[0]
                    else:
                        cant_prod_v = detalles[0]
                    
                    prod_vendidos.update({id_prod: cant_prod_v})
        forma_p = ""
        metodo = {}
        cont_metodo = 0
        importe_metodo = 0
        if venta['forma_pago'] in metodos_contados:
            forma_p = venta['forma_pago']
            cont_metodo = int(metodos_contados[forma_p][1][0]) + 1
            importe_metodo = int(metodos_contados[forma_p][1][1]) + venta['importe_total']
        else:
            forma_p = venta['forma_pago']
            metodo = {}
            cont_metodo = 1
            importe_metodo = venta['importe_total']
        metodo.update({cont_metodo:importe_metodo})

        metodos_contados.update({venta['forma_pago']:metodo})


    prod_mas_vendido = sorted(prod_vendidos.items(), key=lambda prod: prod[1])
    prod_menos_vendido = sorted(prod_mas_vendido, reverse=True)

    metodo_mas_usado = sorted(metodos_contados.items(), key=lambda metodo: list(metodo[1])[0])
    metodo_menos_usado = sorted(metodo_mas_usado, reverse=True)


    # print('|-Cantidad de ventas: 99 - $999999')
    info_ventas.update({'cantidad_venta': cant_ventas})
    info_ventas.update({'cantidad_ganancia': cant_ganancias})


    # print('|-Producto Mas Vendido: teclado - ventas: 22')
    info_ventas.update({'prod_mas_vendidos':prod_mas_vendido[0]})
    # print('|-Producto Menos Vendido: teclado - ventas: 2')
    info_ventas.update({'prod_menos_vendidos':prod_menos_vendido[0]})

    # print('|-Metodo de Pago mas usado: efectivo - $99999')
    info_ventas.update({'metodo_mas_usado':metodo_mas_usado[0]})
    # print('|-Metodo de Pago menos usado: tarjeta - $1000')
    info_ventas.update({'metodo_menos_usado':metodo_menos_usado[0]})
    
    return info_ventas


def estadisticas_generales():
    limpiar_consola()
    print('|###--··  TecStore  ··--###|')
    print('|##·· Estadisticas de Productos')
    stats_prod=estadisticas_productos()
    print(f'|-Cantidad de Productos: {len(productos)} ')
    print(f'|-Cantidad total de Productos: {stats_prod['cantidad_existencias']} - capital: $ {stats_prod['capital_neto']}')
    print(f'|-Producto con mas Stock: {stats_prod['prod_stock_bajo']['nombre']} - stock: {stats_prod['prod_stock_bajo']['stock']}')
    print(f'|-Producto con menos Stock: {stats_prod['prod_stock_alto']['nombre']} - stock: {stats_prod['prod_stock_alto']['stock']}')
    
    print('|##················································')
    print('|##·· Estadisticas de Ventas')
    stats_vent=estadisticas_ventas()
    print(f'|-Cantidad de ventas: {stats_vent['cantidad_venta']} - ${stats_vent['cantidad_ganancia']}')
    print(f'|-Producto Mas Vendido: {mostrar_un_prod(int(stats_vent['prod_mas_vendidos'][0]))['nombre']} - ventas: {stats_vent["prod_mas_vendidos"][1]}')
    print(f'|-Producto Menos Vendido: {mostrar_un_prod(int(stats_vent['prod_menos_vendidos'][0]))['nombre']} - ventas: {stats_vent["prod_menos_vendidos"][1]}')
    print(f'|-Metodo de Pago mas usado: {stats_vent['metodo_mas_usado'][0]} - ${stats_vent['metodo_mas_usado'][1][1]}')
    print(f'|-Metodo de Pago menos usado: {stats_vent['metodo_menos_usado'][0]} - ${stats_vent['metodo_menos_usado'][1][1]}')
    print(f'|##················································')


while True:
    limpiar_consola()
    print('|###--··  TecStore  ··--###|')
    print('|##······················##|')
    print('| 1 ) --- Agregar Producto') 
    print('| 2 ) --- Mostrar Productos')
    print('| 3 ) --- Modificar Stock') 
    print('| 4 ) --- Realizar Venta')
    print('| 5 ) --- Mostrar Ventas')
    print('| 6 ) --- Buscar Producto')
    print('| 7 ) --- Eliminar Producto')
    print('| 8 ) --- Estadisticas de Ventas')
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
        case "8":
            estadisticas_generales()
        case "0":
            print('Saliendo.....')
            break
        case _:
            print('Ingrese una opcion valida!')
    
    input('precione una tecla para continuar!')

