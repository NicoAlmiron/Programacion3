import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
#lo anterior se realiza para poder limpiar la consola

#Diccionarios
# Productos
#      "id" - entero - 6 bits
#  "nombre" - string - 30 bits
#  "precio" - flotante (99999999.99) - 11 bits
#   "stock" - entero - 4 bits
#1     |cosme fulanito               |25000.00   |20  |     


producto = {}


productos = [
    # {
    #     "id": 1,
    #     "nombre": "teclado mecanico",
    #     "precio": 150000,
    #     "stock": 8
    # },
    # {
    #     "id": 2,
    #     "nombre": "mouse gamer RGB",
    #     "precio": 50000,
    #     "stock": 9
    # },
    # {
    #     "id": 3,
    #     "nombre": "prueba",
    #     "precio": 90000,
    #     "stock": 10
    # }
]

def extraer_productos():

    registros = []

    with open('Productos.txt', 'r', encoding='UTF-8') as file:
        registros = file.readlines()
        if len(registros) <= 0:
            return
        for reg in registros:
            producto ={
                "id": int(reg[0:6]),
                "nombre": reg[7:36].strip('  '),
                "precio": float(reg[38:48]),
                "stock": int(reg[50:53]),
                }
            productos.append(producto)


def escribir_producto(producto):
    with open('Productos.txt', 'a', encoding='UTF-8') as arch_prod:
        reg_prod = ""
        reg_prod += f"{producto['id']}{(" " * ( 6 - len(str(producto['id'])) ) )}|" # id producto
        reg_prod += f"{producto['nombre']}{(" " * ( 30 - len(producto['nombre']) ) )}|" # nombre
        reg_prod += f"{producto['precio']}{(" " * ( 11 - len(str(producto['precio'])) ) )}|" # precio
        reg_prod += f"{producto['stock']}{(" " * ( 4 - len(str(producto['stock'])) ) )}|\n" # stock
        arch_prod.write(reg_prod)




def reescribir_productos_archivo():
    with open('Productos.txt', 'w', encoding='UTF-8') as arch_prod:
        for producto in productos:
            reg_prod = ""
            reg_prod += f"{producto['id']}{(" " * ( 6 - len(str(producto['id'])) ) )}|" # id producto
            reg_prod += f"{producto['nombre']}{(" " * ( 30 - len(producto['nombre']) ) )}|" # nombre
            reg_prod += f"{producto['precio']}{(" " * ( 11 - len(str(producto['precio'])) ) )}|" # precio
            reg_prod += f"{producto['stock']}{(" " * ( 4 - len(str(producto['stock'])) ) )}|\n" # stock
            arch_prod.write(reg_prod)


# ventas = [
#     {
#         "id_venta": 1,
#         "detalle_venta": {
#             1 : (2, 300000),
#             2 : (1, 50000)
#         },
#         "importe_total": 350000,
#         "forma_pago": 'Efectivo'
#     },
#     {
#         "id_venta": 2,
#         "detalle_venta": {
#             2 : (1, 50000)
#         },
#         "importe_total": 50000,
#         "forma_pago": 'Tarjeta'
#     },
# ]

#Diccionarios
# Venta
#       "id_venta" - entero - 10 bits
#  "importe_total" - flotante (999,999,999.9) - 11 bits
#     "forma_pago" - string - 13 bits
#1         |500000.0   |Transferencia|
 
# "id_detalle_venta" - entero - 11 bits (se conforma por id_venta mas id_producto por ejemplo el id_detalle_venta seria: '10' + '6' = 106)

# Detalles_Ventas
#      "id_venta" - entero - 6 bits
#      "id_producto" - entero - 6 bits
#         "cantidad" - entero - 3 bits
#         "subtotal" - flotante (99999999.99) - 11 bits
#1     |2     |2  |300000.0   |

venta = {}

