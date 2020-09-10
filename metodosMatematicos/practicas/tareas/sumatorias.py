# Enhory Munguía | 23 Abril 2020 | icep


n = int(input("Ingresa el límite: "))

# Ejercicio No 1
s = 0
i = int
for i in range(1, n + 1):
    s += i
print("El resultado 1 es: {:.3f}".format(s))

# Ejercicio No 2
a = 0
for i in range(1, n + 1):
    a = a + 2 * i
print("El resultado 2 es: {:.3f}".format(a))

# Ejercicio No 3
b = 0
for i in range(1, n + 1):
    b += 2 * i - 1
print("El resultado 3 es: {:.3f}".format(b))

# Ejercicio No 4
c = 0
for i in range(1, n + 1):
    c +=( ((2 * i)) - 1) / (i*(i+1))
print("El resultado 4 es: {:.3f}".format(c))

# Ejercicio No 5
d = 0
for i in range(1, n + 1):
    d += ((i + 1) / i)
print("El resultado 5 es: {:.3f}".format(d))

# Ejercicio No 6
e = 0
for i in range(1, n + 1):
    e += ((i ** 2) / (i + 1))
print("El resultado 6 es: {:.3f}".format(e))
