# operaciones.py
# Funciones básicas de operaciones matemáticas

def suma(a, b):
    """Devuelve la suma de a y b"""
    return a + b


def resta(a, b):
    """Devuelve la resta de a y b"""
    return a - b


def multiplicacion(a, b):
    """Devuelve la multiplicación de a y b"""
    return a * b


def division(a, b):
    """Devuelve la división de a entre b. Controla la división por cero."""
    if b == 0:
        return "Error: división por cero"
    return a / b
