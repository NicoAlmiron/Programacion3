# 11. Escriba un programa donde el usuario pueda ingresar dos números y el programa verifique si
# esos dos números son múltiplos de 2 o de 3. Si el usuario ingresa un número superior a 50
# tendrá que mostrar un mensaje donde indique que no se puede hacer los cálculos.

print('ingrese dos numeros entre 1 y 50')
num1 = int(input('ingrese un numero: '))
num2 = int(input('ingrese otro numero: '))

if num2 < 51 and num1 < 51:
    if num2 % 2 == 0 and num1 % 2 == 0:
        print('los dos numeros son multiplos de 2')
    elif num2 % 2 == 0:
        print('El segundo numero es multiplo de 2')
    elif num1 % 2 == 0:
        print('El primer numero es multiplo de 2')

    if num2 % 3 == 0 and num1 % 3 == 0:
        print('los dos numeros son multiplos de 3')
    elif num2 % 3 == 0:
        print('El segundo numero es multiplo de 3')
    elif num1 % 3 == 0:
        print('El primer numero es multiplo de 3')
else:
    print('se ingreso un numero fuera del limite')
