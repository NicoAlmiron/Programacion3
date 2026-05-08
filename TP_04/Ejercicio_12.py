# 12. Escriba un programa donde el usuario pueda ingresar dos números enteros, considerando que
# el primer número ingresado sea menor que el segundo. El programa deberá mostrar todos los
# números existentes entre esos dos números ingresados.

print('ingrese un rango de numeros')
menor = int(input('ingrese el limite menor: '))
mayor = int(input('ingrese el limite mayor: '))

if menor > mayor:
    print('el menor es mayor!')
else:
    for i in range(menor,mayor+1):
        print('\t'+str(i))