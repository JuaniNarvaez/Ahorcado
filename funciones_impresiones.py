import time

def imprimirmatriz(matriz):
    """
    iMPRIME MATRIZ DE LA HORCA POR PANTALLA.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for f in range (columnas):
            n = ""
            if matriz[i][f] == matriz[0][0]:
                print (n.rjust(25," "),end="")
            
            print("%1s"%matriz[i][f],end="")
        
        print()

def mostrar_cabeza(matriz):
    """
    AGREGA LA CABEZA AL PRIMER ERROR.
    """
    matriz[1][2] = "O"

def mostrar_torso(matriz):
    """
    AGREGA EL CUERPO AL SEGUNDO ERROR.
    """
    matriz[2][2] = "|"

def mostrar_brazo_izq(matriz):
    """
    AGREGA UN BRAZO AL TERCER ERROR.
    """
    matriz[2][1] = "/"

def mostrar_brazo_der(matriz):
    """
    AGREGA UN BRAZO AL CUARTO ERROR.
    """
    matriz[2][3] = '\\'

def mostrar_pierna_izq(matriz):
    """
    AGREGA UNA PIERNA AL QUINTO ERROR.
    """
    matriz[3][1] = "/"

def mostrar_pierna_der(matriz):
    """
    AGREGA UNA PIERNA AL SEXTO ERROR.
    """
    matriz[3][3] = '\\'


def dibujar_error(cantidad, matriz):
    """
    VALIDA CADA ERROR PARA QUE LAS FUNCIONES AGREGEN LOS ERRORES EN LA MATRIZ.
    """
    if cantidad == 1:
        mostrar_cabeza(matriz)
    elif cantidad == 2:
        mostrar_torso(matriz)
    elif cantidad == 3:
        mostrar_brazo_izq(matriz)
    elif cantidad == 4:
        mostrar_brazo_der(matriz)
    elif cantidad == 5:
        mostrar_pierna_izq(matriz)
    elif cantidad == 6:
        mostrar_pierna_der(matriz)

    imprimirmatriz(matriz)

def mostrarReglas():
    """
    MUESTRA POR PANTALLA LAS REGLAS DEL JUEGO.
    VALIDA QUE EXISTA EL ARCHIVO.
    """
    print("\nReglas del Juego")
    print("================")
    try:
        archivo = open('reglas.txt', 'r')
        for linea in archivo:
            print(linea)
    except OSError as mensaje:
        print("No existe el archivo" + mensaje)
    finally:
        try:
            archivo.close()
        except NameError:
            print("Ocurrió un Error al intentar cerrar el archivo.")

def imprimir_creditos():
    """
    MUESTRA POR PANTALLA LOS INTEGRANTES DEL GRUPO CREADOR DEL JUEGO.
    """
    print("PROGRAMADO POR".center(85))
    
    listas_alumnos = [['Fernando', 'Ferreyra Lima', 1137834, 'fferreyralima@uade.edu.ar'], ['Florencia', 'Biondo', 1123526, 'mabiondo@uade.edu.ar'],
     ['Juan Ignacio', 'Fay Narvaez', 1131974, 'jfaynarvaez@uade.edu.ar'], ['Sergio', 'Montañez', 1035375, 'smontanez@uade.edu.ar']]

    tabla = """\
+-------------------------------------------------------------------------------------+
| Nombre               Apellido              Legajo              Mail                 |
|-------------------------------------------------------------------------------------|
{}
+-------------------------------------------------------------------------------------+\
"""   
    tabla = (tabla.format('\n'.join("| {:<20} {:<20} {:<10} {:<30} |".format(*fila)
     for fila in listas_alumnos)))
    print (tabla)
    

    print("""
+-------------------------------------------------------------------------------------+
|  UADE - Materia: Programacion I - Grupo: 7 - Profesor: Ricardo Thompson - Año: 2021 |
+-------------------------------------------------------------------------------------+
""")
    
    time.sleep(2)

def menu_bienvenida():
    """
    Crea mensaje de bienvenida al juego.
    """
    
    print()
    print('BIENVENIDO/A AL:'.center(85))
    
    print(""" 
                     /\   | |                           | |   
                    /  \  | |__   ___  _ __ ___ __ _  __| | ___  
                   / /\ \ | '_ \ / _ \| '__/ __/ _` |/ _` |/ _ \ 
                  / ____ \| | | | (_) | | | (_| (_| | (_| | (_) |
                 /_/    \_\_| |_|\___/|_|  \___\__,_|\__,_|\___/ """)
    print('\n\n')
    
    imprimir_creditos()    
