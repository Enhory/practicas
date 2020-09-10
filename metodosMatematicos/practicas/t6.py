import os
# Python3 program to convert
# binary to decimal
#Enhory Nallely Munguia Preciado | Jennifer Annette Velasco Villalvazo | 17 Abril 2020 | ICEP - Métodos Numéricos
a = 1011101
b = 101.101
c = 0.01101


print("\nConvertidor de números binarios a decimal")
print("Favor de ingresar la opción deseada para convertirla a decimal")


def binaryToDecimal(n):
    num: object = n
    deci = 0

    # Initializing base
    # value to 1, i.e 2 ^ 0
    base = 1
    temporal = num
    while temporal:
        last_digit = temporal % 10
        temporal = int(temporal / 10)
        deci += last_digit * base
        base = base * 2
    return deci


def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    os.system('cls')  # NOTA para windows tienes que ser cls y para mac debe ser clear
    print("\nOpciones:\n a)1011101\n b)101.101\n c)0.01101\n d)otro\n e)salir")


while True:
    # Mostramos el menu
    menu()

    # solicituamos una opción al usuario
    p = input("ponga la opción: ").capitalize()

    if p == "a".capitalize():
        print("este es el número {0} decimal".format(str(binaryToDecimal(a))))
    elif p == "b".capitalize():
        print("este es el número {0} decimal".format(binaryToDecimal(float(b))))
    elif p == "c".capitalize():
        print("este es el número {0} decimal".format(binaryToDecimal(float(c))))
    elif p == "d".capitalize():
        bi = input("Inserte el número binario: ")
        print("este es el número: {0} decimal".format(binaryToDecimal(float(bi))))
    elif p == "e".capitalize():
        print("Adiós")
        break
    else:
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")