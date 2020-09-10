XI = float(input("Introducir el valor Inferior: "))
Xu = float(input("Introducir el valor Superior: "))
Xr = ((XI + Xu) / 2)

if XI * Xu < 0:
    print("La raíz se encuentra dentro del subintervalo inferior o izquierdo")
    Xu = Xr
    print("La solición es, Xu=Xr: {0} ".format(Xu))

if XI * Xr > 0:
    print("La raíz se encuentra dentro del subintervalo superior o derecho")
    XI = Xr
    print("La solición es, XI = Xr: {0} ".format(XI))

if XI * Xr == 0:
    print("La raíz es igual a: {0}".format(Xr))

