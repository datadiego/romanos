class RomanNumber:

    millares = [ "", "M", "MM", "MMM" ]
    centenas = [ "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" ]
    decenas = [ "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" ]
    unidades = [ "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" ]

    conversores = [millares, centenas, decenas, unidades]

    digitos_romanos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def __init__(self, numero):
        """
        Con el constructor puedo instanciar un objeto de tipo RomanNumber
        de dos formas:

        a = RomanNumber(13)  # le paso un entero (valido?)
        b = RomanNumber("XIII")     # le paso una cadena (valida?)
        """
        if isinstance(numero, int):
            self.valor = numero
            self.cadena = self.int_a_romano()
        if isinstance(numero, str):
            for caracter in numero:
                if caracter not in self.digitos_romanos:
                    raise ValueError(f"{caracter} no es un numero romano")
            self.cadena = numero
            self.valor = self.romano_a_int()
        if isinstance(numero, float):
            raise ValueError(f"{numero} debe ser un número romano, un entero o una cadena")
        if isinstance(numero, list):
            raise ValueError(f"{numero} debe ser un número romano, un entero o una cadena")
        if numero == ValueError:
            raise ValueError("Que haces metiendo esto criatura")
        
    def __str__(self) -> str:
        return self.cadena

    def __repr__(self):
        return self.__str__()

    def __eq__(self, otro):
        if isinstance(otro, RomanNumber):
            return self.valor == otro.valor
        if isinstance(otro, int):
            return self.valor == otro
        if isinstance(otro, str):
            return self.cadena == otro
        raise ValueError(f"{otro} debe ser un número romano, un entero o una cadena")
def __gt__(self, otro):
        if isinstance(otro, int):
            return self.valor > otro        

    def __add__(self, sumando):
        """
        RomanNumber + sumando
        """
        if isinstance(sumando, RomanNumber):
            try:
                resultado = self.valor + sumando.valor
                return RomanNumber(resultado)
            except ValueError:
                raise ValueError(f"El resultado ({resultado}) está fuera de rango (debe ser entre 1 y 3999)")
        if isinstance(sumando, int):
            return RomanNumber(self.valor + sumando)
        if isinstance(sumando, str):
            return RomanNumber(self.valor + RomanNumber(sumando).valor)
        raise ValueError(f"{sumando} debe ser un número romano, un entero o una cadena")

    def __radd__(self, sumando):
        return self.__add__(sumando)

    def validar_numero(self):
        """
        Comprueba que el `valor` sea un entero
        con valor entre 1 y 3999 (incluidos).
        """
        if not isinstance(self.valor, int):
            raise ValueError("No has introducido un número")
        if self.valor < 1 or self.valor > 3999:
            raise ValueError ("El número introducido no es válido (debe ser positivo y menor que 4000)")

    def int_a_romano(self):
        """
        Convierte el `valor` numérico a su representación
        en cadena como número romano.
        """
        self.validar_numero()
        numero = self.valor
        divisores = [1000, 100, 10, 1]
        factores = []

        for divisor in divisores:
            cociente = numero // divisor
            resto = numero % divisor
            factores.append(cociente)
            numero = resto

        resultado = ""

        for pos, factor in enumerate(factores):
            resultado = resultado + self.conversores[pos][factor]

        return resultado

    def romano_a_int(self):
        """
        Obtiene el valor numérico de la representación de
        `cadena` del número romano.
        """
        romano = self.cadena

        resultado = 0
        anterior = 0
        restado = False
        cuenta_repetidos = 0

        for letra in romano:
            actual = self.digitos_romanos[letra]

            if anterior >= actual:  # Caso de la suma
                resultado = resultado + actual
                restado = False

            else:  # actual > anterior => Caso de la resta
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

if __name__ == "__main__":
    a = RomanNumber(2)

