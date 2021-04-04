import math

k = int(input())
r = 1
for i in range(k):
    z, p = input().split()
    if z == "1":
        r += int(p)
    elif z == "2":
        r *= int(p)
    else:
        r = int(math.ceil(r / int(p)))
print(r)