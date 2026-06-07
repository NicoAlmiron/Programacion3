import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
#lo anterior se realiza para poder limpiar la consola


materias = ( "Programacion", "Matematica", "Ingles", "Base de datos")

alumno = {}

notas = {}

alumnos = [
    {
        "idAlumno": 0,
        "dni": "40200300",
        "nombre": "Juancito Fulanito",
        "notas": {
            "Programacion": [8,9,10],
            "Matematica": [7,6],
        }
    },
    {
        "idAlumno": 1,
        "dni": "10500400",
        "nombre": "Carlitos Pepito",
        "notas": {
            "Ingles": [4,5,3],
            "Matematica": [8,6],
            "Base de datos": [10,6,6]
        }
    },
    {
        "idAlumno": 2,
        "dni": "111",
        "nombre": "cosme fulanito",
        "notas": {
            "Programacion": [4,1,3],
            "Matematica": [3,2],
            "Base de datos": [2,3,1]
        }
    }
]



def listar_alumnos():
    print('|-|-|-|-|-|## CONTROL DE ALUMNOS ##|-|-|-|-|-|')
    print('|#| Listado de Alumnos |#|')
    for alumno in alumnos: # Se recorre la lista de alumnos
        print(f'|#|Alumno Nroº {alumno.get('idAlumno')} ------------------')
        print(f'|#|\t-Nombre: {alumno.get('nombre')}')
        print(f'|#|\t-DNI: {alumno.get('dni')}')
        print('|#|\t-Notas:') 
        for key, value in alumno['notas'].items(): # aqui se recorre el diccionario "notas"
            print(f'|#|\t  {key}: {value}')
            
    #input('|#| Pulse cualquier tecla para continuar....')


def registrar_alumno():
    limpiar_consola()
    print('|-|-|-|-|-|## CONTROL DE ALUMNOS ##|-|-|-|-|-|')
    print('|#| Registro de Alumnos |#|')
    print('|#|-- Ingrese los datos del alumno')
    
    alumno['idAlumno'] = len(alumnos)

    alumno['nombre'] = input('#Nombre: ')
    alumno['dni'] = input('#DNI: ')
    alumno['notas'] = {}

    alumnos.append(alumno)
    print(f'|#| El alumno se guardo correctamente!!!! ')

