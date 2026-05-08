# 18. Escriba un programa que simule una calculadora de la siguiente manera: el usuario podrá
# ingresar dos números enteros y una vez ingresados esos número deberá mostrar por pantalla el
# siguiente menú: (S) SUMA – (R) RESTA – (M) MULTIPLICAION – (D) DIVISION – (X) Salir.
# Una vez ingresado la opción el programa deberá mostrar por pantalla el resultado de la opción
# ingresada hasta que el usuario ingrese la letra (X) de salir.


flag = 0

while flag == 0:
    print('  ---### Calculadora ###---')
    opcion = ''
    print('Ingrese dos numeros')
    num1 = int(input("\tNumero 1: "))
    num2 = int(input("\tNumero 2: "))
    print('OPERACIONES: (S) SUMA – (R) RESTA – (M) MULTIPLICAION – (D) DIVICION – (X) Salir')
    opcion = input('Ingrese una Operacion: ').upper()

    if opcion == 'X':
        print('Saliendo....')
        flag = 1
        break

    resultado = None

    match opcion:
        case 'S':
            resultado = num1 + num2
            print('Resultado: ' + str(resultado))
        case 'R':
            resultado = num1 - num2
            print('Resultado: ' + str(resultado))
        case 'M':
            resultado = num1 * num2
            print('Resultado: ' + str(resultado))
        case 'D':
            if num2 == 0:
                resultado = 'no se puede dividir por 0!'
            else:
                resultado = num1 / num2
            print('Resultado: ' + str(resultado))
        # case 'X':
        #     print('Saliendo')
        #     flag = 1
        case _:
            print('Ingrese una Operacion valida!')

    #
    # if opcion == 'S':
    #     resultado = num1 + num2
    # elif opcion == 'R':
    #     resultado = num1 - num2
    # elif opcion == 'M':
    #     resultado = num1 * num2
    # elif opcion == 'D' and num2 != 0:
    #     resultado = num1 / num2
    # elif opcion == 'D' and num2 == 0:
    #     resultado = 'no se puede dividir por 0!'
    # else:
    #     print('Ingrese una Operacion valida!')
    #     break


    #
    # if opcion == 'X':
    #     print('Saliendo!...')
    #     break