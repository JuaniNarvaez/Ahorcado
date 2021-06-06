def validar_caracter(texto):
    """
    VALIDA CARA CARACTER QUE SE LEE POR TECLADO PARA LA PALABRA A ADIVINAR.
    """
    while True:
        try:
            letra = input(texto)
            assert (letra.isalpha() and len(letra) == 1) and letra != " "
            break
        except AssertionError:
            print("Recuerde ingresar solo una letra...\n")
        print("Intente nuevamente.\n")
    return letra

def validar_cadena(texto):
    """
    VALIDA EL NOMBRE LEIDO POR TECLADO ESTE CONFORMADO SOLO PPOR LETRAS.
    """
    while True:
        try:
            cadena = input(texto)
            assert cadena.isalpha() and cadena != " "
            break
        except AssertionError:
            print("Recuerde ingresar solo letras...\n")
        print("Intente nuevamente.\n")
    return cadena