#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        resulat = a / b
    except:
        resulat = None
    finally:
        print("Inside result: {}".format(resulat))
    return resultat