def cargar_notas():
    limpiar_consola()
    print('|-|-|-|-|-|## CONTROL DE ALUMNOS ##|-|-|-|-|-|')
    print('|#| Registro de Notas de los Alumnos |#|')
    print('|#|-- Ingrese el dni del alumno')
    dni = input('|# DNI: ')

    for alumno in alumnos: #busco en la lista de alumnos
        for clave, valor in alumno.items(): # aqui busco dato por dato de cada alumno
            if clave == 'dni' and dni == valor: #cyuando encuentro la clave dni comparo con el dni ingresado el valor de esa clave
                mat = []
                if len(alumno['notas']) > 0:
                      
                    notas = alumno['notas'] 
                    for clave in alumno['notas'].keys():
                        if clave == materias[0]:
                            mat.append(1)
                        elif clave == materias[1]:
                            mat.append(2)
                        elif clave == materias[2]:
                            mat.append(3)
                        elif clave == materias[3]:
                            mat.append(4)
                else:
                    notas = {}

                print('|#|-- Ingrese las materias')
                i = 0
                while i < 5:
                    limpiar_consola()
                    cadena1 = '|1| Programacion - |2| Matematica'
                    cadena2 = '|3| Ingles   -  |4| Base de datos'
                    
                    #Este sistema permite ver en "tiempo real que materias esta eligiendo"
                    print('|#-- Ingrese las materias')
                    if 1 in mat: # detecto cuales materias ya se ingresaron
                        if 2 in mat:
                            print(cadena1.replace("1","#").replace("2","#")) # luego se las remplaza individualmente en la cadena 
                        else:
                            print(cadena1.replace("1","#"))
                    elif 2 in mat:
                        print(cadena1.replace("2","#"))
                    else:
                        print(cadena1)
                    
                    if 3 in mat:
                        if 4 in mat:
                            print(cadena2.replace(("3"),"#").replace("4","#"))
                        else:
                            print(cadena2.replace("3","#"))
                    elif 4 in mat:
                        print(cadena2.replace("4","#"))
                    else:
                        print(cadena2)

                    print('    |0| Guardar y Salir')

                    op = input('\n|#|--: ')

                    
                    # Switch de decicion para elegir la opcion
                    match op:
                        case '1': # en caso de elegir programacion

                            nota = []
                            if 1 in mat:
                                print(f'|#| Ya se ingresaron notas!')
                                print(f'|#| desea sobrescribir las notas (S/N)?:  ')
                                op = input('Confirmacion: ')
                                if op.lower() == 'n':
                                    break
                                print(f'|#| Ingrese las notas. Precione N para salir')
                                n = 1
                                while n < 4: # recorro 3 posisciones indicando que la primera pertenece al 1er parcial, la segunda al segundo y la ultima al final
                                    n_provisoria = input(f'| {n}º Nota: ')
                                    if n_provisoria != "N" and n_provisoria != "n": # identifico la bandera de salida
                                        nota.append(int(n_provisoria)) # convierto a entero, igualmente fallara si no se coloca un try catch por fallo de convercion si se ingresa un string
                                        n += 1
                                    else: 
                                        break
                                notas.update({'Programacion': nota})
                                print(f'|#| Las notas se sobrescribieron correctamente')
                            else:
                                print(f'|#| Programacion')
                                print(f'|#| Ingrese las notas. Precione N para salir')
                                n = 1
                                while n < 4: # recorro 3 posisciones indicando que la primera pertenece al 1er parcial, la segunda al segundo y la ultima al final
                                    n_provisoria = input(f'| {n}º Nota: ')
                                    if n_provisoria != "N" and n_provisoria != "n": # identifico la bandera de salida
                                        nota.append(int(n_provisoria)) # convierto a entero, igualmente fallara si no se coloca un try catch por fallo de convercion si se ingresa un string
                                        n += 1
                                    else: 
                                        break
                                notas.update({'Programacion': nota})
                                print(f'|#| Las notas se guardaron correctamente')
                                mat.append(1) # registro el ingreso de esta materia
                        case "2": # Matematica
                            nota = []
                            if 2 in mat:
                                print(f'|#| Ya se ingresaron notas!')
                                print(f'|#| desea sobrescribir las notas (S/N)?:  ')
                                op = input('Confirmacion: ')
                                if op.lower() == 'n':
                                    break
                                print(f'|#| Ingrese las notas. Precione N para salir')
                                n = 1
                                while n < 4: # recorro 3 posisciones indicando que la primera pertenece al 1er parcial, la segunda al segundo y la ultima al final
                                    n_provisoria = input(f'| {n}º Nota: ')
                                    if n_provisoria != "N" and n_provisoria != "n": # identifico la bandera de salida
                                        nota.append(int(n_provisoria)) # convierto a entero, igualmente fallara si no se coloca un try catch por fallo de convercion si se ingresa un string
                                        n += 1
                                    else: 
                                        break
                                notas.update({'Matematica': nota})
                                print(f'|#| Las notas se sobrescribieron correctamente')
                            else:
                                print(f'|#| Matematicas')
                                print(f'|#| Ingrese las notas. Precione N para salir')
                                n = 1
                                while n < 4:
                                    n_provisoria = input(f'| {n}º Nota: ')
                                    if n_provisoria != "N" and n_provisoria != "n": # identifico la bandera de salida
                                        nota.append(int(n_provisoria)) # convierto a entero, igualmente fallara si no se coloca un try catch por fallo de convercion si se ingresa un string
                                        n += 1
                                    else: 
                                        break
                                notas.update({'Matematica': nota})
                                print(f'|#| Las notas se guardaron correctamente')
                                mat.append(2)
                        case "3": # Ingles
                            nota = []
                            if 3 in mat:
                                print(f'|#| Ya se ingresaron notas!')
                                print(f'|#| desea sobrescribir las notas (S/N)?:  ')
                                op = input('Confirmacion: ')
                                if op.lower() == 'n':
                                    break
                                print(f'|#| Ingrese las notas. Precione N para salir')
                                n = 1
                                while n < 4: # recorro 3 posisciones indicando que la primera pertenece al 1er parcial, la segunda al segundo y la ultima al final
                                    n_provisoria = input(f'| {n}º Nota: ')
                                    if n_provisoria != "N" and n_provisoria != "n": # identifico la bandera de salida
                                        nota.append(int(n_provisoria)) # convierto a entero, igualmente fallara si no se coloca un try catch por fallo de convercion si se ingresa un string
                                        n += 1
                                    else: 
                                        break
                                notas.update({'Ingles': nota})
                                print(f'|#| Las notas se sobrescribieron correctamente')
                            else:
                                print(f'|#| Ingles')
                                print(f'|#| Ingrese las notas. Precione N para salir')
                                n = 1
                                while n < 4:
                                    n_provisoria = input(f'| {n}º Nota: ')
                                    if n_provisoria != "N" and n_provisoria != "n": # identifico la bandera de salida
                                        nota.append(int(n_provisoria)) # convierto a entero, igualmente fallara si no se coloca un try catch por fallo de convercion si se ingresa un string
                                        n += 1
                                    else: 
                                        break
                                notas.update({'Ingles': nota})
                                print(f'|#| Las notas se guardaron correctamente')
                                mat.append(3)
                        case "4": # base de datos
                            nota = []
                            if 4 in mat:
                                print(f'|#| Ya se ingresaron notas!')
                                print(f'|#| desea sobrescribir las notas (S/N)?:  ')
                                op = input('Confirmacion: ')
                                if op.lower() == 'n':
                                    break
                                print(f'|#| Ingrese las notas. Precione N para salir')
                                n = 1
                                while n < 4: # recorro 3 posisciones indicando que la primera pertenece al 1er parcial, la segunda al segundo y la ultima al final
                                    n_provisoria = input(f'| {n}º Nota: ')
                                    if n_provisoria != "N" and n_provisoria != "n": # identifico la bandera de salida
                                        nota.append(int(n_provisoria)) # convierto a entero, igualmente fallara si no se coloca un try catch por fallo de convercion si se ingresa un string
                                        n += 1
                                    else: 
                                        break
                                notas.update({'Base de datos': nota})
                                print(f'|#| Las notas se sobrescribieron correctamente')
                            else:
                                print(f'|#| Base de Datos')
                                print(f'|#| Ingrese las notas. Precione N para salir')
                                n = 1
                                while n < 4:
                                    n_provisoria = input(f'| {n}º Nota: ')
                                    if n_provisoria != "N" and n_provisoria != "n": # identifico la bandera de salida
                                        nota.append(int(n_provisoria)) # convierto a entero, igualmente fallara si no se coloca un try catch por fallo de convercion si se ingresa un string
                                        n += 1
                                    else: 
                                        break
                                notas.update({'Base de datos': nota})
                                print(f'|#| Las notas se guardaron correctamente')
                                mat.append(4)
                        case "0": 
                            print('|#| SALIENDO.....')
                            break
                        case _:
                            print('|#|*** INGRESE UNA OPCION VALIDA ***|#|')

                    input('|#| Pulse cualquier tecla para continuar....')
                    i += 1
                alumno['notas'] = notas
                input('|#| Se guardaron las notas exitosamente')

    
