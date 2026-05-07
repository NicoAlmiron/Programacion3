# 7. Escriba un algoritmo que muestre un menú de ABM y muestre por pantalla la opción
# seleccionada. La selección de las opciones debe hacer un algoritmo con opciones numéricas y
# otras con opciones de caracteres o letras. Aclaración: debe considerar en ambos casos la
# posibilidad que el usuario ingrese una opción invalida

print('----#### Gestion de productos ------')
print('\t( A - 1 ) - Alta de Producto')
print('\t( B - 2 ) - Baja de Producto')
print('\t( M - 3 ) - Modificacion de Producto')
opcion = input('\t#Opcion: ')

if opcion.upper() == 'A' or int(opcion) == 1:
    print('\t\t## Alta de Producto----')
elif opcion.upper() == 'B' or int(opcion) == 2:
    print('\t\t## Baja de Producto----')
elif opcion.upper() == 'C' or int(opcion) == 3:
    print('\t\t## Modificacion de Producto----')
else:
    print('\t\t## Opcion invalida----')