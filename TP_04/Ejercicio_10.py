# 10. Escriba un programa donde el usuario pueda ingresar la primera inicial de su signo del zodiaco.
# Luego del ingreso de la primera letra de su signo zodiacal (Tener en cuenta que hay varios
# signos que empiezan con la misma letra), debe ingresar su fecha de nacimiento (dd/mm/aaaa) y
# mostrar por pantalla su signo zodiacal (nombre completo) y el mes de su cumpleaños.

print('~~## Codigos del Zodiaco ##~~')
inicial = input('\t Inicial del Zodiaco: ')
fechaNacimiento = input('\t Fecha de Nacimiento (DD/MM/AAAA): ')

fecha_Formateada = fechaNacimiento.split('/')
fecha_Formateada[1] = int(fecha_Formateada[1])

if inicial.upper() == 'A':
    if fecha_Formateada[1] > 0 and fecha_Formateada[1] < 3:
        if fecha_Formateada[1] == 1:
            print('\t Signo: Acuario, Mes: Enero')
        elif fecha_Formateada[1] == 2:
            print('\t Signo: Acuario, Mes: Febrero')
    elif fecha_Formateada[1] > 2 and fecha_Formateada[1] < 5:
        if fecha_Formateada[1] == 3:
            print('\t Signo: Aries, Mes: Marzo')
        elif fecha_Formateada[1] == 4:
            print('\t Signo: Aries, Mes: Abril')
elif inicial.upper() == 'C':
    if fecha_Formateada[1] > 5 and fecha_Formateada[1] < 8:
        if fecha_Formateada[1] == 6:
            print('\t Signo: Cancer, Mes: Junio')
        elif fecha_Formateada[1] == 7:
            print('\t Signo: Cancer, Mes: Julio')
    elif fecha_Formateada[1] == 12 or fecha_Formateada[1] == 1:
        if fecha_Formateada[1] == 12:
            print('\t Signo: Capricornio, Mes: Diciembre')
        elif fecha_Formateada[1] == 1:
            print('\t Signo: Capricornio, Mes: Enero')
elif inicial.upper() == 'E':
    if fecha_Formateada[1] > 9 and fecha_Formateada[1] < 12:
        if fecha_Formateada[1] == 10:
            print('\t Signo: Escorpio, Mes: Octubre')
        elif fecha_Formateada[1] == 11:
            print('\t Signo: Escorpio, Mes: Noviembre')
elif inicial.upper() == 'G':
    if fecha_Formateada[1] > 4 and fecha_Formateada[1] < 8:
        if fecha_Formateada[1] == 5:
            print('\t Signo: Geminis, Mes: Mayo')
        elif fecha_Formateada[1] == 6:
            print('\t Signo: Geminis, Mes: Junio')
elif inicial.upper() == 'L':
    if fecha_Formateada[1] > 6 and fecha_Formateada[1] < 9:
        if fecha_Formateada[1] == 7:
            print('\t Signo: Leo, Mes: Julio')
        elif fecha_Formateada[1] == 8:
            print('\t Signo: Leo, Mes: Agosto')
    elif fecha_Formateada[1] == 8 or fecha_Formateada[1] == 11:
        if fecha_Formateada[1] == 9:
            print('\t Signo: Capricornio, Mes: Septiembre')
        elif fecha_Formateada[1] == 10:
            print('\t Signo: Capricornio, Mes: Octubre')
elif inicial.upper() == 'P':
    if fecha_Formateada[1] > 1 and fecha_Formateada[1] < 4:
        if fecha_Formateada[1] == 2:
            print('\t Signo: Piscis, Mes: Febrero')
        elif fecha_Formateada[1] == 3:
            print('\t Signo: Piscis, Mes: Marzo')
elif inicial.upper() == 'S':
    if fecha_Formateada[1] > 10 and fecha_Formateada[1] < 13:
        if fecha_Formateada[1] == 11:
            print('\t Signo: Sagitario, Mes: Noviembre')
        elif fecha_Formateada[1] == 12:
            print('\t Signo: Sagitario, Mes: Diciembre')
elif inicial.upper() == 'T':
    if fecha_Formateada[1] > 3 and fecha_Formateada[1] < 6:
        if fecha_Formateada[1] == 4:
            print('\t Signo: Tauro, Mes: Abril')
        elif fecha_Formateada[1] == 5:
            print('\t Signo: Tauro, Mes: Mayo')
elif inicial.upper() == 'V':
    if fecha_Formateada[1] > 7 and fecha_Formateada[1] < 10:
        if fecha_Formateada[1] == 8:
            print('\t Signo: Virgo, Mes: Agosto')
        elif fecha_Formateada[1] == 9:
            print('\t Signo: Virgo, Mes: Septiembre')
