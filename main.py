import matplotlib.pyplot as plt
import scipy.optimize as opt
from math import sqrt


def f1(variables):
    (x, y) = variables
    first_eq = (x - xa) ** 2 + (y - ya) ** 2 - R1 ** 2
    second_eq = (x - xb) ** 2 + (y - yb) ** 2 - R2 ** 2
    return second_eq, first_eq


def f2(variables):
    (x, y) = variables
    first_eq = (x - xb) ** 2 + (y - yb) ** 2 - R2 ** 2
    second_eq = (x - xc) ** 2 + (y - yc) ** 2 - R3 ** 2
    return first_eq, second_eq


def f3(variables):
    (x, y) = variables
    first_eq = (x - xa) ** 2 + (y - ya) ** 2 - R3 ** 2
    second_eq = (x - xc) ** 2 + (y - yc) ** 2 + R1 ** 2
    return first_eq, second_eq


N = 6
xa = 100
xb = 140 + N
xc = 160 + N
ya = 100
yb = 140 + N
yc = 65 + N
R1 = 40 + N
R2 = 40 + N
R3 = 40 + N

x1, y1 = opt.fsolve(f1, (0.1, 1))
x2, y2 = opt.fsolve(f2, (0.1, 1))
x3, y3 = opt.fsolve(f3, (0.1, 1))
x1, y1, x2, y2, x3, y3 = 100, 100, 146, 146, 166, 71


print('\nx\u2081 - ', x1, '\t\ty\u2081 - ', y1)
print('x\u2082 - ', x2, '\ty\u2082 - ', y2)
print('x\u2083 - ', x3, '\ty\u2083 - ', y3)

aa = sqrt((x2 - x1) ** 2 - (y2 - y1) ** 2)
print('\naa = ', aa)

bb = sqrt((x3 - x2) ** 2 - (y2 - y3) ** 2)
print('bb = ', bb)

cc = sqrt(abs((x3 - x1) ** 2 - (y1 - y3) ** 2))
print('cc = ', cc)

h = (aa + bb + cc) / 2
print('\nh = ', h)

S = sqrt(h * (h - aa) * (h - bb) * (h - cc))
print('S = ', S)
# -----------------------CIRCLES--------------------------
fig, ax = plt.subplots()

# Change default range so that new circles will work
ax.set_xlim((50, 210))  # Limit x
ax.set_ylim((20, 200))  # Limit y

# Set canvas settings
ax.set_aspect("equal")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Circles")
plt.grid()

# Create objects
circle1 = plt.Circle((xa, ya), R1, color='r', fill=False)
circle2 = plt.Circle((xb, yb), R2, color='g', fill=False)
circle3 = plt.Circle((xc, yc), R3, color='b', fill=False)

# Centers
plt.plot(xa, ya, 'ro')
plt.plot(xb, yb, 'go')
plt.plot(xc, yc, 'bo')
plt.text(xa - 5, ya + 5, 'O\u2081', horizontalalignment="center")
plt.text(xb + 5, yb + 5, 'O\u2082', horizontalalignment="center")
plt.text(xc - 5, yc - 8, 'O\u2083', horizontalalignment="center")

# Output objects
ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)

# Black dots
plt.plot(x1, y1, 'k.')
plt.plot(x2, y2, 'k.')
plt.plot(x3, y3, 'k.')
plt.text(x1 + 30, y1 - 5, '(' + str(x1) + ' ; ' + str(y1) + ')', horizontalalignment="center")
plt.text(x2 + 20, y2 + 5, '(' + str(round(x2, 1)) + ' ; ' + str(round(y2, 1)) + ')', horizontalalignment="center")
plt.text(x3 + -25, y3 + -10, '(' + str(round(x3, 1)) + ' ; ' + str(round(y3, 1)) + ')', horizontalalignment="center")

plt.savefig('circles.png', bbox_inches='tight')
# -----------------------CIRCLES--------------------------
