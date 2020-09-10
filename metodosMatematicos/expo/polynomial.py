# Interpolacion de Lagrange
# Polinomio en forma simbólica
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INGRESO , Datos de prueba
# Conjunto x
conj_x_1 = float(input(" Conjunto X punto 1: "))
conj_x_2 = float(input(" Conjunto X punto 2: "))
conj_x_3 = float(input(" Conjunto X punto 3: "))
conj_x_4 = float(input(" Conjunto X punto 4: "))
# Conjunto y
print("_____________")
conj_y_1 = float(input(" Conjunto Y punto 1: "))
conj_y_2 = float(input(" Conjunto Y punto 2: "))
conj_y_3 = float(input(" Conjunto Y punto 3: "))
conj_y_4 = float(input(" Conjunto Y punto 4: "))

# xi: 0, 0.33, 0.66, 1
# yi: 1, 1.391, 1.935, 2.718
xi = np.array([conj_x_1, conj_x_2, conj_x_3, conj_x_4])
yi = np.array([conj_y_1, conj_y_2, conj_y_3, conj_y_4])

# PROCEDIMIENTO
n = len(xi)
x = sym.Symbol('x')
# Polinomio
polinomio = 0
for i in range(0, n, 1):
    # Termino de Lagrange
    termino = 1
    for j in range(0, n, 1):
        if (j != i):
            termino = termino * (x - xi[j]) / (xi[i] - xi[j])
    polinomio = polinomio + termino * yi[i]
# Expande el polinomio
px = polinomio.expand()
# para evaluacion numérica
pxn = sym.lambdify(x, polinomio)

# Puntos para la gráfica
a = np.min(xi)
b = np.max(xi)
muestras = 101
xi_p = np.linspace(a, b, muestras)
yi_p = pxn(xi_p)

# Salida
print('Polinomio de Lagrange, expresiones')
print(polinomio)
print('\nPolinomio de Lagrange: ')
print(px)

# Gráfica
plt.title('Interpolación Lagrange')
plt.plot(xi, yi, 'o', label='Puntos', color='black')
plt.plot(xi_p, yi_p, label='Polinomio', color='hotpink')
plt.xlabel('Polinomio de Lagrange: {0}'.format(px))
plt.legend()
plt.show()
