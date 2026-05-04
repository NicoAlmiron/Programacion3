# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por panta
# lla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = input('ingrese nombre: ')
cant = int(input('ingrese un numero entero: '))

for _ in range(cant):
    print(nombre)