def division(a, b):
    """Retourne le quotient de a par b."""
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b
print("Division :", division(6, 3))
