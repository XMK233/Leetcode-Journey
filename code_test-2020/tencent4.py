stdin = [
    "6 5",
    "1 3",
    "2 3",
    "3 5",
    "4 5",
    "5 6",
]
import collections
map1 = collections.defaultdict(list)
for i, line in enumerate(stdin):
    if i == 0:
        pass
    else:
        p1, p2 = line.split()
        map1[p1].append(p2)
        map1[p2].append(p1)
map2 = collections.defaultdict(list)
for key in map1:
    value = map1[key]
    sv = ",".join(sorted(value))
    map2[sv].append(key)
# print(map2)
###
def getV(n):
    if n == 1:
        return 1
    else:
        return n * getV(n - 1)
def combination(n, m):
    if n == m:
        return 1
    else:
        up = getV(n)
        down1 = getV(m)
        down2 = getV( n - m)
        return up // (down1 * down2)
# print(combination(5, 3))
num = 0
for key in map2:
    value = map2[key]
    l = len(value)
    if l < 2:
        continue
    num += combination(l, 2)
print(num)
