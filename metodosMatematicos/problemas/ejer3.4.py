#

from math import pi

s = 0
for i in range(1, 10000):
    s = s + 1 / i ** 4

disp = (((pi ** 4) / 90 - s) / ((pi ** 4) / 90))

print(s)
print("{0} %".format(disp))




