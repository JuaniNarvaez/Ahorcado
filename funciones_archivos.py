import random


def cantidad_registros_de_archivo(ruta):
    """ RECORRE TODO EL ARCHIVO PARA SABER LA CANTIDAD REGISTROS QUE CONTIENE. """
    cantidad = 0
    try:
        archivo = open(ruta, "r")
        for i in archivo:
            cantidad += 1
    except OSError as mensaje:
        print("No existe el archivo")
    finally:
        try:
            archivo.close()
        except NameError:
            print("Ocurrió un Error al intentar cerrar el archivo.")
    return cantidad


def mostrar_jugadores():
    """ MUESTRA POR PANTALLA LOS RESULTADOS HISTORICOS DE LOS JUGADORES Y SUS NOMBRES. """
    str_encabezado = "\nLos SCORE de los jugadores del ahorcado son:\n"
    print(str_encabezado.ljust(10, '-'))
    try:
        archivo = open('jugadores.txt', 'r')
        print('-' * 42)
        print('{:<15} {:<15} {:<15}'.format('JUGADOR', 'GANADAS', 'PERDIDAS'))
        print('-' * 42 + '\n')
        linea = archivo.readline()
        while linea:
            nombre, ganadas, perdidas = linea.split(";")
            print('{:<17} {:<17} {:<14}'.format(nombre, ganadas, perdidas))
            linea = archivo.readline()
        print('-' * 40)

    except OSError as mensaje:
        print("No existe el archivo" + mensaje)
    finally:
        try:
            archivo.close()
        except NameError:
            print("Ocurrió un Error al intentar cerrar el archivo de Jugadores.")


def agregar_actualizar_reg_archivo_jugadores(nombre_mayuscula, ganadas, perdidas):
    """ AGREGA EL NOMBRE DEL JUGADOR Y SU SCORE AL ARCHIVO DE JUGADORES. """
    try:
        nombre = nombre_mayuscula.upper()
        existe = False
        copia_archivo("jugadores.txt", "jugadoresaux.txt")
        archivo = open('jugadores.txt', 'w')
        archivo_copia = open('jugadoresaux.txt', 'r')
        for linea in archivo_copia:
            n_aux, g_aux, p_aux = linea.split(';')
            if nombre == n_aux:
                existe = True
                ganadas = ganadas + int(g_aux)
                perdidas = perdidas + int(p_aux)
                linea = nombre + ";" + str(ganadas) + ";" + str(perdidas) + "\n"
            archivo.write(linea)
        if not existe:
            archivo.write(nombre + ";" + str(ganadas) + ";" + str(perdidas) + "\n")
    except OSError as mensaje:
        print("No existe el archivo" + mensaje)
    finally:
        try:
            archivo.close()
            archivo_copia.close()
        except NameError:
            print("Ocurrió un Error al intentar cerrar los archivos de copia.")


def validar_dependencias():
    """
    VERIFICA QUE EXISTAN LOS ARCHIVOS NECESARIOS PARA COMENZAR Y FINALIZAR EL JUEGO.
    """
    dependencia_jugadores("jugadores.txt")
    valido = True
    if not dependencia_file("categoria1.txt"):
        valido = False
    elif not dependencia_file("categoria2.txt"):
        valido = False
    elif not dependencia_file("categoria3.txt"):
        valido = False

    return valido


def dependencia_file(archA):
    """
    VERIFICA EXISTENCIA DE UN ARCHIVO SEGUN UNA RUTA POR PARÁMETRO.
    """
    try:
        archivoA = open(archA, "r")
        archivoA.close()
        return True
    except FileNotFoundError as mensaje:
        print("No existe el archivo", str(archA))
        return False


def dependencia_jugadores(archA):
    try:
        archivoA = open(archA, "rt")
    except FileNotFoundError as mensaje:
        print("No existe el archivo", str(archA), mensaje, "se creara para jugar")
        archivoA = open(archA, "wt")
        archivoA.close()


def copia_archivo(archA, archB):
    """
    RECIBE LA RUTA DE DOS ARCHIVOS Y COPIA EL CONTENIDO DEL archivoA EN EL archivoB.
    """
    try:
        archivoA = open(archA, "r")
        archivoB = open(archB, "w")
        for linea in archivoA:
            archivoB.write(linea)
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    finally:
        try:
            archivoA.close()
            archivoB.close()
        except NameError:
            print("Ocurrió un Error al intentar cerrar los archivos a copiar.")


def obtener_palabra_por_categoria(categoria):
    """ SELECIONA UNA PALABRA AL AZAR DE TODO EL ARCHIVO. """
    nombre_archivo = f'categoria{categoria}.txt'
    cant_registros = cantidad_registros_de_archivo(nombre_archivo)

    if cant_registros > 0:
        nro_azar = random.randint(1, cant_registros)
        try:
            archivo = open(nombre_archivo, 'r')
        except FileNotFoundError as mensaje:
            print("No se puede abrir el archivo:", mensaje)

    pasada = 0
    palabra = ''
    for linea in archivo:
        pasada += 1
        palabra = linea

        if pasada == nro_azar:
            break
    try:
        archivo.close()
    except NameError:
        print("Ocurrió un Error al intentar cerrar el archivo de categorias.")

    palabra = palabra.rstrip('\n')
    incognita = palabra.upper()
    return incognita
