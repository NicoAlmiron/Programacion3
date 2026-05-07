# 4. Escriba un algoritmo que ingrese un importe en pesos y muestre por pantalla su equivalente a
# Dólares, Euros y Reales, pero previamente debe mostrar un menú donde el usuario pueda elegir
# el tipo de conversión.

EUR = 1639.20
USD = 1401.99
BRL = 281.19

pesos = round(float(input('Ingrese el importe en pesos: $')),2)

print('$'+str(pesos)+' a Dolares -> $'+str(round(pesos / USD,2))+'USD')
print('$'+str(pesos)+' a Euros -> $'+str(round(pesos / EUR,2))+'EUR')
print('$'+str(pesos)+' a Reales -> $'+str(round(pesos / BRL,2))+'BRL')