# Ejercicio 12
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir
# un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe
# mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

BPAN = 3.49

cantBarr = int(input('Cuantas Barras de pan de ayer se vendio? \nBarras de pan: '))

print('Precio Total: $' + str(round(cantBarr * BPAN, 2)))
print('Precio Final: $' + str(round((cantBarr * BPAN)-((cantBarr * BPAN)*0.6), 2)))
print('(El pan que no es el día tiene un descuento del 60%)')