# 2. Escriba un programa donde un usuario puede ingresar el precio de un artículo (el precio es con
# dos decimales) y una determinada cantidad de ese artículo. El programa deberá calcular lo
# siguiente:
#   a) Si la cantidad es inferior o igual a 5 unidades el precio del artículo será el el mismo que el
#   ingresado por el usuario
#   b) Si la cantidad es superior a 5 unidades e inferior a 10 unidades tendrá un descuento del
#   5%
#   c) Y si la cantidad ingresada es superior a 20 unidades, aparte del descuento del 5%
#   anterior tendrá otro descuento del 10% más.
# El programa imprimirá por pantalla: el precio unitario, el precio total por la cantidad ingresada
# sin el descuento y el precio total con el descuento incluido.

precio = float(input("Ingrese el precio del producto ($0.00): "))
cantidad = int(input("Ingrese la cantidad: "))
precioTotal = cantidad * precio;
precioDescuento = precioTotal;


if cantidad > 5 and cantidad < 10:
    precioDescuento = precioTotal - (precioTotal*0.05)
elif cantidad > 20:
    precioDescuento = precioTotal - ((precioTotal - (precioTotal*0.05))*0.1)

print(' -Precio por Unidad: $' + str(round(precio, 2)))
print(' -Precio Total: $' + str(round(precioTotal,2)) + " x " + str(cantidad) + ' unidades')
print(' -Precio con Descuento: $' + str(round(precioDescuento,2)))