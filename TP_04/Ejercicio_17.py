# 17. Escriba un programa donde el usuario pueda ingresar N cantidad de números y muestre por
# pantalla si número es módulo de 2, de 3 o de 4 hasta que el usuario ingrese el numero 0(cero)
# para salir del programa.


opcion = 0

while opcion == 0:
    x = int(input("Ingrese un numero: "))
    if x % 2 == 0 and x % 3 == 0 and x % 4 == 0:
        print("Es multiplo de 2, 3 y 4")
    elif x % 2 == 0 and x % 3 == 0:
        print("Es multiplo de 2 y 3")
    elif x % 2 == 0 and x % 4 == 0:
        print("Es multiplo de 2 y 4")
    elif x % 2 == 0:
        print("Es multiplo de 2")
    elif x % 3 == 0 and x % 4 == 0:
        print("Es multiplo de 3 y 4")
    elif x % 3 == 0:
        print("Es multiplo de 3")
    elif x % 4 == 0:
        print("Es multiplo de 4")
    opcion = int(input("quiere ingresar otro numero (0(SI) - 1(NO)): "))
    if opcion == 1:
        break