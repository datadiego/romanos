def convertir_en_romano(numero):
    """
    Restricciones:
        - Es un número natural
        - El número está entre 0 y 3999
            - no es negativo
            - no es mayor que 3999
    Resultado es una cadena que contiene (I, V, X, L, C, D, M)

    Ideas para comprobar un entero:
            - (X) isdigit(): porque no aplica a cualquier cosa que no sea cadena
        - (V) convertir a int y si no se puede, error
        - (V) isinstance()
            - (V) type()
            - (X) isnumeric()

    Pasos:
        1. Validar la entrada
        2a. Si es válido: lo convierto
        2b. Si no es válido: muestro un error
    """
    millares = [ "", "M", "MM", "MMM" ]
    centenas = [ "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" ]
    decenas = [ "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" ]
    unidades = [ "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" ]

    conversores = [millares, centenas, decenas, unidades]

    if not isinstance(numero, int):
        return "No has introducido un número"
    if numero < 1 or numero > 3999:
        return "El número introducido no es válido (debe ser positivo y menor que 4000)"

    divisores = [1000, 100, 10, 1]
    factores = []

    for divisor in divisores:
        cociente = numero // divisor
        resto = numero % divisor
        factores.append(cociente)
        numero = resto

    resultado = ""

    for pos, factor in enumerate(factores):
        resultado = resultado + conversores[pos][factor]

    return resultado


def convertir_a_numero(romano):
    """
    MCXXIII: 1123
        - de izquierda a derecha
        - convertir cada letra en su valor
        - sumo los valores si a la izquierda hay un dígito mayor que a la derecha
            - VI: sumo ==> 6
        - resto si el valor de la izquierda es menor que el de la derecha
            - IV: resto ==> 4

        1. leo una letra y guardo su valor (letra1)
        2. leo otra letra (letra2)
            2a. si letra2 > letra1 =>  resultado = letra2 - letra1
            2b. si no => resultado letra2 + letra1
    """

    digitos_romanos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    resultado = 0
    anterior = 0
    restado = False
    cuenta_repetidos = 0

    for letra in romano:
        actual = digitos_romanos[letra]

        if anterior >= actual:  # Caso de la suma
            resultado = resultado + actual
            restado = False

        else:  # actual > anterior => Caso de la resta
            """
            # antes de restar voy a ver si la resta es posible
            # validando que no puedo restar si hay más de un orden
            # de magnitud entre anterior y actual
            #   3   2   1   0
            # 10  10  10  10
            # 1123 = 1*10^3 + 1*10^2 + 2*10^1 + 3*10^1 = 1000 + 100 + 20 + 3
            # anterior < actual

            # IV  ---   anterior=1,   actual=5         10 ---- 5
            # IX  ---   anterior=1,   actual=10        10 ---- 10
            # CM  ---   anterior=100, actual=1000    1000 ---- 1000

            # IC  ---   anterior=1,   actual=100      10 ---- 100
            # XM  ---   anterior=10,  actual=1000    100 ---- 1000

            # I   ---   anterior=0,   actual=1         0 ---- 1
            # X   ---   anterior=0,   actual=10        0 ---- 10

            # actual - anterior*10 ---> si cero o negativo OK
            #                      ---> si positivo KO

            # IV
            # anterior=0, actual=1 ----    0 <= 1 ////  1 - 0 > 0
            # anterior=1, actual=5         0 <= 10 //// 10 > 0

            # if (actual - anterior*10) > 0:
            # if anterior > 0 and anterior*10 < actual:
            # if anterior*10 > 0 and anterior*10 < actual:

            # if anterior == 5 or anterior == 50 or anterior == 500:
            """
            if cuenta_repetidos == 1:   # > 0
                raise ValueError("No se pueden restar símbolos repetidos")

            if restado:
                raise ValueError("No puedes restar más de un símbolo")

            if anterior in (5, 50, 500):
                raise ValueError("No se puede restar un número múltiplo de 5")

            if 0 < anterior*10 < actual:
                raise ValueError("No se puede restar más de un orden de magnitud")

            resultado = resultado - anterior
            resultado = resultado + (actual - anterior)
            if anterior > 0:
                restado = True

        if anterior == actual:  # MMMXCIII
            cuenta_repetidos = cuenta_repetidos + 1
            if actual in (5, 50, 500):
                raise ValueError("No se puede restar un número múltiplo de 5")
            if cuenta_repetidos > 2:
                raise ValueError("No puedes tener más de tres símbolos iguales")
        else:
            cuenta_repetidos = 0

        anterior = actual
    return resultado

if __name__ == '__main__':
    print(convertir_a_numero("MMMM"))
    # print(convertir_a_numero("MMMXCIII"))
