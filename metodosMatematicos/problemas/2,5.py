import math
"""
comparar resultado
http://es.onlinemschool.com/math/assistance/equation/quadratic/
"""
print("programa ecuación cuadratica (ax²+bx+c=0)\n")
a = int(input("ingresa coeficiente cuadratico:"))
b = int(input("ingresa coeficiente lineal:"))
c = int(input("ingresa constante:"))
disc = b * b - 4 * a * c
if a != 0:
    if disc < 0:
        print("tiene raices en 0")
    else:
        x1 = (-b + (math.sqrt(disc))) / (2 * a)
        x2 = (-b - (math.sqrt(disc))) / (2 * a)
        print("X1 = " + str(x1) + " X2 = " + str(x2))
else:
    print("coefiente cuadratico debe ser diferente de cero")
