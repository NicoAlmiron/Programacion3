# Ejercicio 9
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y
# muestre por pantalla el capital obtenido en la inversión.

invercion = int(input('ingrese el monto a invertir: $'))

interesA = float(input('ingrese el porcentaje de interes anual: %'))

cantAños = int(input('ingrese la cantidad de Años: '))

capitalGenerado = (invercion * ((interesA+100)/100)) * cantAños

print('El capital generado es: $'+str(capitalGenerado))