ventas = [
    # {
    #     "id_venta": 1,
    #     "detalle_venta": [
    #     {
    #         'id_producto' : 1,
    #         'detalle_prod' : 
    #         {
    #             'cantidad': 2,
    #             'sub_total': 300000       
    #         },
    #     },
    #     {
    #         'id_producto' : 2,
    #         'detalle_prod' :
    #         {
    #             'cantidad': 1,
    #             'sub_total': 50000                
    #         },
    #     }],
    #     "importe_total": 350000,
    #     "forma_pago": 'Efectivo',
    # },
    # {
    #     "id_venta": 2,
    #     "detalle_venta": [{
    #         'id_producto': 1,
    #         'detalle_prod':
    #         {
    #                'cantidad': 1,
    #                'sub_total': 50  
    #         }              
    #        }],
    #     "importe_total": 50000,
    #     "forma_pago": 'Tarjeta'
    # },
]

#Diccionarios
# Venta
#       "id_venta" - entero - 10 bits
#  "importe_total" - flotante (999,999,999.9) - 11 bits
#     "forma_pago" - string - 13 bits
#1         |500000.0   |Transferencia|

#Detalles_Ventas
#      "id_venta" - entero - 10 bits
#      "id_producto" - entero - 6 bits
#         "cantidad" - entero - 3 bits
#         "subtotal" - flotante (99999999.99) - 11 bits
#1     |2     |2  |300000.0   |

detalle_venta = {}

def extraer_ventas():

    ventas_arch = []
    detalles_ventas = []

    with open('venta.txt', 'r', encoding='UTF-8') as arch_venta, open('detalles_ventas.txt', 'r', encoding='UTF-8') as arch_detalle_venta:
        ventas_arch = arch_venta.readlines()
        detalles_ventas = arch_detalle_venta.readlines()
        if len(ventas_arch) <= 0:
            return 
        for venta_item in ventas_arch:
            venta ={
                "id_venta": int(venta_item[0:9]),
                "detalle_venta": [],
                "importe_total": float(venta_item[11:21]),
                "forma_pago": venta_item[23:36].strip('  ')
                }
            
            
            for det_vent in detalles_ventas:
                if int(det_vent[0:5]) == venta['id_venta']:
                    #print(f"{int(det_vent[0:5])} -  {venta['id_venta']}")
                    detalle_venta = {
                        'id_producto': int(det_vent[7:12]),
                        'detalle_prod':
                        {
                               'cantidad': int(det_vent[14:16]),
                               'sub_total': float(det_vent[18:29])  
                        }              
                    }
                    venta['detalle_venta'].append(detalle_venta)
                    
            ventas.append(venta)


def escribir_venta(venta):
    with open('venta.txt', 'a', encoding='UTF-8') as arch_venta, open('detalles_ventas.txt', 'a', encoding='UTF-8') as arch_detalle_venta:
 
        reg_vent = ""
        reg_vent += f"{venta['id_venta']}{(" " * ( 10 - len(str(venta['id_venta'])) ) )}|" # id venta
        reg_vent += f"{venta['importe_total']}{(" " * ( 11 - len(str(venta['importe_total'])) ) )}|" # nombre
        reg_vent += f"{venta['forma_pago']}{(" " * ( 13 - len(venta['forma_pago']) ) )}|\n"# precio
        arch_venta.write(reg_vent)
        for det_venta in venta['detalle_venta']:
            reg_det_vent = ""
            reg_det_vent += f"{venta['id_venta']}{(" " * ( 10 - len(str(venta['id_venta'])) ) )}|" # id venta
            reg_det_vent += f"{det_venta['id_producto']}{(" " * ( 6 - len(str(det_venta['id_producto'])) ) )}|" # id producto
            reg_det_vent += f"{det_venta['detalle_prod']['cantidad']}{(" " * ( 3 - len(str(det_venta['detalle_prod']['cantidad'])) ) )}|" # cantidad
            reg_det_vent += f"{det_venta['detalle_prod']['sub_total']}{(" " * ( 11 - len(str(det_venta['detalle_prod']['sub_total'])) ) )}|\n" # subtotal
            arch_detalle_venta.write(reg_det_vent)


metodos_pago = ("Efectivo", "Transferencia", "Tarjeta")