def calcular_promedios():
    while True:
            
        limpiar_consola()
        print('|-|-|-|-|-|## CONTROL DE ALUMNOS ##|-|-|-|-|-|')
        print('|#| Calculadora de promedios |#|')
        print('|#| ( 1 ) -----> Listar alumnos con promedios')
        print('|#| ( 2 ) -----> Promedio de un alumno')
        print('|#| ( 3 ) -----> Lista con promedios generales')
        print('|#| ( 4 ) -----> Promedio mas alto y bajo')
        print('|#| ( 0 ) -----> Salir')
        
        opcion = input('|#| OPCION ------------: ')

        limpiar_consola()
        match opcion:
            case "1": 
                print('|#| Listado de Promedios |#|')
                for alumno in alumnos: # Se recorre la lista de alumnos
                    print(f'|#|Alumno Nroº {alumno.get('idAlumno')} ------------------')
                    print(f'|#|\t-Nombre: {alumno.get('nombre')}')
                    print(f'|#|\t-DNI: {alumno.get('dni')}')
                    print('|#|\t-Promedios:') 
                    for key, value in alumno['notas'].items(): # aqui se recorre el diccionario "notas"
                        prom = sum(value) / len(value)
                        print(f'|#|\t  {key}: {prom}')
            case "2":
                print('|#| Promedio de Alumno |#|')
                print('|#-- Ingrese el DNI del alumno')
                dni = input('|#| DNI: ')
                for alumno in alumnos: # Se recorre la lista de alumnos
                    for clave, valor in alumno.items():
                        if clave == 'dni' and valor == dni:
                            print(f'|#|Alumno Nroº {alumno.get('idAlumno')} ------------------')
                            print(f'|#|\t-Nombre: {alumno.get('nombre')}')
                            print(f'|#|\t-DNI: {alumno.get('dni')}')
                            print('|#|\t-Promedios:') 
                            for key, value in alumno['notas'].items(): # aqui se recorre el diccionario "notas"
                                prom = sum(value) / len(value)
                                print(f'|#|\t  {key}: {prom}')
            case "3":
                print('|#| Listado de Promedios |#|')
                for alumno in alumnos: # Se recorre la lista de alumnos
                    promGeneral = 0
                    print(f'|#|Alumno Nroº {alumno.get('idAlumno')} ------------------')
                    print(f'|#|\t-Nombre: {alumno.get('nombre')}')
                    print(f'|#|\t-DNI: {alumno.get('dni')}')
                    tot = 0
                    for value in alumno['notas'].values(): # aqui se recorre el diccionario "notas"
                        tot += sum(value) / len(value)
                    
                    promGeneral = tot / len(alumno['notas'])
                    print(f'|#|\t-Promedio: {promGeneral}') 
            case "4": 
                print('|#| Promedio Mas Alto y Mas Bajo |#|')

                # Promedio mas bajo
                print('|# Mas Bajo ----------------')
                promMasBajo = sorted(alumnos, key=lambda alum:  (   #utilizo la funcion sorted para crear una lista nueva ordenada
                                    sum(   #realizo la sumatoria de notas del alumno
                                        nota   # parametro que se sumara en la funcion sumatoria
                                        for materia in alum['notas'].values()
                                           for nota in materia
                                        )                                     
                                    ) 
                                    / 
                                    sum(
                                        len(materia) #pa
                                        for materia in alum['notas'].values()
                                    ) 
                                )   
                print(f'|#|Alumno Nroº {promMasBajo[0].get('idAlumno')} ------------------')
                print(f'|#|\t-Nombre: {promMasBajo[0].get('nombre')}')
                print(f'|#|\t-DNI: {promMasBajo[0].get('dni')}')
                tot = 0
                for value in promMasBajo[0]['notas'].values(): # aqui se recorre el diccionario "notas"
                    tot += sum(value) / len(value)
                promGeneral = tot / len(promMasBajo[0]['notas'])
                print(f'|#|\t-Promedio: {promGeneral}')


                # Promedio mas alto
                print('|# Mas Alto ----------------')
                promMasAlto = sorted(alumnos, key=lambda alum:  (   #utilizo la funcion sorted para crear una lista nueva ordenada
                                    sum(   #realizo la sumatoria de notas del alumno
                                        nota   # parametro que se sumara en la funcion sumatoria
                                        for materia in alum['notas'].values()
                                           for nota in materia
                                        )                                     
                                    ) 
                                    / 
                                    sum(
                                        len(materia) #pa
                                        for materia in alum['notas'].values()
                                    ) 
                                    , reverse=True
                                )           
                promGeneral = 0
                print(f'|#|Alumno Nroº {promMasAlto[0].get('idAlumno')} ------------------')
                print(f'|#|\t-Nombre: {promMasAlto[0].get('nombre')}')
                print(f'|#|\t-DNI: {promMasAlto[0].get('dni')}')
                tot = 0
                for value in promMasAlto[0]['notas'].values(): # aqui se recorre el diccionario "notas"
                    tot += sum(value) / len(value)
                promGeneral = tot / len(promMasAlto[0]['notas'])
                print(f'|#|\t-Promedio: {promGeneral}')

            case "0": 
                print('|#| SALIENDO.....')
                break
            case _:
                print('|#|*** INGRESE UNA OPCION VALIDA ***|#|')
        input('|#| Pulse cualquier tecla para continuar....')

