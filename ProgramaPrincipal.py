from funciones_archivos import *
from funciones_auxiliares import *
from funciones_impresiones import *
from funciones_validaciones import *


def comienza_juego(categ):
    """
    Contiene las funciones para obtener la palabra incognita , validacion de los caracteres que se lean por teclado
    y gererar la palabra incognito solo mostrando el primer carater (si se repite ese caracter se coloca en todas las posiciones necesarias).
    """
    seguir_juego = True
    matriz_dibujo = [["", " ", "┌", "─", " ┐", " "], ["", " ", " ", " ", " ", "|"], ["", " ", " ", " ", " ", "|"],
                     ["", " ", " ", " ", " ", "|"], ["", "_", "_", "_", "_", "|"]]
    incorrectas = []
    palabra = obtener_palabra_por_categoria(categ)
    incognita = ['_' for i in range(0, len(palabra))]
    asignar_caracter_en_incognita(incognita, palabra, palabra[0])

    imprimirmatriz(matriz_dibujo)

    print("ADIVINA LA PALABRA")
    aux_p = 0
    while seguir_juego:

        print(*incognita)

        while incognita.count("_") >= 1:
            # falta validar caracter.
            caracter = validar_caracter("Ingrese caracter: ")
            aux_p += 1
            if existe_caracter_en_cadena(caracter, palabra):
                asignar_caracter_en_incognita(incognita, palabra, caracter)
            else:
                print(agregar_caracter_en_lista(caracter, incorrectas, matriz_dibujo))

            if incognita.count("_") == 0:
                ganador = True
                seguir_juego = False
                print("La palabra incógnita era: ", *incognita)
                break

            if len(incorrectas) == 6:
                ganador = False
                seguir_juego = False
                print("Letras incorrectas ", incorrectas)
                break

            print("La palabra incógnita es: ", *incognita)
            print("Letras incorrectas ", incorrectas)

    return ganador, palabra


def menu_principal():
    """
    Muestra el menu principal y valida las que la respuesta sea valida.
    """
    print("+"+'-'*85+"+\n|"+" "*35+"MENÚ PRINCIPAL"+" "*36+"|\n"+"+"+'-'*85+"+\n")
    print('Seleccioná una de las siguientes opciones:\n'.center(90))
    texto_menu = "1- Comenzar Nueva Partida" \
                 "\n2- Ver Reglas del Juego\n3- Ver Créditos\n0- Salir del Juego\n\nOpción Seleccionada: "
    lst_opc = list(range(0, 4))
    opc_exit = 0
    opc, salir = prompt_opciones_numericas(texto_menu, lst_opc, opc_exit)

    partida_ganada = 0
    partida_perdida = 0
    if salir:
        return 1
    else:
        if opc == 1:
            nombre_jugador = validar_cadena("Ingrese su nombre: ")
            categ, salida = seleccionar_categoria(nombre_jugador)
            if not salida:
                gano, palabra_adivinar = comienza_juego(categ)
                print()

                if gano:
                    print("\n --- GANASTE  ---\n")
                    partida_ganada += 1
                    time.sleep(3)
                else:
                    print("\n --- PERDISTE ---\n")
                    print(f'La palabra era: {palabra_adivinar}\n')
                    partida_perdida += 1
                    time.sleep(3)

            agregar_actualizar_reg_archivo_jugadores(nombre_jugador, partida_ganada, partida_perdida)

            menu_principal()
        elif opc == 2:
            mostrarReglas()
            print()
            menu_principal()
        elif opc == 3:
            imprimir_creditos()
            print()
            menu_principal()


# Programa Principal
menu_bienvenida()
if validar_dependencias():
    menu_principal()
    mostrar_jugadores()
    print("Hasta pronto!.")
else:
    print("Error: Faltan archivos críticos para comenzar el juego.")
