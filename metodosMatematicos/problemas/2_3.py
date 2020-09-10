num = input("Raíz cuadrada de:")
num1 = int(num)*1

if num1 >= 0:
    p = num1
    i = 0
    while i!=p:
        i=p
        p=(num1/p+p)/2
    print("El resultado es: ",p)
else:
    print("Numero incorrecto")