# 14. Escriba un programa donde el usuario pueda ingresar un número entero, donde ese número
# entero será el tope del incremento de una variable X empezando desde el número 1. El
# programa deberá mostrar por pantalla el valor de la variable hasta el tope del incremento
# ingresado por el usuario. La variable debe incrementarse en dos unidades por vez.

maxX = int(input("Ingrese el tope: "))

for n in range(1,maxX+1,2):
    print("X: "+str(n))
