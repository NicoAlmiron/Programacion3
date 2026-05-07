# 8. Escribir un programa donde el usuario pueda ingresar un número del 1 al 7 de acuerdo al día de
# la semana y muestre que día en letras ingreso. Por ejemplo si ingresa 1(Lunes) o si ingresa
# 3(Miércoles). Considere que el usuario no puede ingresar otros valores diferentes entre 1 y 7.

opcion = int(input('digite un dia de la semana con el numero correspondiente (1 - 7): '))

if opcion == 1:
    print('\t- Lunes')
elif opcion == 2:
    print('\t- Martes')
elif opcion == 3:
    print('\t- Miercoles')
elif opcion == 4:
    print('\t- Jueves')
elif opcion == 5:
    print('\t- Viernes')
elif opcion == 6:
    print('\t- Sabado')
elif opcion == 7:
    print('\t- Domingo')
else:
    print('\t- Dia incorrecto')