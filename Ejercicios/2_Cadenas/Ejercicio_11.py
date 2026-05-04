# Ejercicio 11
# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por
# pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decima
# les, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.


nombre = input("Ingrese nombre del producto: ")
precio = input("Ingrese precio del producto: $")
cantidad = input("Ingrese cantidad: ")
importe = str(float(precio)*int(cantidad))
importe = importe.split('.')
precio = precio.split('.')

com = 6 - len(precio[0])

if com > 0:
    precio[0] = '0'*com + precio[0]

    precio[1] = precio[1][:2]

if len(cantidad)<3:
    cantidad = '0'*(3-len(cantidad))+cantidad

if len(importe[0])<8:
    importe[0] = '0'*(8-len(importe[0]))+importe[0]

if len(importe[1])<2:
    importe[1] = "0"*(2-len(importe[1]))+importe[1]
else:
    importe[1] = importe[1][:2]

print(nombre + ' Precio $' + precio[0] + "."+ precio[1] + "C/U - Cantidad " + cantidad +
      " - Importe $" + importe[0] + "."+importe[1])