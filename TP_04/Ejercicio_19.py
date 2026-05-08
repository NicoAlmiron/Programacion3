# 19. Escriba un programa donde muestre el siguiente menú con las cinco vocales(A – E –I –O-U).El
# usuario deberá poder ingresar esas vocales y el programa responderá por pantalla si es una
# vocal abierta o cerrada hasta que el usuario ingrese la letra (S) para salir del programa y
# terminar con su ejecución.

while True:
    print('VOCALES | A - E - I - O - U | S - Salir')
    vocal = input('Ingrese vocal: ').upper()
    match vocal:
        case 'A':
            print('La vocal es abierta')
        case 'E':
            print('La vocal es abierta')
        case 'I':
            print('La vocal es cerrada')
        case 'O':
            print('La vocal es abierta')
        case 'U':
            print('La vocal es cerrada')
        case 'S':
            print('Saliendo....')
            break