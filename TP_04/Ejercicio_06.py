# 6. Escriba un algoritmo que simule una calculadora de la siguiente manera: el usuario podrá
# ingresar dos números enteros o reales y una vez ingresados esos número deberá mostrar por
# pantalla el siguiente menú: (S) SUMA – (R) RESTA – (M) MULTIPLICAION – (D) DIVISION. Una vez
# ingresado la opción el algoritmo deberá mostrar por pantalla el resultado de la opción
# ingresada.

num1 = float(input('digite el primer numero: '))
num2 = float(input('digite el segundo numero: '))

print('Operaciones: (S) SUMA – (R) RESTA – (M) MULTIPLICAION – (D) DIVISION')
operacion = input('digite operacion: ').upper()
if operacion == 'S':
    suma = num1 + num2
    print('La suma es: '+str(suma))
elif operacion == 'R':
    resta = num1 - num2
    print('La resta es: '+str(resta))
elif operacion == 'M':
    multiplicacion = num1 * num2
    print('La multiplicacion es: '+str(multiplicacion))
elif operacion == 'D':
    division = num1 / num2
    print('La division es: '+str(division))