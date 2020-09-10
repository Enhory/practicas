#Figura 3.10 Programa para sumar un número 10^5 veces.
#Se suma el número con presición simple y el número 10^-5 con presición simple y doble.
import numpy as np

sum1 = 0.0
sum2 = 0.0
sum3 = np.float64(0.0)
x1 = 1.0
x2 = np.float32(1.1e-5)
x3 = np.float64(1.e-5)

for i in range(10000):
    sum1 = sum1 + x1
    sum2 = sum2 + x2
    sum3 = sum3 + x3
print(sum1)
print(sum2)
print(sum3)