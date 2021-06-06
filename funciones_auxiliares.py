from funciones_impresiones import *


def existe_caracter_en_cadena(caracter, palabra):
    """ VERIFICA QUE EL CARACTER LEIDO POR TECLADO NO ESTE YA INGRESADO. """
    ret = False
    caracter = caracter.upper()
    if caracter in palabra:
        ret = True
    return ret


def agregar_caracter_en_lista(caracter, lista, matriz):
    """ AGREGA EL CARACTER LEIDO POR TECLADO A LA LISTA DE ERRORES Y VERIFICA QUE NO ESTE REPETIDO. """
    caracter = caracter.upper()
    if caracter in lista:
        msg = "Ya dijiste esa letra\n"
    else:
        msg = "\n"
        lista.append(caracter.upper())
        dibujar_error(len(lista), matriz)
    return msg


def asignar_caracter_en_incognita(incognita, palabra, caracter):
    """ AGREGA EL CARACTER EN LA POSICION CORRESPONDIENTE DE LA PALABRA INCOGNITA. """
    for i in range(0, len(palabra)):
        # print(str(i) + palabra[i])
        aux_c_l = caracter
        aux_c_u = caracter
        if aux_c_u.upper() == palabra[i] or aux_c_l.lower() == palabra[i]:
            incognita[i] = caracter.upper()


def seleccionar_categoria(jugador):
    """ MUESTRA POR PANTALLA LAS CATEGORIAS Y LLAMA A LA FUNCION PARA VALIDAR QUE SEA CORRECTA LA OPCION ELEGIDA. """
    texto_menu = f"\n\n{jugador}, ahora seleccioná la categoria con la que querés jugar, ingresando el valor de la " \
                 f"lista.\n\n1- Animales\n2- Paises\n3- Objetos\n0- Para volver al Menú Anterior\n\nOpción " \
                 f"Seleccionada: "
    lst_Opc = list(range(0, 4))
    opc_Exit = 0
    opc, salir = prompt_opciones_numericas(texto_menu, lst_Opc, opc_Exit)
    return opc, salir


def prompt_opciones_numericas(texto, opciones, opcion_salida):
    """ VERIFICA LO QUE SE LEE POR TECLADO SEA UN NUMERO, CORRESPONDIENTE A UNA CATEGORIA. """
    opc = input(texto)
    while not opc.isdigit() or int(opc) not in opciones:
        print("Recuerde que debe ingresar una opción válida y solamente números...")
        print()
        opc = input(texto)
    else:
        if (int(opc) == opcion_salida):
            opcion = int(opc)
            salir = True
        else:
            opcion = int(opc)
            salir = False
    return opcion, salir
