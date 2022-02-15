import math
from IPython.display import display, Math

def ulmigthify(a, b, c):
    discriminant = (b**2) - (4 * a * c)
    if discriminant < 0:
        print(f"Equation {a}x^2 {b}x {c} = 0, has no real roots")
    elif  discriminant == 0:
        fac = math.sqrt(discriminant)
        x1 = (-b + fac)/(2*a)
        print(f"root is x = {x1}")
    else:
        fac = math.sqrt(discriminant)
        x1 = (-b + fac)/(2*a)
        x2 = (-b - fac)/(2*a)
        print(f"roots ar x1 = {x1}, x2 = {x2}")


a_in = int(input("a: "))
b_in = int(input("b: "))
c_in = int(input("c: "))

ulmigthify(a_in, b_in, c_in)