def agregar_prod():
    producto = {}
    print('|###--··  TecStore  ··--###|')
    print('|##-· Producto Nuevo')
    ultima_pocicion =  len(productos)-1
    producto['id'] = productos[ultima_pocicion]['id'] + 1
    print(f'|##-· Producto ID: {producto['id']}')
    producto['nombre'] = input('|-Nobre del articulo: ').lower()
    producto['precio'] = float(input('|-Precio: $'))
    producto['stock'] = int(input('|-Stock Inicial: '))

    productos.append(producto)
    escribir_producto(producto)
    print("Se Guardo el producto exitosamente!")


def mod_prod():
    producto = {}
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
    reescribir_productos_archivo()

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
        renglon = f'|ID: {producto['id']}{(" " * ( 6 - len(str(producto['id'])) ) )}'
        renglon += f'| {producto['nombre']}{(" " * ( 30 - len(producto['nombre']) ) )}'
        renglon += f'| ${producto['precio']}{(" " * ( 11 - len(str(producto['precio'])) ) )}'
        renglon += f'| STOCK: {producto['stock']}'
        if int(producto['stock']) < 4:
            renglon += '(STOCK BAJO)'
        elif int(producto['stock']) == 0:
            renglon += '(SIN STOCK!!*!*!*!)'
        print(renglon)

def mostrar_un_prod(id):
    encontrado = False
    for producto in productos:
        if producto['id'] == id:
            encontrado = True
            return producto
    if encontrado is False : return False

def descontar_stock(id,cantidad):
    for producto in productos:
        for clave, valor in producto.items():
            if clave == 'id' and valor == id:
                producto['stock'] = producto['stock'] - cantidad


def realizar_venta():
    descuento = False
    venta = {}
    list_venta = []
    print('|###--··  TecStore  ··--###|')
    listar_productos()
    total_venta = 0
    while True:
        print('|##-· Ingrese el Id del producto o Dejar vacio para continuar')
        id_v = input('|##-· ID: ')
        if id_v.lower() == '':
            break
        for producto in productos:
            if int(id_v) == producto['id']:
                cant = 1
                cant = int(input('|##-· Cantidad: '))
                if producto['stock'] > 0:
                    v = {
                            'cantidad': cant,
                            'sub_total': (producto['precio'] * cant)  
                        }
                    total_venta = total_venta + (producto['precio'] * cant)
                    #producto['stock'] = producto['stock'] - cant
                    prod_venta = {
                        'id_producto': producto['id'],
                        'detalle_prod': v
                    }
                    list_venta.append(prod_venta)
                else:
                    print('|# Producto Sin Stock')
                print(f'|#-{producto['nombre']} x {cant} Agregado a la compra')        
    venta["importe_total"] = total_venta
    if len(list_venta) > 0:
        venta['id_venta'] = len(ventas) + 1
        venta['detalle_venta'] = list_venta
        while True:
            print('|##-· Para continuar, ingrese la forma de pago')
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
            

            if opc == "1":
                desc = float(input('|#  ·Descuento: %'))
                venta['importe_total'] = float(venta['importe_total'])-(float(venta['importe_total'])*(desc/100))
                print(f'|-----------Importe Total ${total_venta} ')
                print(f'|-----------Importe con Descuento ${venta['importe_total']} ')
                descuento = True
                break
            elif opc == "2":
                desc = float(input('|#  ·Descuento: $'))
                venta['importe_total'] = venta['importe_total'] - desc
                print(f'|-----------Importe Total ${total_venta} ')
                print(f'|-----------Importe con Descuento ${venta['importe_total']} ')
                descuento = True
                break
            elif opc == "0":
                print(f'|-----------Importe Actual ${venta['importe_total']}')
                break
            else:
                print(f'|# No se indico una opcion valida!')

        
        for prod_v in list_venta:
            descontar_stock(prod_v['id_producto'],prod_v['detalle_prod']['cantidad'])
        ventas.append(venta)
        escribir_venta(venta)
        print("|##·· Se realizo la venta exitosamente! ··##|")
        print('|# Resumen de la venta!')
        print('|- Productos')
        print('|········································')
        for prodc_v in venta['detalle_venta']:
            producto = mostrar_un_prod(prodc_v['id_producto'])
            print(f'|{producto['nombre']} - precio unitario ${producto['precio']} ')
            print(f'|\t\tx {prodc_v['detalle_prod']['cantidad']} - SubTotal ${prodc_v['detalle_prod']['sub_total']} ')
            print('|········································')
        print(f'|- Total: ${total_venta}')
        if descuento : print(f'|- Total(Descuento): ${venta['importe_total']}')
        print(f'|- Forma de pago: {venta['forma_pago']}')


        
