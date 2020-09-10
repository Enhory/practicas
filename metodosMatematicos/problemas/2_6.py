import math

c = input("ingrese el valor del conseno: ")
c1 = math.cos(math.radians(float(c)))


def func_cos(x, n):
    cos_approx = 0
    for i in range(n):
        coef = (-1) ** i
        num = x ** (2 * i)
        denom = math.factorial(2 * i)
        cos_approx += coef * (num / denom)

    return cos_approx


print(func_cos(c1, 2))