def buscar_alumno():
    while True:
        limpiar_consola()
        print('|-|-|-|-|-|## CONTROL DE ALUMNOS ##|-|-|-|-|-|')
        print('|#| Buscador de Alumnos |#|')
        print('|#| ( 1 ) --> Por DNI')
        print('|#| ( 2 ) --> Por Nombre')
        print('|#| ( 3 ) --> Por Materia')
        print('|#| ( 0 ) --> Salir')
        
        opcion = input('|#| OPCION ------------: ')
        limpiar_consola()
        match opcion:
            case "1":
                print('|#-- Ingrese el DNI del alumno')
                dni = input('|#| DNI: ')
                for alumno in alumnos: # Se recorre la lista de alumnos
                    for clave, valor in alumno.items():
                        if clave == 'dni' and valor == dni:
                            print(f'|#|Alumno Nroº {alumno.get('idAlumno')} ------------------')
                            print(f'|#|\t-Nombre: {alumno.get('nombre')}')
                            print(f'|#|\t-DNI: {alumno.get('dni')}')
                            print('|#|\t-Promedios:') 
                            for key, value in alumno['notas'].items(): # aqui se recorre el diccionario "notas"
                                prom = sum(value) / len(value)
                                print(f'|#|\t  {key}: {prom}')
            case "2":
                print('|#-- Ingrese el Nombre del alumno')
                nombre = input('|#| Nombre: ')
                for alumno in alumnos: # Se recorre la lista de alumnos
                    for clave, valor in alumno.items():
                        if clave == 'nombre' and valor == nombre:
                            print(f'|#|Alumno Nroº {alumno.get('idAlumno')} ------------------')
                            print(f'|#|\t-Nombre: {alumno.get('nombre')}')
                            print(f'|#|\t-DNI: {alumno.get('dni')}')
                            print('|#|\t-Promedios:') 
                            for key, value in alumno['notas'].items(): # aqui se recorre el diccionario "notas"
                                prom = sum(value) / len(value)
                                print(f'|#|\t  {key}: {prom}')
            case "3":
                print('|#-- Ingrese la Materia')
                
                print('|#| (1) - Programacion | (2) - Matematica')
                print('|#| (3) - Ingles       | (4) - Base de Datos')
                op =  input('|# Materia: ')
                limpiar_consola()
                if type(op) != int:
                    print('Ingrese un numero')

                materia = materias[int(op )-1]
                print(f'|#-- {materia} ----------')
                for alumno in alumnos: # Se recorre la lista de alumnos
                    for key in alumno['notas'].keys(): # aqui se recorre el diccionario "notas"
                            if key.lower() == materia.lower():
                                print(f'|#|Alumno Nroº {alumno.get('idAlumno')} ------------------')
                                print(f'|#|\t-Nombre: {alumno.get('nombre')}')
                                print(f'|#|\t-DNI: {alumno.get('dni')}')
                                print('|#|\t-Promedios:') 
                                for key, value in alumno['notas'].items():
                                    if key.lower() == materia.lower():
                                        prom = sum(value) / len(value)
                                        print(f'|#|\t  {key}: {prom}')

            case "0": 
                print('|#| SALIENDO.....')
                break
            case _:
                print('|#|*** INGRESE UNA OPCION VALIDA ***|#|')
        input('|#| Pulse cualquier tecla para continuar....')

