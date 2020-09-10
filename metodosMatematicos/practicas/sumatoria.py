# Enhory Munguía | 23 Abril 2020 | icep
#a=1 a<x a=a+1 | s=s+(1/a)


s = 0
n = int(input("Ingresa el límite: "))


for i in range(1, n+1):
    s = s + (1 / i)

print("El resultado es: {:.3f}".format(s))


