# 1. Escriba en lenguaje C los siguientes algoritmos:
#   a) Ingrese un número y muestre por pantalla si es positivo.
#   b) Ingrese un número y si es 0(cero) muestre por pantalla un error.
#   c) Ingrese un número y muestre por pantalla un mensaje si es PAR o IMPAR.
#   d) Ingrese dos números y muestre por pantalla el Mayor de ellos dos.
#   e) Ingrese un vocal y muestre un mensaje si es Abierta o Cerrada.
#   f) Ingrese un número del 1 al 7 y muestre por cada número el correspondiente día de la
#       semana.
#   g) Ingrese un número del 1 al 12 y muestre por cada número el correspondiente mes del
#       año.
#   h) Ingrese un número por pantalla, identifique si es positivo y muestre por pantalla si es par
#       o impar.

num = int(input("Ingrese un numero: "))

print("El numero ingresado ")
# a)
if num > 0:
    print(" - es positivo")
# b)
elif num == 0:
    print(" - es negativo")
# c)
if num % 2 == 0:
    print(" - es par")
elif num % 2 != 0:
    print(" - es impar")
# d)
num2 = int(input("Ingrese otro numero: "))
if num2 > num:
    print("El segundo numero es mayor")
elif num2 < num:
    print("El primer numero es mayor")
# e)
vocal = input("Ingrese una vocal: ").lower()
if vocal == "a" :
    print("El vocal ingresada es Abierta")
elif vocal == "e":
    print("El vocal ingresada es Abierta")
elif vocal == "o":
    print("El vocal ingresada es Abierta")
elif vocal == "i":
    print("El vocal ingresada es Cerrada")
elif vocal == "u":
    print("El vocal ingresada es Cerrada")

# f)

dia = int(input("Ingrese un numero (del 1 al 7): "))


if dia == 1:
    print("El dia Elegido Es Lunes")
elif dia == 2:
    print("El dia Elegido Es Martes")
elif dia == 3:
    print("El dia Elegido Es Miercoles")
elif dia == 4:
    print("El dia Elegido Es Jueves")
elif dia == 5:
    print("El dia Elegido Es Viernes")
elif dia == 6:
    print("El dia Elegido Es Sabado")
elif dia == 7:
    print("El dia Elegido Es Domingo")
else:
    print("por favor siga las instrucciones...")

# g)
mes = int(input("Ingrese un numero (del 1 al 12): "))


if mes == 1:
    print("El mes Elegido fue Enero")
elif mes == 2:
    print("El mes Elegido fue Febrero")
elif mes == 3:
    print("El mes Elegido fue Marzo")
elif mes == 4:
    print("El mes Elegido fue Abril")
elif mes == 5:
    print("El mes Elegido fue Mayo")
elif mes == 6:
    print("El mes Elegido fue Junio")
elif mes == 7:
    print("El mes Elegido fue Julio")
elif mes == 8:
    print("El mes Elegido fue Agosto")
elif mes == 9:
    print("El mes Elegido fue Septiembre")
elif mes == 10:
    print("El mes Elegido fue Octubre")
elif mes == 11:
    print("El mes Elegido fue Noviembre")
elif mes == 12:
    print("El mes Elegido fue Diciembre")
else:
    print("por favor siga las instrucciones...")