def alumnos_aprobados():
    while True:
        limpiar_consola()
        print('|-|-|-|-|-|## CONTROL DE ALUMNOS ##|-|-|-|-|-|')
        print('|#| Alumnos Aprobados |#|')
        print('|#| ( 1 ) --> Listar Todos los Aprobados')
        print('|#| ( 2 ) --> Buscar Alumo Aprobado')
        print('|#| ( 0 ) --> Salir')
        
        opcion = input('|#| OPCION ------------: ')
        match opcion:
            case "1":
                print('|#-- Lista de Alumnos con sus Materias Aprobadas')
                for alumno in alumnos: # Se recorre la lista de alumnos
                    bandera = [] # coloco una lista para verificar que se muestren las materias correspondiente
                    cadena = '| El Alumno '+ alumno['nombre'] + ' aprobo:'
                    for key, value in alumno['notas'].items(): # aqui se recorre el diccionario "notas"
                        prom = sum(value) / len(value)
                        if prom >= 6:
                            cadena += " - "+key
                            bandera.append(True)
                        else:
                            bandera.append(False)
                    if True in bandera:
                        print(cadena)
                    
                    
            case "2":
                print('|#-- Ingrese el DNI del alumno')
                dni = input('|#| DNI: ')
                for alumno in alumnos: # Se recorre la lista de alumnos
                    bandera = []
                    if alumno['dni'] == dni:
                        #for clave, valor in alumno.items():
                        cadena = '| El Alumno '+ alumno['nombre'] + ' aprobo:'
                        #    if clave == 'notas':
                        for key, value in alumno['notas'].items(): # aqui se recorre el diccionario "notas"
                            prom = sum(value) / len(value)
                            if prom >= 6:
                                cadena += " - "+ key
                                bandera.append(True)
                            else:
                                bandera.append(False)
                if True in bandera:
                    print(cadena) 
                else:
                    print('| No se contro notas aprobadas') 
            case "0": 
                print('|#| SALIENDO.....')
                break
            case _:
                print('|#|*** INGRESE UNA OPCION VALIDA ***|#|')

        input('|#| Pulse cualquier tecla para continuar....')


