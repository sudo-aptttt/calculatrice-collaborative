def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b

def puissance(a, b):
	return a ** b
def division(a, b):
    """Retourne le quotient de a par b."""
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b


def modulo(a, b):
	return a % b

print("Modulo :", modulo(17, 5))
print("Addition :", addition(5, 3))
print("Soustraction :", soustraction(5, 3))
print("Multiplication :", multiplication(5, 3))
print("Puissance :", puissance(5,3 ))
print("Division :", division(6, 3))
