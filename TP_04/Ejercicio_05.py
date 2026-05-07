# 5. Escriba un programa que pregunte al usuario el momento del día con una letra (M-mañana, T
# Tarde, N-Noche), el sexo con otra letra (M-Masculino, F-Femenino). El programa dirá: Buenos
# días, tarde, o noches (según el momento) señor o señora según el sexo.

dia = input('Ingrese el momento del dia (M - T - N): ').lower()
sexo = input('Ingrese el sexo (F - M): ').lower()
cadena = ""
if sexo == 'f':
    cadena = "Señora"
elif sexo == 'm':
    cadena = "Señor"

if dia == 'm':
    print('Buenos dias '+cadena+'!')
elif dia == 't':
    print('Buenas tardes '+cadena+'!')
elif dia == 'n':
    print('Buenas noches '+cadena+'!')