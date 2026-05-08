# 20. Escriba un programa que pueda sumar y restar dos números hasta que alguno de ellos sea igual
# a cero.

while True:
    print('Ingrese dos numeros - (0 para salir)')
    num1 = int(input('Numero 1: '))
    if num1 == 0:
        break
    num2 = int(input('Numero 2: '))
    if num2 == 0:
        break
    print('La suma es: ', num1 + num2, ' y la resta', num1 - num2)
