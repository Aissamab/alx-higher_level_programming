#!/usr/bin/python3
def safe_print_division(a, b):
    resultat = 0

    try:
        resultat = a / b
    except ZeroDivisionError:
        resultat = None
    finally:
        print('Inside result: {}'.format(resultat))
        return resultat