def alumnos_desaprobados():
    while True:
        limpiar_consola()
        print('|-|-|-|-|-|## CONTROL DE ALUMNOS ##|-|-|-|-|-|')
        print('|#| Alumnos Desaprobados |#|')
        print('|#| ( 1 ) --> Listar Todos los Desaprobados')
        print('|#| ( 2 ) --> Buscar Alumno Desaprobados')
        print('|#| ( 0 ) --> Salir')
        
        opcion = input('|#| OPCION ------------: ')
        match opcion:
            case "1":
                print('|#-- Lista de Alumnos con sus Materias Desaprobadas')
                for alumno in alumnos: # Se recorre la lista de alumnos
                    bandera = []
                    cadena = '| El Alumno '+ alumno['nombre'] + ' desaprobo:'
                    for key, value in alumno['notas'].items(): # aqui se recorre el diccionario "notas"
                        prom = sum(value) / len(value)
                        if prom < 6:
                            cadena += " - " + key
                            bandera.append(True)
                        else:
                            bandera.append(False)
                    if True in bandera:
                        print(cadena)
                    
                    
            case "2":
                print('|#-- Ingrese el DNI del alumno')
                dni = input('|#| DNI: ')
                for alumno in alumnos: # Se recorre la lista de alumnos
                    bandera = []
                    if alumno['dni'] == dni:
                        #for clave, valor in alumno.items():
                        cadena = '| El Alumno '+ alumno['nombre'] + ' desaprobo:'
                        #    if clave == 'notas':
                        for key, value in alumno['notas'].items(): # aqui se recorre el diccionario "notas"
                            prom = sum(value) / len(value)
                            if prom < 6:
                                cadena += " - "+ key
                                bandera.append(True)
                            else:
                                bandera.append(False)
                if True in bandera: # si existe algun valor verdadero en la lista, muestra la cadena
                    print(cadena) 
                else:
                    print('| No se contro notas desaprobadas') 
            case "0": 
                print('|#| SALIENDO.....')
                break
            case _:
                print('|#|*** INGRESE UNA OPCION VALIDA ***|#|')

        input('|#| Pulse cualquier tecla para continuar....')


    

# Se inicia un bucle que contendra el menu interactivo
while True: 
    limpiar_consola() # Cada vez que entre en el bucle se va a limpiar la consola

    # Menu de opciones
    print('|-|-|-|-|-|## CONTROL DE ALUMNOS ##|-|-|-|-|-|')
    print('|#| ( 1 ) -----> Registrar Alumnos')
    print('|#| ( 2 ) -----> Cargar Notas')
    print('|#| ( 3 ) -----> Mostrar Alumnos')
    print('|#| ( 4 ) -----> Calcular Promedios')
    print('|#| ( 5 ) -----> Buscar Alumno')
    print('|#| ( 6 ) -----> Mostrar Aprobados')
    print('|#| ( 7 ) -----> Mostrar Desprobados')
    print('|#| ( 0 ) -----> Salir')
    
    opcion = input('|#| OPCION ------------: ')

    # Switch para elegir la opcion
    match  opcion:
            case "1": 
                registrar_alumno()
            case "2":
                cargar_notas()
            case "3":
                listar_alumnos()
            case "4": 
                calcular_promedios()
            case "5":
                buscar_alumno()
            case "6":
                alumnos_aprobados()
            case "7":
                alumnos_desaprobados()
            case "0": 
                print('|#| SALIENDO.....')
                break
            case _:
                print('|#|*** INGRESE UNA OPCION VALIDA ***|#|')

    input('|#| Pulse cualquier tecla para continuar....')