# Ejercicio 9
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por
# pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes
# se introduzcan con un solo carácter.

fechaNacimineto = input('Ingrese el fecha de nacimineto (DD/MM/AAAA): ')

fechaDesglozada = fechaNacimineto.split('/')

print('Dia: '+fechaDesglozada[0])
print('Mes: '+fechaDesglozada[1])
print('Año: '+fechaDesglozada[2])