# Programa para resolver la formula general.
# Enhory Nallely Munguía Preciado | 25 Abril 2020 | icep
import math

x1 = float(0)
x2 = float(0)
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))
discriminante = ((b**2) - 4 * (a * c))

if discriminante < 0:
    print("La ecuación no tiene soluciones reales")
if discriminante == 0:
    print("La ecuación tiene sólo una raíz real")
    x1 = (-b) / (2 * a)
    print("La solición es, x1=x2: {0} ".format(x1))
if discriminante > 0:
    print("La ecuación tiene dos raices reales")
    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)
    print('El El resultado X1 es: {0}'.format(x1))
    print('El El resultado X2 es: {0}'.format(x2))
