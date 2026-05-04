# Ejercicio 10
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la
# empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñe
# cas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa
# que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que
# será enviado.


PAYASO = 112

MUÑECA = 75

print('-- Juegueteria -- | Ultimo Pedido')
cantPayasos = int(input('# Cantidad vendida de Payasos: '))

cantMuñecas = int(input('# Cantidad vendida de Muñecas: '))

pesoTotal = ((cantMuñecas * MUÑECA) + (cantPayasos * PAYASO)) / 1000
#pesoTotal = (cantMuñecas * MUÑECA) + (cantPayasos * PAYASO)
#
#if pesoTotal > 1000:
#    print('El peso total del pedido es de: ' + str(pesoTotal/1000) + 'Kg')
#else:
#    print('El peso total del pedido es de: ' + str(pesoTotal) + 'g')

print('El peso total del pedido es de: ' + str(pesoTotal) + 'Kg')