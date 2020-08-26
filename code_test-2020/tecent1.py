print(pow(3, 3))

line = "2 3 1 2"
def integrate(A, B, x):
    return A/3 * pow(x, 3) + 0.5 * pow(x, 2) + B * x
def origin(A, B, x):
    return A * pow(x, 2) + x + B


A, B, C, D = [int(n) for n in line.split()]
midLine = -1 / 2 / A
res = 0
if (C - midLine) * (D - midLine) >= 0:
    res = abs(integrate(A, B, D) - integrate(A, B, C))
else:
    pass
print(round(res, 6))

