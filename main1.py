import matplotlib.pyplot as plt
from math import pi, sin, cos


def cot(arg: float) -> float:
    """котангенс угла"""
    return cos(arg) / sin(arg)


N = 2
Xa = 100
Xb = 150 + 2 * N
Ya = 200
Yb = 200 - 2 * N
a = 20 + 2 * N
b = 360 - 15 - 2 * N

# Перевод в радианы
a = a * pi / 180
b = b * pi / 180
print('\na = ', a)
print('b = ', b)

ka = -cot(a)
kb = cot(b)
print('\nka = ', ka)
print('kb = ', kb)


Ba = Ya - ka * Xa
Bb = Yb - kb * Xb
print('\nBa = ', Ba)
print('Bb = ', Bb)


lst_x = []
lst_y = []
x = list(range(1, 501))

# CENTER
Xc = ((cot(b) * Xb + cot(a) * Xa + Ya - Yb)) / (cot(b) + cot(a))
Yc = cot(b) * (Xc - Xb) + Yb

for i in range(len(x)):
    lst_x.append(ka * x[i] + Ba)
    lst_y.append(kb * x[i] + Bb)

plt.plot(x, lst_x, 'b-')
plt.plot(x, lst_y, 'g-')
plt.plot(Xc, Yc, 'ro-', label='[ ' + str(round(Xc, 2)) + ' ; ' + str(round(Yc, 2)) + ' ]')

plt.legend(loc='best')
plt.grid()
plt.show()
