# 16. Escriba un programa donde el usuario ingrese un numero entero y muestre por pantalla todos
# los números que van desde el 1 hasta el numero ingresado. Cuando termine la secuencia de
# mostrar los números por pantalla el programa deberá preguntar si desea salir introduciendo
# otro número con 0(SI) y 1(NO)

opcion = 0

while opcion == 0:
    x = int(input("Ingrese un numero: "))
    for n in range(1,x+1):
        print(n)
    opcion = int(input("quiere ingresar otro numero (0(SI) - 1(NO)): "))
    if opcion == 1:
        break

# AprendePython_SergioDelgadoQuintero.pdf - pagina 127 libro - pagina 131 pdf