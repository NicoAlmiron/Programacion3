# Ejercicio 4
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el có
# digo del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que
# pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo
# y la extensión.

telefono = input("Ingrese el nombre del telefono: ")

#ultimosNumeros = telefono[len(telefono)-2]+telefono[len(telefono)-1]

#numeroSolo = telefono.split('+34')[1].split(ultimosNumeros)[0]
#numeroSolo = telefono.split('+34')[1].replace(ultimosNumeros,"")
##numeroSolo = telefono.split('+34')[1].rstrip(ultimosNumeros)

#print(numeroSolo)

#https://www.w3schools.com/python/python_strings_methods.asp

#Solucion

print('El telefono es: ', telefono[3:-2])