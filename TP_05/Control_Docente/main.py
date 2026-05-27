import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
#lo anterior se realiza para poder limpiar la consola


materias = ("Matematicas", "Programacion", "Ingles", "Base de datos")

alumno = {}

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
    }
]



def listar_Alumnos():
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
    print('|-|-|-|-|-|## CONTROL DE ALUMNOS ##|-|-|-|-|-|')
    print('|#| Registro de Alumnos |#|')
    print('|#|-- Ingrese los datos del alumno')
    
    alumno['idAlumno'] = len(alumnos)

    alumno['nombre'] = input('#Nombre: ')
    alumno['dni'] = input('#DNI: ')

    print('|#|-- Ingrese las materias')
    i = 0

    mat = []
    while i < 5:

        cadena1 = '|1| Programacion - |2| Matematica'
        cadena2 = '|3| Ingles   -  |4| Base de datos'
        
        #Este sistema permite ver en "tiempo real que materias esta eligiendo"
        print('|#|-- Ingrese las materias')
        if "1" in mat:
            if "2" in mat:
                print(cadena1.replace(("1", "2"),"#"))
            print(cadena1.replace("1","#"))
        elif "2" in mat:
            print(cadena1.replace("2","#"))
        
        if "3" in mat:
            if "4" in mat:
                print(cadena2.replace(("3", "4"),"#"))
            print(cadena2.replace("3","#"))
        elif "4" in mat:
            print(cadena2.replace("4","#"))

        print('        |0| Salir')

        op = input('\n|#|--: ')
        mat.append(op)

        match op:
            case '1':
                if "1" in mat:
                    print("ya se ingreso")
                else:
                    alumno['notas'] # ingreso de notas
            case "2":
                print('programacion')
            case "3":
                print('programacion')
            case "4":
                print('programacion')
            case "0": 
                print('|#| SALIENDO.....')
                break
            case _:
                print('|#|*** INGRESE UNA OPCION VALIDA ***|#|')
        i += 1

    

# Se inicia un bucle que contendra el menu interactivo
while True: 
    limpiar_consola() # Cada vez que entre en el bucle se va a limpiar la consola


    # Menu de opciones
    print('|-|-|-|-|-|## CONTROL DE ALUMNOS ##|-|-|-|-|-|')
    print('|#| ( 1 ) -----> Registrar Alumnos')
    print('|#| ( 2 ) -----> ')
    print('|#| ( 3 ) -----> Mostrar Alumnos')
    print('|#| ( 4 ) -----> ')
    print('|#| ( 5 ) -----> ')
    print('|#| ( 6 ) -----> ')
    print('|#| ( 7 ) -----> ')
    print('|#| ( 0 ) -----> Salir')
    
    opcion = input('|#| OPCION ------------: ')

    # Switch para elegir la opcion
    match  opcion:
            case "1": 
                registrar_alumno()
            case "2":
                print('Cargar Notas de Alumnos')
            case "3":
                listar_Alumnos()
            case "4": 
                print('Calcular promedios')
            case "5":
                print('Bucar Alumnos')
            case "6":
                print('Mostrar Aprobados')
            case "7":
                print('Mostrar Desprobados')
            case "0": 
                print('|#| SALIENDO.....')
                break
            case _:
                print('|#|*** INGRESE UNA OPCION VALIDA ***|#|')

    input('|#| Pulse cualquier tecla para continuar....')