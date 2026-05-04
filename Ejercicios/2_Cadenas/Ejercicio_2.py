# Ejercicio 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla
# el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayús
# culas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su
# nombre combinando mayúsculas y minúsculas como quiera.

nombre = input('ingrese nombre: ')

nombreMin = nombre.casefold()
nombreMax = nombre.upper()
nombreFormal =nombre.title()

print(nombreMin)
print(nombreMax)
print(nombreFormal)


# https://www.w3schools.com/python/python_strings_methods.asp