def listar_ventas():
    print('|# Lista de Ventas')
    if len(ventas) == 0:
        print('|  ·No se emcontraron ventas!')
        return
    for venta in ventas:
        print(f'o- Venta Nroº: {venta['id_venta']}')
        print(' - Productos:')
        for prod_vent in venta['detalle_venta']:
            for producto in productos:
                if producto['id'] == prod_vent['id_producto']:
                    print(f'     ·{producto['nombre']}{(" " * ( 30 - len(producto['nombre']) ) )}- ${producto['precio']}{(" " * ( 11 - len(str(producto['precio'])) ) )} - x {prod_vent['detalle_prod']['cantidad']} - SubTotal ${prod_vent['detalle_prod']['sub_total']} ')
        print(f' - Total: ${venta['importe_total']}')
        print(f' - Forma de pago: {venta['forma_pago']}')
        print('-········································')




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

    ganancias_totales = 0
    #ganancias_netas = 0

    metodos_contados = {
        # 'efectivo':{
        #  'veces_usado' : 4
        #  'importe_metodo' : 70000
        # }
    }

    prod_vendidos = {
        # 3 : {
        #     # 'nombre' : 'prueba',
        #     # 'cantidad_vendidos': 5
        # }
    }
    

    # {
#         "id_venta": 2,
#         "detalle_venta": [{
#             'id_producto': 1,
#             'detalle_prod':
#             {
#                    'cantidad': 1,
#                    'sub_total': 50  
#             }              
#            }],
#         "importe_total": 50000,
#         "forma_pago": 'Tarjeta'
#     },

    for venta in ventas:
        cant_ganancias = cant_ganancias + float(venta['importe_total'])
        for prod_det_vent in venta['detalle_venta']:
            p = {}
            nombre = ""
            cant_prod_v = 0
        
        ganancias_totales = + ganancias_totales

        for clave, valor in prod_vendidos.items():
            if clave == 'id_prod' and prod_det_vent['id_producto'] == valor:
                cant_prod_v = int(prod_vendidos['cantidad_vendidos']) + int(prod_det_vent['detalle_prod']['cantidad'])

        if cant_prod_v == 0:
            cant_prod_v = int(prod_det_vent['detalle_prod']['cantidad'])
        nombre = mostrar_un_prod(prod_det_vent['id_producto'])['nombre']

        p = {
            prod_det_vent['id_producto']:{
                'nombre': nombre,
                'cantidad_vendidos': cant_prod_v
            }
        }
        prod_vendidos.update(p)

          
        forma_p = ""
        metodo = {}
        cont_metodo = 0
        importe_metodo = 0
        if venta['forma_pago'] in metodos_contados:
            forma_p = venta['forma_pago']
            for clave, valor in metodos_contados[forma_p].items():
                if clave == 'veces_usado':
                    cont_metodo = valor + 1
                elif clave == 'importe_metodo':
                    importe_metodo = valor + venta['importe_total']
        else:
            forma_p = venta['forma_pago']
            metodo = {}
            cont_metodo = 1
            importe_metodo = venta['importe_total']
        
        metodo.update({'veces_usado':cont_metodo})
        metodo.update({'importe_metodo':importe_metodo})

        metodos_contados.update({venta['forma_pago']:metodo})

    prod_menos_vendido = []
    prod_mas_vendido = []
    prod_menos_vendido = sorted(prod_vendidos.items(), key=lambda prod: prod[1]['cantidad_vendidos'])
    prod_mas_vendido = sorted(prod_vendidos.items(), key=lambda prod: prod[1]['cantidad_vendidos'], reverse=True)
    # print(prod_menos_vendido)
    # print(prod_mas_vendido)


    metodo_menos_usado = []
    metodo_mas_usado = []
    metodo_menos_usado = sorted(metodos_contados.items(), key=lambda metodo: metodo[1]['veces_usado'])
    metodo_mas_usado = sorted(metodos_contados.items(), key=lambda metodo: metodo[1]['veces_usado'], reverse=True)
    # print(metodo_menos_usado)
    # print(metodo_mas_usado)

    metodo_mas_recaudado= []
    metodo_menos_recaudado= []
    metodo_mas_recaudado= sorted(metodos_contados.items(), key=lambda metodo: metodo[1]['importe_metodo'])
    metodo_menos_recaudado = sorted(metodos_contados.items(), key=lambda metodo: metodo[1]['importe_metodo'], reverse=True)
    # print(metodo_menos_recaudado)
    # print(metodo_mas_recaudado)


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


    # print('|-Metodo de Pago que mas recaudo: efectivo - $99999')
    info_ventas.update({'metodo_mas_recaudado':metodo_mas_recaudado[0]})
    # print('|-Metodo de Pago que menos recaudo: tarjeta - $1000')
    info_ventas.update({'metodo_menos_recaudado':metodo_menos_recaudado[0]})

    return info_ventas


