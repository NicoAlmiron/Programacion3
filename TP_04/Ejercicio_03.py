# 3. Tengo la siguiente función matemática:
# f(x) =3x -2
# Deberá escribir un programa que realice el cálculo de la función, teniendo en cuenta los
# siguientes puntos:
#  La  función deberá ingresar al menos 5 valores para X para obtener los resultados de
# y=f(x)
#  Los valores ingresados pueden ser enteros o números con dos decimales únicamente,
# los cuales también pueden ser negativos.
#  Los resultados de la función deben ser impresos por pantalla en el siguiente formato(es
# un ejemplo a modo ilustrativo):
# x y=f(x)
# 1 4
# 8 10 -5 -45
# 2,23 4,87
# 7 14

x1 = round(float(input('Introduce un numero para X1: ')),2)
x2 = round(float(input('Introduce un numero para X2: ')),2)
x3 = round(float(input('Introduce un numero para X3: ')),2)
x4 = round(float(input('Introduce un numero para X4: ')),2)
x5 = round(float(input('Introduce un numero para X5: ')),2)

resX1 = (3 * x1) - 2
resX2 = (3 * x2) - 2
resX3 = (3 * x3) - 2
resX4 = (3 * x4) - 2
resX5 = (3 * x5) - 2

print('Resultados de la funcion con las X')
print('  X  | y = f(x)')
print(' '+str(x1)+'  |  '+str(resX1))
print(' '+str(x2)+'  |  '+str(resX2))
print(' '+str(x3)+'  |  '+str(resX3))
print(' '+str(x4)+'  |  '+str(resX4))
print(' '+str(x5)+'  |  '+str(resX5))