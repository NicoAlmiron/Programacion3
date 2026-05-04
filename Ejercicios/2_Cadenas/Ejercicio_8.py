# Ejercicio 8
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre
# por pantalla el número de euros y el número de céntimos del precio introducido.

precio = input('Introduzca el precio: $')

precioDesglosado = precio.split('.')

print('El precio es de ' + precioDesglosado[0] + ' Euros con ' + precioDesglosado[1] + ' centimos')