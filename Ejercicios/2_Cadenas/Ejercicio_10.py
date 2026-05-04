# Ejercicio 10
# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por co
# mas, y muestre por pantalla cada uno de los productos en una línea distinta.

listaCompras = " " + input('ingrese la lista de compra, separando los productos por una coma "," \nlista de compras: ')

listaDesglosada = listaCompras.split(',')

for i in range(len(listaDesglosada)):
    print("+" + listaDesglosada[i])

print('Fin de la lista')