# 9. Escribir un programa que simule la comanda de una pizzería, donde el mozo pueda ingresar el
# número de porciones de pizzas (nº superior de 1 a 8) y el precio de la porción. Considerar lo
# siguiente:
#  Si son entre 1 y 3 porciones debe hacer un descuento del 5%
#  Si son entre 4 y 6 porciones debe hacer un descuento del 7%
#  Si son 7 u 8 porciones debe hacer un descuento del 9%
# El programa deberá mostrar por pantalla la cantidad de porciones, el precio de cada porción, el
# precio total de todas las porciones y el precio total con el descuento.

print('#### Pizzeria Gurmello ####')
cantPorciones = int(input('Digite la cantidad de Porciones: '))
precioXPorc = round(float(input('Ingrese el precio de la porcion: ')),2)
precioTotal = round(precioXPorc * cantPorciones)
precioFinal = 0;

if cantPorciones > 0 and cantPorciones < 4:
    precioFinal = precioTotal - (precioTotal * 0.05)
elif cantPorciones > 3 and cantPorciones < 7:
    precioFinal = precioTotal - (precioTotal * 0.07)
elif cantPorciones > 6 and cantPorciones < 9:
    precioFinal = precioTotal - (precioTotal * 0.09)

print('\t ### Cantidad de Porciones: '+str (cantPorciones))
print('\t ### Precio Unitario $'+str(precioXPorc))
print('\t ### Precio Total $'+str(precioTotal))
print('\t ### Precio Final (condescuento) $'+str(precioFinal))