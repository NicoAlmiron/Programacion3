# Ejercicio 6

# Escribir un programa que lea un entero positivo, , introducido por el usuario y después muestre en pantalla la
# suma de todos los enteros desde 1 hasta .

nUsuario = int(input('ingrese un numero: '))

#suma = 0
#for _ in range(nUsuario):
#    suma += _
#
#print(suma + nUsuario)

suma = (nUsuario * (nUsuario + 1)) / 2
print(suma)
