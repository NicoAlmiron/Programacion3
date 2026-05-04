# Ejercicio 11
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros de
# bido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Es
# cribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida
# por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer,
# segundo y tercer años. Redondear cada cantidad a dos decimales.


ahorros = float(input('ingrese la cantidad de ahorros: '))
INTERESES = 1.04
firstYear = ahorros * INTERESES
twoYears = firstYear * INTERESES
treeYears = twoYears * INTERESES

print('Primer Año - Ahorros: $' + str(round(firstYear, 2)))
print('Segundo Año - Ahorros: $' + str(round(twoYears, 2)))
print('Tercer Año - Ahorros: $' + str(round(treeYears, 2)))