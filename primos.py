"""
Gestió de nombres primers.

Nom: Biel Batet Tudela

Tests unitaris:
    >>> [numero for numero in range(2, 50) if esPrimo(numero)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)

    >>> mcm(90, 14)
    630

    >>> mcd(924, 780)
    12

    >>> mcm(42, 60, 70, 63)
    1260

    >>> mcd(840, 630, 1050, 1470)
    210
"""


def esPrimo(numero):
    """Retorna True si numero és primer, False si no ho és.

    Args:
        numero: nombre natural major que 1

    Returns:
        True si és primer, False si no ho és

    Raises:
        TypeError: si numero no és un natural major que 1
    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("numero ha de ser un natural major que 1")
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def primos(numero):
    """Retorna una tupla amb tots els nombres primers menors que numero.

    Args:
        numero: nombre natural major que 1

    Returns:
        tupla amb tots els primers menors que numero
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))


def descompon(numero):
    """Retorna una tupla amb la descomposició en factors primers de numero.

    Args:
        numero: nombre natural major que 1

    Returns:
        tupla amb els factors primers de numero
    """
    factors = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factors.append(divisor)
            numero //= divisor
        divisor += 1
    return tuple(factors)


def mcm(*numeros):
    """Retorna el mínim comú múltiple dels arguments.

    Args:
        *numeros: dos o més nombres naturals

    Returns:
        mínim comú múltiple dels arguments
    """
    def mcm_dos(a, b):
        factors_a = list(descompon(a))
        factors_b = list(descompon(b))
        factors_b_copia = factors_b.copy()
        for f in factors_a:
            if f in factors_b_copia:
                factors_b_copia.remove(f)
        resultat = factors_a + factors_b_copia
        producte = 1
        for f in resultat:
            producte *= f
        return producte

    resultat = numeros[0]
    for n in numeros[1:]:
        resultat = mcm_dos(resultat, n)
    return resultat


def mcd(*numeros):
    """Retorna el màxim comú divisor dels arguments.

    Args:
        *numeros: dos o més nombres naturals

    Returns:
        màxim comú divisor dels arguments
    """
    def mcd_dos(a, b):
        factors_a = list(descompon(a))
        factors_b = list(descompon(b))
        factors_comuns = []
        factors_a_copia = factors_a.copy()
        for f in factors_b:
            if f in factors_a_copia:
                factors_comuns.append(f)
                factors_a_copia.remove(f)
        resultat = 1
        for f in factors_comuns:
            resultat *= f
        return resultat

    resultat = numeros[0]
    for n in numeros[1:]:
        resultat = mcd_dos(resultat, n)
    return resultat


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)