def estadisticas_generales():
    limpiar_consola()
    print('|###--··  TecStore  ··--###|')
    stats_prod=estadisticas_productos()
    stats_vent=estadisticas_ventas()
    print('|##·· Estadisticas Generales')
    print(f'|-Cantidad de productos registrados: {len(productos)}')
    print(f'|-Cantidad de Ventas Totales: {stats_vent['cantidad_venta']} - Recaudado: ${stats_vent['cantidad_ganancia']}')
    print('|')
    print('|##·· Estadisticas Productos')
    print(f'|-Producto Mas Vendido: {stats_vent['prod_mas_vendidos'][1]['nombre']} - vendidos: {stats_vent["prod_mas_vendidos"][1]['cantidad_vendidos']}')
    print(f'|-Producto Menos Vendido: {stats_vent['prod_menos_vendidos'][1]['nombre']} - vendidos: {stats_vent["prod_menos_vendidos"][1]['cantidad_vendidos']}')
    print('|')
    print('|##·· Estadisticas Stock')
    print(f'|-Cantidad total de Productos: {stats_prod['cantidad_existencias']} - capital: $ {stats_prod['capital_neto']}')
    print(f'|-Producto con mas Stock: {stats_prod['prod_stock_bajo']['nombre']} - stock: {stats_prod['prod_stock_bajo']['stock']}')
    print(f'|-Producto con menos Stock: {stats_prod['prod_stock_alto']['nombre']} - stock: {stats_prod['prod_stock_alto']['stock']}')
    print('|')
    print('|##·· Estadisticas Metodos de Pago')
    print(f'|-Mas usado: {stats_vent['metodo_mas_usado'][0]} ({stats_vent['metodo_mas_usado'][1]['veces_usado']} veces) - ${stats_vent['metodo_mas_usado'][1]['importe_metodo']}')
    print(f'|-Menos usado: {stats_vent['metodo_menos_usado'][0]} ({stats_vent['metodo_menos_usado'][1]['veces_usado']} veces) - ${stats_vent['metodo_menos_usado'][1]['importe_metodo']}')
    print(f'|-Metodo que mas recaudo: {stats_vent['metodo_mas_recaudado'][0]} - ${stats_vent['metodo_mas_recaudado'][1]['importe_metodo']}')
    print(f'|-Metodo que menos recaudo: {stats_vent['metodo_menos_recaudado'][0]} - ${stats_vent['metodo_menos_recaudado'][1]['importe_metodo']}')
    print('|##················································')

def sincronisar_datos():
    extraer_productos()
    extraer_ventas()


sincronisar_datos()
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

