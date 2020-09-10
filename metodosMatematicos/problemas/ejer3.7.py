# a) Evalúe el polinomio y=x^3-7x^2+8x+0.35 en x=1.37. Utilice aritmética de 3 dígitos con corte.
#Evalúe el error relativo porcentual.
# b) Repita el inciso a) pero exprese a y como y=[(x-7)x+8]x+0.35. Evalúe el error y compárelo con el inciso a).
import math
import math

x = 1.37

y = x**3 - 7*x**2 + 8*x + 0.35
y2 = ((x - 7) * x + 8) * x + 0.35

print("Y= {:.3f}".format(y))
print("Y2= {:.3f}".format(y2))