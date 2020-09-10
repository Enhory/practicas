

from math import pi

s = 0
for i in range(10000 -1):
    try:
        s = s + 1 / i ** 4
    except ZeroDivisionError:
        s = 0
disp = (((pi ** 4) / 90 - s) / ((pi ** 4) / 90))

print(s)
print("{0} %".format(disp))



